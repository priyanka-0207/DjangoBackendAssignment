var url = document.getElementById('signup-api-url').getAttribute('data-url');

$(document).ready(function() {
    $('#signup_form').submit(function(event) {
      event.preventDefault();
      var formData = JSON.stringify($(this).serializeArray());
      var selectedValue = document.getElementById("gender").value;

      var obj = JSON.parse(formData);
      obj.push({"name":"gender","value":selectedValue})
      var formData = JSON.stringify(obj);
  
      $.ajax({
        url: url,
        type: 'POST',
        contentType: 'application/json',
        data: formData,
        success: function(response) {
          console.log(response);
        },
        error: function(xhr, errmsg, err) {
          console.log(xhr.status + ': ' + xhr.responseText);
          var errorBanner = document.getElementById("error-banner");
          var errorMessage = errorBanner.querySelector(".error-message");
          errorMessage.textContent = xhr.status + ': ' + xhr.responseText;
          errorBanner.style.display = "block";
        }
      });
    });
  });
  
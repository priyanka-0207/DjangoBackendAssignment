const options = ['New York', 'London', 'Paris', 'Tokyo', 'Sydney'];
const searchInput = document.querySelector('.search-input');
const autosuggestDropdown = document.querySelector('.autosuggest-dropdown');
  
searchInput.addEventListener('input', () => { const inputValue = searchInput.value.trim();
   const autosuggestOptions = getAutosuggestOptions(inputValue);
  
   generateAutosuggestDropdown(autosuggestOptions);
});
  
function getAutosuggestOptions(input) { return options.filter(option => option.toLowerCase().includes(input.toLowerCase()));
}
  
function generateAutosuggestDropdown(autosuggestOptions) { autosuggestDropdown.innerHTML = '';
  
   autosuggestOptions.forEach(option => {    const optionElement = document.createElement('div');
      optionElement.classList.add('autosuggest-item');
      optionElement.textContent = option;
      optionElement.addEventListener('click', () => {       searchInput.value = option;
         autosuggestDropdown.innerHTML = '';
      });
      autosuggestDropdown.appendChild(optionElement);
   });
}
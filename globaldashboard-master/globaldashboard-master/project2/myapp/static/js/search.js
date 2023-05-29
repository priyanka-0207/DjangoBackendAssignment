const searchInput = document.getElementById('search-input');
const suggestionsList = document.getElementById('suggestions-list');

searchInput.addEventListener('input', function () {
    const query = searchInput.value; 
    if (query.length > 0) {
        const suggestions = ['apple', 'banana', 'cherry', 'grape', 'orange'];
        showSuggestions(suggestions);
    } 
    else { 
        hideSuggestions(); 
    }
});
function showSuggestions(suggestions) {
    suggestionsList.innerHTML = '';
    for (let i = 0; i < suggestions.length; i++) {
        const suggestion = document.createElement('li');
        suggestion.textContent = suggestions[i];
        suggestion.addEventListener('click', function () {
            searchInput.value = suggestions[i];
            hideSuggestions();
        });
        suggestionsList.appendChild(suggestion);
    }
    suggestionsList.style.display = 'block';
}
function hideSuggestions() { suggestionsList.style.display = 'none'; }
const searchButton = document.getElementById('search-button');
searchButton.addEventListener('click', function () {
    const query = searchInput.value; if (query.length > 0) {
        console.log('Search query:', query);
    }
});

const searchBar = document.querySelector('.search-bar');
const list = document.querySelector('section ul');
let listItem;
let itemText;
let inputValue;


if (searchBar && list) {
    window.addEventListener('load', () => {
        searchBar.focus()
    })
    
    searchBar.addEventListener('change', function() {
        resetItems();
        inputValue = searchBar.value;
    
        for (let i = 0; i<list.childElementCount; i++) {
            listItem = list.children[i];
            itemText = listItem.textContent;
            
            removeItem(listItem, itemText);
        }
    })
}


function resetItems() {
    for (let i = 0; i<list.childElementCount; i++) {
        listItem = list.children[i];
        listItem.style.display = 'flex'
    } 
}

function removeItem(item, text) {
    if (text.toLowerCase().indexOf(searchBar.value.toLowerCase()) === -1) {
        item.style.display = 'None';
    } 
}

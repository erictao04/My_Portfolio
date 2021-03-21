const button = document.querySelector('#check')
const section = document.querySelectorAll('section');

button.addEventListener('click', function() {
    if (button.checked) {
        section.forEach(remove_content)
    } else {
        section.forEach(add_content)
    }
})

function remove_content(section) {
    section.style.display = 'none';
}

function add_content(section) {
    section.style.display = 'block';
}


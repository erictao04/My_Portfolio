const button = document.querySelector('#check')
const section = document.querySelectorAll('section');
let display = true;

button.addEventListener('click', function() {
    if (display) {
        section.forEach(remove_content)
    } else {
        section.forEach(add_content)
    }
})

function remove_content(section) {
    section.style.display = 'none';
    display = false;
}

function add_content(section) {
    section.style.display = 'block';
    display = true;
}


const button = document.querySelector('#check')
const section = document.querySelectorAll('section');
const side_checkbtns = document.querySelectorAll('.side-check')


button.addEventListener('click', function() {
    if (button.checked) {
        section.forEach(remove_content);
    } else {
        section.forEach(add_content);
        for (let i = 0; i < side_checkbtns.length; i++) {
            side_checkbtns[i].checked = false;
        }
    }
})

function remove_content(section) {
    section.style.display = 'none';
}

function add_content(section) {
    section.style.display = 'block';
}

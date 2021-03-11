const export_form = document.querySelectorAll('form');

let export_icon;
for (let i=0; i<export_form.length; i++) {
    export_form[i].addEventListener('submit', function() {
        export_icon = document.querySelector(`.export > li:nth-child(${i+1}) i:nth-child(2)`);
        let check;
        for (let j = 0; j<export_form.length; j++) {
            try {
                check = document.querySelector(`.export > li:nth-child(${j+1}) i:nth-child(3)`);
                check.style.display = 'none';
            }
            catch(err) {
                continue
            }
        };
        export_icon.style.display = 'block';
    });
}

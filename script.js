document.getElementById('form').addEventListener('submit',(event) => {
    event.preventDefault();
let name = document.getElementById('Name').value;
let age  = document.getElementById('age').value;
document.getElementById('namep').textContent = name;
document.getElementById('agep').textContent = age;
});
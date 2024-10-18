// Modal de saiba mais para pagina de sites
document.querySelectorAll('.saiba-mais-btn').forEach(button => {
    button.addEventListener('click', function() {
        const titulo = this.getAttribute('data-titulo');
        const img = this.getAttribute('data-img');
        const descricaoModal = this.getAttribute('data-descricao'); 

        document.getElementById('modal-title').innerText = titulo;
        document.getElementById('modal-image').src = img;
        document.getElementById('modal-description').innerText = descricaoModal;

        document.getElementById('modal').style.display = 'block';
    });
});

document.querySelector('.close').addEventListener('click', function() {
    document.getElementById('modal').style.display = 'none';
});

window.addEventListener('click', function(event) {
    if (event.target === document.getElementById('modal')) {
        document.getElementById('modal').style.display = 'none';
    }
});

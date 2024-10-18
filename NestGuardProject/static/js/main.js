// Função para mostrar a modal com o título e descrição fornecidos
function showTextModal(title, description) {
    document.getElementById('text-modal-title').innerText = title; // Atualiza o título
    document.getElementById('text-modal-description').innerText = description; // Atualiza a descrição
    document.getElementById('textModal').style.display = 'block'; // Exibe a modal
}

document.addEventListener('DOMContentLoaded', function() {
    // Lógica para modal de "Saiba mais" da página de sites
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

    // Fechar modal "Saiba mais" ao clicar no botão de fechar
    document.querySelector('.close').addEventListener('click', function() {
        document.getElementById('modal').style.display = 'none';
    });

    // Fechar modal "Saiba mais" ao clicar fora da modal
    window.addEventListener('click', function(event) {
        if (event.target === document.getElementById('modal')) {
            document.getElementById('modal').style.display = 'none';
        }
    });

    // Fechar modal de "Passos" ao clicar no botão de fechar (X)
    document.querySelector('.text-close').addEventListener('click', function() {
        console.log('Botão de fechar clicado');
        document.getElementById('textModal').style.display = 'none';
    });

    // Fechar modal de "Passos" ao clicar fora da modal
    window.addEventListener('click', function(event) {
        if (event.target === document.getElementById('textModal')) {
            document.getElementById('textModal').style.display = 'none';
        }
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const textModal = document.getElementById('textModal');
    const closeButton = document.querySelector('.text-close');

    closeButton.addEventListener('click', function () {
        console.log('Fechando modal de passos...');
        textModal.style.display = 'none';
    });

    window.addEventListener('click', function (event) {
        if (event.target === textModal) {
            console.log('Fechando modal ao clicar fora...');
            textModal.style.display = 'none';
        }
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const searchForm = document.getElementById('search-form');
    const resultDiv = document.getElementById('result');

    searchForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const code_barres = document.getElementById('code_barres').value;

        fetch('/search', {
            method: 'POST',
            body: new URLSearchParams({ code_barres }),
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                resultDiv.innerHTML = `<p>${data.message}</p>`;
            } else {
                resultDiv.innerHTML = `
                    <p>Description : ${data.description}</p>
                    <p>Quantité : ${data.quantite}</p>
                    <p>Emplacement : ${data.emplacement}</p>
                `;
            }
        })
        .catch(error => {
            console.error('Erreur :', error);
        });
    });
});

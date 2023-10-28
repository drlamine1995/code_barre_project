document.addEventListener("DOMContentLoaded", function() {

    // Intercepte la soumission du formulaire de recherche
    document.getElementById("searchForm").addEventListener("submit", function(event){
        event.preventDefault();  // Empêche le rechargement de la page

        let codeBarres = document.getElementById("code_barres").value;

        fetch("/search", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
            body: "code_barres=" + codeBarres
        })
        .then(response => response.json())
        .then(data => {
            let resultsDiv = document.getElementById("searchResults");
            if (data.message) {
                resultsDiv.innerHTML = data.message;
            } else {
                resultsDiv.innerHTML = "Code Barres: " + data.code_barres + "<br>" +
                                       "Numéro Machine: " + data.numero_machine + "<br>" +
                                       "Description: " + data.description + "<br>" +
                                       "Quantité: " + data.quantite + "<br>" +
                                       "Emplacement: " + data.emplacement + "<br>" +
                                       "Date d'Ajout: " + data.date_ajout;
            }
        });
    });

    // Vous pouvez ajouter d'autres fonctions ou scripts ici si nécessaire

});

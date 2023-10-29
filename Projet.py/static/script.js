
document.addEventListener("DOMContentLoaded", function() {
    const searchForm = document.getElementById("searchForm");
    const codeBarresInput = document.getElementById("code_barres");

    searchForm.addEventListener("submit", function(event) {
        event.preventDefault();
        const codeBarresValue = codeBarresInput.value.trim();
        if (!codeBarresValue) {
            event.preventDefault();
            alert("Veuillez entrer un code barre.");
    
        }
    });
});
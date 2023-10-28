
document.addEventListener("DOMContentLoaded", function() {
    const searchForm = document.getElementById("searchForm");
    const codeBarresInput = document.getElementById("code_barres");

    searchForm.addEventListener("submit", function(event) {
        event.preventDefault();
        const codeBarresValue = codeBarresInput.value.trim();
        if (codeBarresValue) {
            window.location.href = `/details_bouteille/${codeBarresValue}`;
        }
    });
});
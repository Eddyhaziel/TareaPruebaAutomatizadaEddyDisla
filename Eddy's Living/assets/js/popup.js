document.addEventListener('DOMContentLoaded', function() {
    const enlaces = document.querySelectorAll(".miClase");
    const popup = document.createElement('div');
    popup.id = "popup";
    popup.style.display = "none";
    popup.style.position = "fixed";
    popup.style.top = "50%";
    popup.style.left = "50%";
    popup.style.transform = "translate(-50%, -50%)";
    popup.style.zIndex = "1050";
    popup.style.maxWidth = "90%";
    popup.style.width = "400px"; 
    popup.style.height = "200px";
    popup.style.minHeight = "200px";

    popup.innerHTML = `
        <div class="alert alert-warning alert-dismissible fade show" role="alert" style="font-size: 1.2rem; padding: 30px 20px; display: flex; align-items: center; justify-content: center; text-align: center; position: relative; height: 100%;">
            <!-- Icono centrado verticalmente -->
            <i class="bi bi-exclamation-triangle-fill" style="font-size: 3rem; margin-right: 20px; position: absolute; left: 20px; top: 50%; transform: translateY(-50%);"></i>
            
            <!-- Mensaje centrado -->
            <strong style="flex-grow: 1;">Próximamente</strong>
            
            <!-- Botón de cerrar centrado verticalmente -->
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close" style="font-size: 1.5rem; position: absolute; right: 20px; top: 50%; transform: translateY(-50%);"></button>
        </div>
    `;
    document.body.appendChild(popup);

    const cerrarPopup = popup.querySelector(".btn-close");

    enlaces.forEach(function(enlace) {
        enlace.addEventListener("click", function(event) {
            event.preventDefault();
            popup.style.display = "block"; 
        });
    });

    cerrarPopup.addEventListener("click", function() {
        popup.style.display = "none"; 
    });
});

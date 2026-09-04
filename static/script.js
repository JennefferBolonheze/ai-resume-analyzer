document.addEventListener("DOMContentLoaded", () => {
    const resumeFile = document.getElementById("resume_file");
    const uploadArea = document.querySelector(".upload-area");
    const form = document.querySelector(".analyzer-form");
    const analyzeButton = document.querySelector(".analyze-button");
    const results = document.querySelector(".results");

    // =========================
    // MOSTRAR NOME DO ARQUIVO
    // =========================

    if (resumeFile && uploadArea) {
        resumeFile.addEventListener("change", () => {
            const existingFileName = uploadArea.querySelector(".file-name");

            if (existingFileName) {
                existingFileName.remove();
            }

            if (resumeFile.files.length > 0) {
                const file = resumeFile.files[0];

                const fileName = document.createElement("p");

                fileName.classList.add("file-name");

                fileName.textContent = `✓ ${file.name}`;

                uploadArea.appendChild(fileName);
            }
        });
    }


    // =========================
    // BOTÃO "ANALISANDO..."
    // =========================

    if (form && analyzeButton) {
        form.addEventListener("submit", () => {
            analyzeButton.disabled = true;

            analyzeButton.textContent = "⏳ Analisando...";
        });
    }


    // =========================
    // SCROLL PARA RESULTADOS
    // =========================

    if (results) {
        setTimeout(() => {
            results.scrollIntoView({
                behavior: "smooth",
                block: "start"
            });
        }, 250);
    }
});
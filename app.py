from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from pypdf import PdfReader

from analyzer import analyze_resume


app = Flask(__name__)


# Limite máximo do currículo: 5 MB
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024


ALLOWED_EXTENSIONS = {
    "pdf",
    "txt"
}


def allowed_file(filename):
    """
    Verifica se o arquivo possui
    uma extensão permitida.
    """

    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower()
        in ALLOWED_EXTENSIONS
    )


def extract_text_from_pdf(file):
    """
    Extrai texto de um currículo em PDF.
    """

    reader = PdfReader(file)

    text_parts = []

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text_parts.append(page_text)

    return "\n".join(text_parts).strip()


def extract_text_from_txt(file):
    """
    Extrai texto de um arquivo TXT.
    """

    file_content = file.read()

    try:
        text = file_content.decode("utf-8-sig")

    except UnicodeDecodeError:
        text = file_content.decode(
            "latin-1",
            errors="ignore"
        )

    return text.strip()


@app.route("/", methods=["GET", "POST"])
def index():

    result = None

    resume_text = ""
    job_text = ""

    resume_filename = ""

    error = None


    if request.method == "POST":

        # Descrição da vaga
        job_text = request.form.get(
            "job_text",
            ""
        ).strip()


        # Currículo digitado/colado
        resume_text_manual = request.form.get(
            "resume_text",
            ""
        ).strip()


        # Currículo enviado por arquivo
        resume_file = request.files.get(
            "resume_file"
        )


        # Se existir um arquivo enviado,
        # ele terá prioridade sobre o texto manual
        if resume_file and resume_file.filename:

            resume_filename = secure_filename(
                resume_file.filename
            )


            if not allowed_file(resume_filename):

                error = (
                    "Formato de arquivo não permitido. "
                    "Envie um currículo em PDF ou TXT."
                )


            else:

                extension = resume_filename.rsplit(
                    ".",
                    1
                )[1].lower()


                try:

                    if extension == "pdf":

                        resume_text = extract_text_from_pdf(
                            resume_file
                        )


                    elif extension == "txt":

                        resume_text = extract_text_from_txt(
                            resume_file
                        )


                except Exception as e:

                    print(
                        "Erro ao ler currículo:",
                        e
                    )

                    error = (
                        "Não foi possível ler o arquivo. "
                        "Tente outro currículo ou cole "
                        "o texto manualmente."
                    )


        else:

            resume_text = resume_text_manual


        # Validações
        if not error:

            if not resume_text:

                error = (
                    "Adicione seu currículo em PDF/TXT "
                    "ou cole o texto do currículo."
                )


            elif not job_text:

                error = (
                    "Cole a descrição da vaga "
                    "que deseja analisar."
                )


            else:

                result = analyze_resume(
                    resume_text,
                    job_text
                )


    return render_template(
        "index.html",
        result=result,
        resume_text=resume_text,
        job_text=job_text,
        resume_filename=resume_filename,
        error=error
    )


@app.errorhandler(413)
def file_too_large(error):

    return render_template(
        "index.html",
        result=None,
        resume_text="",
        job_text="",
        resume_filename="",
        error=(
            "O arquivo enviado é muito grande. "
            "O tamanho máximo permitido é 5 MB."
        )
    ), 413


if __name__ == "__main__":

    app.run(
        debug=True
    )
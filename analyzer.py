from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_match(resume_text, job_text):
    """
    Calcula a similaridade entre o currículo
    e a descrição da vaga usando TF-IDF
    e similaridade de cosseno.
    """

    if not resume_text.strip():
        return 0.0

    if not job_text.strip():
        return 0.0


    documents = [
        resume_text,
        job_text
    ]


    vectorizer = TfidfVectorizer(
        lowercase=True
    )


    try:

        tfidf_matrix = vectorizer.fit_transform(
            documents
        )


        similarity = cosine_similarity(
            tfidf_matrix[0:1],
            tfidf_matrix[1:2]
        )[0][0]


    except ValueError:

        return 0.0


    match_percentage = round(
        similarity * 100,
        2
    )


    return match_percentage


def extract_skills(text):
    """
    Identifica competências técnicas
    presentes no texto.
    """

    skills = [
        "python",
        "sql",
        "java",
        "javascript",
        "html",
        "css",
        "flask",
        "django",
        "react",
        "git",
        "github",
        "power bi",
        "excel",
        "pandas",
        "numpy",
        "machine learning",
        "artificial intelligence",
        "inteligência artificial",
        "data analysis",
        "análise de dados",
        "power automate",
        "sharepoint",
        "linux",
        "cloud",
        "aws",
        "azure"
    ]


    text_lower = text.lower()


    found_skills = []


    for skill in skills:

        if skill in text_lower:

            found_skills.append(
                skill
            )


    return found_skills


def analyze_resume(
    resume_text,
    job_text
):
    """
    Executa a análise completa
    entre currículo e vaga.
    """

    match_score = calculate_match(
        resume_text,
        job_text
    )


    resume_skills = extract_skills(
        resume_text
    )


    job_skills = extract_skills(
        job_text
    )


    matched_skills = [
        skill
        for skill in job_skills
        if skill in resume_skills
    ]


    missing_skills = [
        skill
        for skill in job_skills
        if skill not in resume_skills
    ]


    return {

        "match_score":
            match_score,

        "resume_skills":
            resume_skills,

        "job_skills":
            job_skills,

        "matched_skills":
            matched_skills,

        "missing_skills":
            missing_skills

    }


if __name__ == "__main__":

    resume_example = """
    Estudante de Sistemas de Informação
    com conhecimentos em Python,
    SQL, Power BI, Excel,
    Power Automate e SharePoint.
    """


    job_example = """
    Procuramos pessoa com conhecimentos
    em Python, SQL, Power BI,
    análise de dados e Git.
    """


    result = analyze_resume(
        resume_example,
        job_example
    )


    print(result)
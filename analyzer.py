import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


SKILL_ALIASES = {
    "Python": ["python"],
    "SQL": ["sql"],
    "Java": ["java"],
    "JavaScript": ["javascript", "js"],
    "HTML": ["html"],
    "CSS": ["css"],
    "Flask": ["flask"],
    "Django": ["django"],
    "React": ["react", "react.js", "reactjs"],
    "Git": ["git"],
    "GitHub": ["github"],
    "Power BI": ["power bi", "powerbi"],
    "Excel": ["excel"],
    "Pandas": ["pandas"],
    "NumPy": ["numpy"],
    "Machine Learning": [
        "machine learning",
        "aprendizado de máquina",
    ],
    "Inteligência Artificial": [
        "artificial intelligence",
        "inteligência artificial",
        "inteligencia artificial",
        "ai",
    ],
    "Análise de Dados": [
        "data analysis",
        "análise de dados",
        "analise de dados",
        "data analytics",
    ],
    "Power Automate": [
        "power automate",
    ],
    "Power Apps": [
        "power apps",
        "powerapps",
    ],
    "SharePoint": [
        "sharepoint",
    ],
    "Linux": [
        "linux",
    ],
    "Cloud": [
        "cloud",
        "computação em nuvem",
        "computacao em nuvem",
    ],
    "AWS": [
        "aws",
        "amazon web services",
    ],
    "Azure": [
        "azure",
        "microsoft azure",
    ],
    "Docker": [
        "docker",
    ],
    "APIs": [
        "api",
        "apis",
        "rest api",
        "restful",
    ],
    "Banco de Dados": [
        "database",
        "banco de dados",
        "databases",
    ],
}


def calculate_match(resume_text, job_text):
    """
    Calcula a similaridade textual entre o currículo
    e a descrição da vaga usando TF-IDF
    e similaridade de cosseno.
    """

    if not resume_text.strip():
        return 0.0

    if not job_text.strip():
        return 0.0

    documents = [
        resume_text,
        job_text,
    ]

    vectorizer = TfidfVectorizer(
        lowercase=True,
        stop_words=None,
    )

    try:
        tfidf_matrix = vectorizer.fit_transform(documents)

        similarity = cosine_similarity(
            tfidf_matrix[0:1],
            tfidf_matrix[1:2],
        )[0][0]

    except ValueError:
        return 0.0

    return round(similarity * 100, 2)


def contains_skill(text, aliases):
    """
    Verifica se uma competência aparece no texto.
    Usa regex para evitar falsos positivos.
    """

    text_lower = text.lower()

    for alias in aliases:
        pattern = r"(?<!\w)" + re.escape(alias.lower()) + r"(?!\w)"

        if re.search(pattern, text_lower):
            return True

    return False


def extract_skills(text):
    """
    Identifica competências técnicas presentes no texto.
    """

    found_skills = []

    for skill_name, aliases in SKILL_ALIASES.items():
        if contains_skill(text, aliases):
            found_skills.append(skill_name)

    return found_skills


def calculate_skill_coverage(matched_skills, job_skills):
    """
    Calcula a porcentagem de competências da vaga
    encontradas no currículo.
    """

    if not job_skills:
        return 0.0

    coverage = (
        len(matched_skills)
        / len(job_skills)
    ) * 100

    return round(coverage, 2)


def generate_recommendations(
    resume_skills,
    job_skills,
    matched_skills,
    missing_skills,
    match_score,
):
    """
    Gera recomendações personalizadas com base
    nas competências encontradas e ausentes.
    """

    recommendations = []

    if missing_skills:
        missing_text = ", ".join(missing_skills[:5])

        recommendations.append(
            f"A vaga menciona competências que não foram "
            f"identificadas no currículo: {missing_text}. "
            f"Se você tiver experiência com alguma delas, "
            f"considere mencioná-la de forma clara."
        )

    if matched_skills:
        matched_text = ", ".join(matched_skills[:5])

        recommendations.append(
            f"Destaque melhor no currículo as competências "
            f"que já combinam com a vaga, como: {matched_text}."
        )

    if len(resume_skills) < 4:
        recommendations.append(
            "Considere deixar a seção de habilidades técnicas "
            "mais clara e objetiva, destacando ferramentas, "
            "linguagens e tecnologias que você realmente utiliza."
        )

    if match_score < 40:
        recommendations.append(
            "O currículo possui baixa similaridade textual com "
            "a descrição da vaga. Vale adaptar o resumo profissional "
            "e a descrição dos projetos usando termos relevantes "
            "da vaga, desde que representem experiências reais."
        )

    elif match_score < 70:
        recommendations.append(
            "Existe compatibilidade parcial com a vaga. "
            "Tente evidenciar projetos, experiências e resultados "
            "relacionados às principais exigências da oportunidade."
        )

    else:
        recommendations.append(
            "A compatibilidade textual é boa. "
            "Revise o currículo para garantir que suas experiências "
            "mais relevantes estejam destacadas logo nas primeiras seções."
        )

    recommendations.append(
        "Sempre que possível, descreva resultados concretos, "
        "como melhorias de processo, redução de tempo, "
        "automação de tarefas ou indicadores desenvolvidos."
    )

    return recommendations


def generate_strengths(matched_skills):
    """
    Cria uma lista de pontos fortes identificados
    em relação à vaga.
    """

    strengths = []

    if matched_skills:
        strengths.append(
            "O currículo possui competências técnicas "
            "também mencionadas na vaga."
        )

        strengths.append(
            "Competências compatíveis: "
            + ", ".join(matched_skills)
            + "."
        )
    else:
        strengths.append(
            "Nenhuma competência técnica específica da vaga "
            "foi identificada diretamente no currículo."
        )

    return strengths


def generate_assessment(
    final_score,
    missing_skills,
):
    """
    Gera uma avaliação geral da compatibilidade.
    """

    if final_score >= 80:
        assessment = (
            "Excelente compatibilidade com a vaga. "
            "O currículo apresenta forte alinhamento "
            "com os requisitos identificados."
        )

    elif final_score >= 65:
        assessment = (
            "Boa compatibilidade com a vaga. "
            "O currículo atende a vários requisitos, "
            "mas ainda existem pontos que podem ser destacados."
        )

    elif final_score >= 45:
        assessment = (
            "Compatibilidade moderada. "
            "Existem pontos alinhados, mas o currículo "
            "pode ser adaptado para evidenciar melhor "
            "as competências exigidas."
        )

    else:
        assessment = (
            "Compatibilidade baixa. "
            "Vale revisar o currículo e verificar quais "
            "requisitos da vaga podem ser demonstrados "
            "com experiências ou projetos reais."
        )

    if missing_skills:
        assessment += (
            f" Foram identificadas {len(missing_skills)} "
            f"competência(s) da vaga que não aparecem no currículo."
        )

    return assessment


def analyze_resume(
    resume_text,
    job_text,
):
    """
    Executa a análise completa entre currículo e vaga.
    """

    text_similarity = calculate_match(
        resume_text,
        job_text,
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

    skill_coverage = calculate_skill_coverage(
        matched_skills,
        job_skills,
    )

    if job_skills:
        final_score = round(
            (text_similarity * 0.40)
            + (skill_coverage * 0.60),
            2,
        )
    else:
        final_score = text_similarity

    strengths = generate_strengths(
        matched_skills
    )

    recommendations = generate_recommendations(
        resume_skills,
        job_skills,
        matched_skills,
        missing_skills,
        final_score,
    )

    assessment = generate_assessment(
        final_score,
        missing_skills,
    )

    return {
        "match_score": final_score,
        "text_similarity": text_similarity,
        "skill_coverage": skill_coverage,
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "strengths": strengths,
        "recommendations": recommendations,
        "assessment": assessment,
    }


if __name__ == "__main__":
    resume_example = """
    Estudante de Sistemas de Informação
    com conhecimentos em Python,
    SQL, Power BI, Excel,
    Power Automate e SharePoint.
    Desenvolvimento de projetos utilizando
    Flask, Git e análise de dados.
    """

    job_example = """
    Procuramos pessoa com conhecimentos
    em Python, SQL, Power BI,
    análise de dados, Git,
    AWS e Docker.
    """

    result = analyze_resume(
        resume_example,
        job_example,
    )

    print(result)
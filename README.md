# 🤖 AI Resume Analyzer

Aplicação web desenvolvida em Python para analisar a compatibilidade entre um currículo e a descrição de uma vaga.

O sistema utiliza técnicas de **Processamento de Linguagem Natural (NLP)** para comparar os textos, identificar competências técnicas e apresentar um percentual de compatibilidade entre o perfil do candidato e os requisitos encontrados na vaga.

---

## ✨ Funcionalidades

- 📄 Upload de currículo em PDF ou TXT
- ✍️ Opção de colar o currículo manualmente
- 💼 Análise da descrição de uma vaga
- 📊 Cálculo de Match Score
- ✅ Identificação de skills compatíveis
- 🎯 Identificação de skills que estão faltando
- 🧠 Detecção automática de competências técnicas
- 🔎 Comparação textual utilizando TF-IDF
- 📐 Cálculo de similaridade utilizando Cosine Similarity
- 📱 Interface responsiva

---

## 🧠 Como funciona

O usuário pode anexar seu currículo em **PDF ou TXT** ou inserir o conteúdo manualmente.

Em seguida, adiciona a descrição da vaga que deseja analisar.

O sistema:

1. Extrai o texto do currículo.
2. Processa o currículo e a descrição da vaga.
3. Identifica competências técnicas nos dois textos.
4. Compara as skills encontradas.
5. Identifica competências presentes e ausentes.
6. Calcula a similaridade textual utilizando **TF-IDF e Cosine Similarity**.
7. Gera um Match Score combinando a análise textual com a compatibilidade de skills.

---

## 📊 Match Score

O Match Score utiliza duas informações principais:

- **Similaridade textual:** compara o conteúdo geral do currículo com a descrição da vaga.
- **Compatibilidade de skills:** verifica quantas competências solicitadas pela vaga também aparecem no currículo.

Na versão atual, o cálculo combina:

```text
40% → Similaridade textual
60% → Compatibilidade de skills
```

Essa abordagem permite considerar tanto o contexto dos textos quanto as tecnologias e competências técnicas identificadas.

---

## 🛠️ Tecnologias utilizadas

### Back-end

- Python
- Flask
- Scikit-learn
- PyPDF

### NLP / Machine Learning

- TF-IDF Vectorization
- Cosine Similarity
- Extração de skills baseada em termos e aliases

### Front-end

- HTML5
- CSS3
- JavaScript
- Jinja2

---

## 📁 Estrutura do projeto

```text
ai-resume-analyzer/
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── app.py
├── analyzer.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/JennefferBolonheze/ai-resume-analyzer.git
```

Entre na pasta:

```bash
cd ai-resume-analyzer
```

### 2. Crie um ambiente virtual

```bash
python -m venv .venv
```

No Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Instale as dependências

```bash
python -m pip install -r requirements.txt
```

### 4. Execute a aplicação

```bash
python app.py
```

Depois acesse no navegador:

```text
http://127.0.0.1:5000
```

---

## 📄 Formatos de currículo

Atualmente o sistema aceita:

- `.pdf`
- `.txt`

O tamanho máximo permitido para upload é de **5 MB**.

> PDFs baseados apenas em imagens podem não ter o texto extraído corretamente, pois a aplicação não utiliza OCR nesta versão.

---

## 🔐 Privacidade

Os currículos enviados são utilizados apenas para realizar a análise durante a requisição.

A aplicação atual não possui banco de dados para armazenar os currículos enviados.

---

## ⚠️ Limitações

Esta versão utiliza NLP clássico e uma base definida de competências técnicas.

Por isso, o sistema pode não reconhecer uma tecnologia ou competência que ainda não esteja cadastrada na base de skills.

O Match Score deve ser interpretado como uma estimativa de compatibilidade textual e técnica, e não como uma decisão real de recrutamento.

---

## 🔮 Melhorias futuras

Algumas possibilidades de evolução do projeto:

- 🧠 Utilização de embeddings para comparação semântica
- 🤖 Integração com modelos de linguagem (LLMs)
- 💡 Sugestões personalizadas para melhorar o currículo
- 📑 Suporte a arquivos DOCX
- 🌎 Melhor suporte para currículos em diferentes idiomas
- 🔍 Expansão automática da base de competências
- 📈 Análise mais detalhada dos requisitos da vaga
- ☁️ Deploy da aplicação
- 🎨 Melhorias na experiência do usuário

---

## 🎯 Objetivo do projeto

O projeto foi desenvolvido com o objetivo de aplicar conceitos de **Python, desenvolvimento web, Machine Learning e Processamento de Linguagem Natural** em uma aplicação prática.

Além da comparação textual, o projeto explora extração de informações, processamento de documentos e análise de competências profissionais.

---

## 👩‍💻 Autora

**Jenneffer Souza Bolonheze**

Estudante de Sistemas de Informação com interesse em:

`Inteligência Artificial` • `Automação` • `Dados` • `Tecnologia`

---

⭐ Se você gostou do projeto, considere deixar uma estrela no repositório!
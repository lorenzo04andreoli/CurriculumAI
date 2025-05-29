## 📄 Analisador de Currículos com IA

Este é um projeto de análise de currículos que utiliza a **Groq API** com o modelo **Llama 3.1 8B-Instant** para resumir e pontuar currículos com base na descrição de uma vaga específica. O projeto é desenvolvido em **Python**, com o **Streamlit** como front-end para a interface do usuário, além de integração com a **Google Drive API** para automação no download de currículos.

---

## ✅ Funcionalidades

* **Upload de Currículos em Lote**: Carrega vários currículos de uma vez para análise.
* **Análise de Currículos**: Avalia currículos com base em diferentes seções, atribuindo uma pontuação conforme a relevância para a vaga.
* **Comparação de Currículos**: Compara currículos lado a lado para uma avaliação mais detalhada.
* **Análise Crítica Descritiva**: Geração de uma análise crítica e descritiva sobre o currículo em relação à vaga.
* **Autenticação com Google Drive**: Automatiza o download de currículos diretamente do Google Drive.

---

## 🛠️ Tecnologias Utilizadas

* **Python**: Linguagem de programação principal utilizada no projeto.
* **Streamlit**: Framework utilizado para criar a interface web de maneira rápida e interativa.
* **Groq API (Llama 3.1 8B-Instant)**: API utilizada para resumir os currículos e gerar a pontuação.
* **Google Drive API**: Utilizada para autenticação e automação no download dos currículos.
* **pip**: Ferramenta utilizada para gerenciamento de dependências.

---

## 🚀 Instalação e Execução

### ✅ Pré-requisitos

* Python **3.10** ou superior
* **pip** instalado

### ✅ Passos para instalação

Clone este repositório para o seu ambiente local:

```bash
git clone https://github.com/lorenzo04andreoli/CurriculumAI.git
cd CurriculumAI
```

Instale as dependências do projeto utilizando o **pip**:

```bash
pip install 
```

Execute o projeto com o **Streamlit**:

```bash
streamlit run analyze/app.py
```

Acesse o projeto no seu navegador através do endereço:

```
http://localhost:8502
```

---

## 🌟 Uso

Após subir o projeto, você poderá:

* Cadastrar novas vagas através da interface.
* Subir currículos em lote para análise.
* Visualizar a análise de cada currículo por vaga, com a possibilidade de comparar currículos.
* Gerar análises críticas descritivas sobre os currículos em relação às vagas.

---

## 📊 Documentação do Sistema de Pontuação

O sistema de pontuação foi projetado para avaliar currículos com base em uma vaga específica. As seções avaliadas incluem:

* **Experiência** (Peso: 30%)
* **Habilidades Técnicas** (Peso: 25%)
* **Educação** (Peso: 10%)
* **Idiomas** (Peso: 10%)
* **Pontos Fortes** (Peso: 15%)
* **Pontos Fracos** (Desconto de até 10%)

Cada seção recebe uma pontuação de **0 a 10**, com justificativas para as notas atribuídas. A pontuação final é uma **média ponderada** das avaliações, refletindo a adequação do candidato à vaga.

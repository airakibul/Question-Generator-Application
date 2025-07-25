# Question-Generator-Application

A powerful tool built with LangChain, FastAPI, and modern NLP techniques that allows users to upload PDF files and automatically generate relevant questions and answers based on the document content. Users can view the PDF and download the generated Q&A pairs as a CSV file.

---

## 🚀 Features

- 📁 PDF Upload – Easily upload any PDF file
- 📄 PDF Viewer – View the uploaded PDF within the app
- ❓ Question Generator – Generate relevant questions from the PDF content using advanced language models  
- ✅ Answer Generator – Automatically generate accurate answers
- 💾 CSV Export – Download questions and answers as a structured .csv file
- 🧠 Powered by LangChain, OpenRouter, and transformers  

---

## 🛠️ Technology Stack

- **Framework**: LangChain 
- **Frontend**: FastAPI 
- **Embeddings**: HuggingFace (`sentence-transformers/all-MiniLM-L6-v2`)  
- **Vector Database**: Faiss  
- **PDF Processing**: PyPDF2  
- **Language Models**: ChatOpenAI( `mistralai/mistral-7b-instruct`)  
- **Text Processing**: OpenAI (`gpt-3.5-turbo`)  

---

## 📋 Prerequisites

- Python 3.10+  
- Openrouter API key  

---

## ⚙️ Installation

1. Create an environment

```bash
git clone https://github.com/airakibul/Question-Generator-Application.git

```

2. Create an environment

```bash
conda create -n interview python=3.10 -y

conda activate interview

```

3. Create a .env file and add your API key from OpenRouter

```bash

OPENROUTER_API_KEY = "paste your api key"

```

4. install requirements

```bash

pip install -r requirements.txt

```

---

## Usage

1. Start the application

```bash

python app.py

```

2. open a browser and go to http://localhost:8080/
3. Upload a PDF file
4. Click the "Generate Q&A" Button
5. Click the "Download" icon to Download the .csv file

---

## Project Structure

```text
├── data
├── Research
│   └── expriement.ipynb
├── src
│   ├── __init__.py
│   ├── helper.py
│   └── prompt.py
├── templates
│   └── index.html
├── static
├── app.py
├── setup.py
└── requirements.txt
```
---

## Features in Detail

- 📁 PDF Upload & Viewing: Upload and preview PDF files directly in the app.

- 🧠 Q&A Generation: Generates relevant questions and answers from PDF content using LLMs via OpenRouter.

- ✂️ Text Chunking: Splits text into manageable chunks for accurate processing.

- 🧾 CSV Export: Download generated Q&A pairs as a CSV file.

- 💬 Simple Interface: User-friendly FastAPI UI for easy interaction.

- 📝 Modular Code: Clean, organized structure for easy maintenance and scaling.

- 🔗 LangChain Integration: Manages LLM workflows and document handling.

- 🔐 Secure Config: Uses .env for managing API keys and settings securely.

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## Screenshots

1. Frontend

![App Screenshot](https://github.com/airakibul/Question-Generator-Application/blob/main/screenshots/Screenshot1.png)

2. CSV file

![App Screenshot](https://github.com/airakibul/Question-Generator-Application/blob/main/screenshots/Screenshot2.png)
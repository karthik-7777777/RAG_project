# 📚 RAG Project — PDF Question Answering System

A modular **Retrieval-Augmented Generation (RAG)** system built with Python that allows users to ask questions about PDF documents. The system loads PDF files, splits them into meaningful chunks, generates vector embeddings, stores them in a FAISS vector database, retrieves relevant information, and uses an LLM to generate answers based on the retrieved context.

## 🚀 Features

* 📄 Load and process PDF documents
* ✂️ Split documents into smaller chunks
* 🧠 Generate semantic embeddings
* 🔎 Perform similarity-based document retrieval
* 🗃️ Store and search embeddings using FAISS
* 🤖 Generate context-aware answers using an LLM
* 🧩 Modular project structure
* 🔐 Store API keys securely using environment variables

## 🏗️ RAG Pipeline

```text
                PDF Documents
                     │
                     ▼
              Document Loader
                     │
                     ▼
              Text Chunking
                     │
                     ▼
              Embeddings Model
                     │
                     ▼
               FAISS Vector DB
                     │
                     ▼
                User Query
                     │
                     ▼
              Query Embedding
                     │
                     ▼
             Similarity Search
                     │
                     ▼
            Relevant Documents
                     │
                     ▼
                   LLM
                     │
                     ▼
              Generated Answer
```

## 📂 Project Structure

```text
RAG/
│
├── app.py
│
├── Data_loader.py
├── Split_documents.py
├── Embeddings_manager.py
├── VectorStore_manager.py
├── Rag_retriever.py
│
├── pdfs/
│   └── PDF documents
│
├── faiss_db/
│   └── FAISS vector store
│
├── .env
├── .gitignore
└── README.md
```

## 🧩 Modules

### `Data_loader.py`

Responsible for loading PDF documents and converting them into documents that can be processed by the RAG pipeline.

### `Split_documents.py`

Splits the loaded documents into smaller chunks to improve retrieval accuracy and provide manageable context to the language model.

### `Embeddings_manager.py`

Handles the conversion of text chunks and user queries into numerical vector representations using an embedding model.

### `VectorStore_manager.py`

Manages the FAISS vector database, including storing embeddings and performing similarity searches.

### `Rag_retriever.py`

Retrieves the most relevant document chunks based on the user's query.

### `app.py`

Acts as the main application entry point and connects the different components of the RAG pipeline.

## 🛠️ Tech Stack

* **Python**
* **LangChain**
* **FAISS**
* **Embedding Models**
* **LLM**
* **PyMuPDF**
* **python-dotenv**

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/karthik-7777777/RAG_project.git
cd RAG_project
```

### 2. Create a virtual environment

```bash
python -m venv .RAG311env
```

Activate it on Windows:

```powershell
.RAG311env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_api_key_here
```

> Never commit your `.env` file or API keys to GitHub.

## 📄 Add Documents

Place the PDF files you want to query inside:

```text
pdfs/
```

For example:

```text
pdfs/
├── Attention.pdf
├── LLMs.pdf
├── LoRa.pdf
└── RAG.pdf
```

## ▶️ Run the Application

Run:

```bash
python app.py
```

Then enter your questions and the system will retrieve relevant information from the uploaded PDF documents before generating an answer.

## 🔍 How Retrieval Works

When a user asks a question:

1. The question is converted into an embedding.
2. FAISS searches for vectors that are most similar to the query.
3. The most relevant document chunks are retrieved.
4. Retrieved chunks are provided as context to the LLM.
5. The LLM generates an answer using the retrieved context.

This helps the model answer questions using information from the provided documents rather than relying only on its pretrained knowledge.

## 📌 Example

**User:**

```text
What is self-attention in Transformers?
```

**RAG System:**

```text
Query
  ↓
Embedding
  ↓
FAISS Similarity Search
  ↓
Relevant chunks from Attention.pdf
  ↓
LLM
  ↓
Generated Answer
```

## 🎯 Purpose of the Project

This project was built to understand and implement the core concepts of **Retrieval-Augmented Generation**, including:

* Document ingestion
* Text chunking
* Embeddings
* Vector databases
* Similarity search
* Retrieval
* Context construction
* LLM-based answer generation
* Modular RAG architecture

  
## 👨‍💻 Author

**Karthik K**

B.Tech — Artificial Intelligence & Machine Learning

---

⭐ If you find this project useful, consider giving it a star!

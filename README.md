# Multi-Document RAG Assistant

A full-stack **Multi-Document Retrieval-Augmented Generation (RAG) Assistant** that allows users to upload multiple PDF, DOCX, and TXT documents and ask questions about their content.

The system retrieves relevant document sections using semantic search and generates answers using a local Large Language Model (LLM).

## 🚀 Features

* Upload multiple documents
* Supports PDF, DOCX, and TXT files
* Automatic document text extraction
* Text chunking with overlap
* Semantic embeddings using Sentence Transformers
* Vector storage and similarity search using ChromaDB
* Question answering using Ollama
* Source document and page references
* React-based web interface
* Flask REST API backend
* Local AI processing

## 🏗️ Architecture

```text
User
 │
 ▼
React Frontend
 │
 │ HTTP REST API
 ▼
Flask Backend
 │
 ├── Document Processor
 │       ├── PDF
 │       ├── DOCX
 │       └── TXT
 │
 ├── Text Chunking
 │
 ├── Embedding Service
 │       └── Sentence Transformers
 │
 ├── ChromaDB
 │       └── Vector Search
 │
 └── Ollama
         └── Llama 3.2
```

## 📂 Project Structure

```text
multi-document-rag/
│
├── frontend/
│   └── React/
│       ├── src/
│       │   ├── App.jsx
│       │   ├── App.css
│       │   └── main.jsx
│       ├── index.html
│       ├── package.json
│       └── package-lock.json
│
├── backend/
│   ├── routes/
│   │   ├── upload.py
│   │   └── chat.py
│   │
│   ├── services/
│   │   ├── document_processor.py
│   │   ├── embedding.py
│   │   ├── retriever.py
│   │   └── llm.py
│   │
│   ├── rag/
│   │   ├── chunking.py
│   │   └── vector_store.py
│   │
│   ├── app.py
│   └── requirements.txt
│
└── .gitignore
```

## 🛠️ Technologies Used

### Frontend

* React
* Vite
* JavaScript
* HTML
* CSS

### Backend

* Python
* Flask
* Flask-CORS
* REST API

### RAG Pipeline

* PyPDF
* python-docx
* Sentence Transformers
* ChromaDB
* Ollama
* Llama 3.2

## 🔄 How It Works

### 1. Upload Documents

The user uploads PDF, DOCX, or TXT documents through the React interface.

### 2. Document Processing

The Flask backend extracts text from the uploaded documents.

### 3. Chunking

The extracted text is divided into smaller overlapping chunks.

### 4. Embeddings

Each chunk is converted into a vector representation using:

```text
all-MiniLM-L6-v2
```

### 5. Vector Storage

The embeddings and document metadata are stored in ChromaDB.

### 6. Question

The user enters a question through the React interface.

### 7. Retrieval

The question is converted into an embedding and compared with the stored document vectors.

The most relevant chunks are retrieved.

### 8. Answer Generation

The retrieved context is sent to the local Ollama LLM.

The LLM generates an answer based only on the retrieved document context.

### 9. Sources

The application returns the source document and page number along with the answer.

## ⚙️ Installation

### Backend

Navigate to the backend directory:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Ollama

Install Ollama:

https://ollama.com/

Download the required model:

```bash
ollama pull llama3.2
```

Start Ollama if required:

```bash
ollama run llama3.2
```

### Start Flask Backend

From the backend directory:

```bash
python app.py
```

The backend will run at:

```text
http://127.0.0.1:5000
```

### Frontend

Open another terminal:

```bash
cd frontend/React
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

Open:

```text
http://localhost:5173
```

## 🔌 API Endpoints

### Health Check

```http
GET /api/health
```

Example response:

```json
{
  "status": "ok"
}
```

### Upload Documents

```http
POST /api/upload
```

Accepts multiple:

* PDF
* DOCX
* TXT

### Ask a Question

```http
POST /api/chat
```

Request:

```json
{
  "question": "What is the main topic of the document?"
}
```

Response:

```json
{
  "answer": "Generated answer...",
  "sources": [
    {
      "document": "example.pdf",
      "page": 1
    }
  ]
}
```

## 🔐 Data and Privacy

The RAG pipeline is designed to process documents locally.

Uploaded documents are processed by the local Flask backend, while the LLM is accessed through the local Ollama service.

## 🚧 Current Limitations

* Scanned/image-only PDFs require OCR and are not currently supported.
* DOCX documents currently use a simplified page representation.
* Duplicate document detection is not implemented.
* Authentication is not currently implemented.
* Conversation history is not currently persisted.

## 🔮 Future Improvements

* OCR support for scanned PDFs
* Streaming LLM responses
* Conversation memory
* Document deletion
* Duplicate document detection
* User authentication
* Improved chunking strategies
* Reranking for better retrieval
* Chat history
* Docker deployment
* Cloud deployment
* Document preview
* Better source citation and highlighting

## 👨‍💻 Author

**Darshan Vijaykumar Babannavar**

Electronics & Communication Engineering

Angadi Institute of Technology and Management, Belagavi

GitHub:

https://github.com/DarshanBabannavar

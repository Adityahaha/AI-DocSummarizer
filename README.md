# Make It Asaan — Dynamic RAG

A Streamlit application that lets you upload multiple research papers (PDFs), builds a persistent, dynamic Retrieval-Augmented Generation (RAG) index using Chroma and Hugging Face embeddings, and interactively queries across all uploaded documents using Groq’s LLaMA3 model.

---

## 🚀 Features

* **Dynamic Ingestion**: Upload new PDFs at any time; documents are immediately chunked, embedded, and appended to the existing index.
* **Persistent Vector Store**: Uses [Chroma](https://github.com/chroma-core/chroma) as a disk-persisted vector database; resumes state on app restart.
* **High-Quality Embeddings**: Leverages Hugging Face’s `all-MiniLM-L6-v2` model for text embeddings.
* **Powerful LLM**: Groq’s LLaMA3-70B-8192 via `langchain-groq` for concise, context-rich answers.
* **Streamlit UI**: Simple, responsive frontend for uploading files and asking questions.
* **Reset Capability**: One-click button to clear the entire index and start fresh.

---

## 📋 Prerequisites

* Python 3.8+
* pip or conda
* Streamlit account (optional for deployment)
* Groq API key (store in Streamlit secrets)

---

## 🔧 Installation

1. **Clone this repository**

   ```bash
   git clone https://github.com/yourusername/make-it-asaan
   cd make-it-asaan
   ```

2. **Create & activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate      # macOS/Linux
   venv\Scripts\activate       # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Groq API key**

   * Add the following to your `~/.streamlit/secrets.toml`:

     ```toml
     [default]
     GROQ_API_KEY = "<YOUR_GROQ_API_KEY>"
     ```

---

## ⚙️ Usage

1. **Run the Streamlit app**

   ```bash
   streamlit run app.py
   ```

2. **Upload PDFs**

   * Click **Browse** and select one or more research papers.
   * The app will chunk, embed, and persist them to `./chroma_db`.

3. **Ask Questions**

   * Enter any free-text query in the input box.
   * Click **Run Query** to retrieve contextually relevant answers from all uploaded documents.

4. **Reset Index**

   * Open the sidebar and click **🔄 Reset Index** to clear all stored embeddings.

---

## 🛠️ Code Structure

```text
├── app.py              # Main Streamlit application code
├── requirements.txt    # Python dependencies
├── chroma_db/          # Persisted vector store directory (auto-created)
└── README.md           # This file
```

---

## 🌍 Deployment

* **Streamlit Cloud**: Connect your GitHub repo and deploy in minutes.
* **Docker**:

  1. Build: `docker build -t make-it-asaan .`
  2. Run:  `docker run -p 8501:8501 -e GROQ_API_KEY=<key> make-it-asaan`

---

## 📝 License

MIT License © 2025 Your Name

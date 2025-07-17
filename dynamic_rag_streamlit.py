import streamlit as st
import tempfile, os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq  # Groq's LLM

# --- Configuration ---
os.environ["GROQ_API_KEY"] = "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"  # store key in Streamlit secrets
st.set_page_config(page_title="AI DocSummarizer", layout="centered")

# Initialize persistent vector store
persist_dir = "./chroma_db"
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = Chroma(persist_directory=persist_dir, embedding_function=embeddings)

# UI
st.markdown("# 📘 AI DocSummarizer")
st.markdown("_Upload PDFs & ask questions across all uploads in real&nbsp;time._")

# 1️⃣ Upload or Add Document
uploaded_file = st.file_uploader("Upload research paper (PDF)", type=["pdf"])
if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        path = tmp.name
    loader = PyPDFLoader(path)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)
    vector_store.add_documents(chunks)
    vector_store.persist()
    st.success(f"Added {len(chunks)} chunks to the index.")

# 2️⃣ Interactive Query
query = st.text_input("Ask a question about your documents:")
if st.button("Run Query") and query:
    # Re-load the persisted index dynamically
    vectordb = Chroma(persist_directory=persist_dir, embedding_function=embeddings)
    retriever = vectordb.as_retriever(search_kwargs={"k": 5})
    llm = ChatGroq(model="llama3-70b-8192", temperature=0.3)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type="stuff")
    with st.spinner("Generating answer..."):
        answer = qa_chain.run(query)
    st.write(answer)

# 3️⃣ Optional: Clear Index
if st.sidebar.button("🔄 Reset Index"):
    vector_store.delete_collection()
    st.sidebar.info("Index cleared. You can upload new PDFs.")

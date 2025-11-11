# 🧠 AWS Bedrock PDF Chat App

This project is an interactive Question-Answering (QA) application built with LangChain, AWS Bedrock, and Streamlit.
It allows users to upload PDF documents, processes them into chunks, embeds them using Bedrock Embeddings, and answers user queries using Amazon Bedrock LLMs — all powered by modern LangChain (v1.1+) components.

# 🚀 Features

📄 Upload one or more PDFs and automatically extract text

✂️ Split documents into chunks using RecursiveCharacterTextSplitter

🔍 Create a FAISS vector store for similarity search

🧩 Use Bedrock Embeddings for semantic understanding

💬 Query your documents using Bedrock LLMs

⚡ Built with LangChain 1.1+ — no deprecated modules like RetrievalQA

🖥️ Streamlit frontend for easy use

# 🏗️ Tech Stack
Component	Technology
Framework	Streamlit
LLM	AWS Bedrock
Embeddings	BedrockEmbeddings
Vector Store	FAISS
Orchestration	LangChain 1.1
Document Processing	PyPDFDirectoryLoader, RecursiveCharacterTextSplitter

🧠 How It Works

1. PDFs are loaded and text is extracted using PyPDFDirectoryLoader.

2. Text is split into chunks using RecursiveCharacterTextSplitter.

3. Each chunk is embedded using BedrockEmbeddings.

4. The embeddings are stored in a FAISS vector database.

5. When a user asks a question:

  Similar chunks are retrieved via FAISS.

  The retrieved context is passed to the Bedrock LLM.

  <img width="1919" height="1035" alt="image" src="https://github.com/user-attachments/assets/376d8681-3a60-4df1-aab9-ab00b4274c8a" />

# LLama output
<img width="1907" height="1041" alt="image" src="https://github.com/user-attachments/assets/43c7def1-f173-470f-bf85-a6f40d8d6d8c" />

# Mistral Output
<img width="1910" height="1036" alt="Screenshot 2025-11-11 143224" src="https://github.com/user-attachments/assets/9f78fb03-815f-4e62-81b4-2b1845c68b8b" />


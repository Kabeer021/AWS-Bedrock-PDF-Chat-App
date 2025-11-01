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

<img width="1024" height="535" alt="image" src="https://github.com/user-attachments/assets/c8f51685-55c8-44a4-88ec-56499b9d2c51" />


# LLama 

<img width="953" height="1036" alt="Screenshot 2025-11-01 164412" src="https://github.com/user-attachments/assets/f433fb5a-6222-4723-a2f0-956373dc8af4" />



<img width="961" height="1030" alt="Screenshot 2025-11-01 164521" src="https://github.com/user-attachments/assets/b5706138-0ac6-47cd-84bd-8fe59a8f5d02" />

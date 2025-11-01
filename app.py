import json
import os
import sys
import boto3
import streamlit as st

# AWS Bedrock Embeddings
from langchain_aws import BedrockEmbeddings

# AWS Bedrock LLMs
from langchain_community.llms import Bedrock

## Data Ingestion
import numpy as np


from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.document_loaders import PyPDFDirectoryLoader


# Vector Embedding and Vector store

from langchain_community.vectorstores import FAISS

## LLM models
from langchain_core.prompts import PromptTemplate

from langchain import create_retrieval_chain


## Bedrock clients
bedrock = boto3.client(service_name = "bedrock-runtime")

bedrock_embeddings = BedrockEmbeddings(model_id = 'amazon.titan-embed-text-v2:0' , client= bedrock)

## data ingestion

def data_ingestion():
            loader = PyPDFDirectoryLoader("data")
            documents = loader.load()

            text_splitter = RecursiveCharacterTextSplitter(chunk_size = 10000,
            chunk_overlap = 1000)

            docs = text_splitter.split_documents(documents)
            return docs

## Vector Embedding and vector store

def get_vector_store(docs):
        vectorstore_faiss = FAISS.from_documents(
                docs,
                bedrock_embeddings
        )

        vectorstore_faiss.save_local("faiss_index")

def get_llama3_llm():
        
        llm = Bedrock(model_id = "meta.llama3-8b-instruct-v1:0",
                      client = bedrock,
                      model_kwargs = {'max_gen_len':512})
        return llm

def get_claude_llm():
        
        llm = Bedrock(model_id = "anthropic.claude-3-7-sonnet-20250219-v1:0",
                      client = bedrock,
                      model_kwargs = {'maxtokens':512})
        return llm


prompt_template = """
Human: Use the following pieces of context to provide a concise answer to the question at the end but use at least summarize with 250 words with detailed explanations. If you don't know the answer, just say that you don't know, don't try to make up an answer.
<context>
{context}
</context>

Question: {question}

Assistant :"""

PROMPT = PromptTemplate(
        template = prompt_template,
        imput_variables = ["context" , "question"]
)

def get_response_llm(llm, vectorstore_faiss, query):
        
        qa = create_retrieval_chain.from_chain_type(
                llm = llm,
                chain_type = "stuff",
                retriever = vectorstore_faiss.as_retriever(
                        search_type ="similarity" , search_kwargs = {"k":3} # top 3 prompts
                ),
                return_source_documents = True,
                chain_type_kwargs = {"prompt":PROMPT}
        )

        answer = qa({"query" : query})
        return answer['result']



## APP body 

def main():
        
            st.set_page_config("Chat PDF")
            st.header("Chat with PDF using AWS Bedrock")

            user_question = st.text_input("Ask a Question from PDF files")

            with st.sidebar:
                st.title("Update or create vector store")

                if st.button("Vectors Update"):
                        with st.spinner("Processing..."):
                                docs = data_ingestion()
                                get_vector_store(docs)
                                st.success("Done")
         
            if st.button("LLama Output"):
                        with st.spinner("Processing..."):
                                faiss_index = FAISS.load_local("faiss_index", bedrock_embeddings)
                                llm = get_llama3_llm()
                        
                        st.write(get_response_llm(llm, faiss_index, user_question))
                        st.success("Done")

            if st.button("Claude Output"):
                        with st.spinner("Processing..."):
                                faiss_index = FAISS.load_local("faiss_index", bedrock_embeddings)
                                llm = get_claude_llm()
                        
                        st.write(get_response_llm(llm, faiss_index, user_question))
                        st.success("Done")

if __name__ == "__main__":
        main()

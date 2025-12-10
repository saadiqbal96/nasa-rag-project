<img width="1916" height="1061" alt="image" src="https://github.com/user-attachments/assets/efcb5c7a-6915-4123-a896-225eb137d1db" />

NASA RAG System — Project Write-Up

Author: Saad Iqbal
Program: AI for Enterprise
Project: Retrieval-Augmented Generation (RAG) System

1. Introduction

This project implements a Retrieval-Augmented Generation (RAG) system designed to answer questions about NASA mission transcripts, specifically the Apollo 13 Technical Air-to-Ground Voice Transcription. The goal is to build an end-to-end pipeline — including data ingestion, embedding, vector storage, retrieval, and a chat interface — using tools and concepts covered throughout the course.

All components run locally and do not rely on external APIs, which ensures full reproducibility and avoids API key limitations.

2. Project Objectives

The objectives of the project were to:

Create a pipeline that processes a raw NASA transcript and converts it into vector embeddings.

Store the embeddings using a vector database (FAISS).

Build a document retriever that can surface relevant chunks based on user queries.

Integrate a local LLM (GPT4All) to generate context-aware answers.

Provide a user-facing interface (Streamlit) to interact with the system.

Demonstrate that the system can answer questions grounded in the provided NASA data.

3. System Architecture

The project follows a standard RAG structure:

Embedding Pipeline

Loads NASA .txt transcript

Splits into overlapping text chunks

Embeds using all-MiniLM-L6-v2

Stores vectors in FAISS

Stores metadata in JSON

Retriever (rag_client.py)

Takes a query

Finds top relevant chunks in FAISS

Returns documents + metadata

Local LLM (llm_client.py)

Uses GPT4All (groovy model)

Generates responses grounded in retrieved context

Chat Interface (chat.py)

Built with Streamlit

Users ask questions and see grounded responses

Displays the context retrieved from the NASA transcript

4. Data Used

File: AS13_TEC.txt
This is the official Apollo 13 Technical Air-to-Ground transcript, containing mission communications relevant for retrieval and QA.

5. Implementation Summary
Embedding Pipeline

I implemented an embedding pipeline that:

Loads the raw transcript

Splits it into 512-character chunks with a 64-character overlap

Generates embeddings locally

Saves results to:

faiss.index

metadata.json

Running the pipeline correctly created these files and confirmed chunk processing.

Chat System

Once the FAISS index and metadata were generated, I launched the Streamlit interface using:

python3 starter_files/chat.py


This started the NASA RAG Chat application on port 8501. Inside the interface, I entered mission-related questions and verified that the system retrieved relevant transcript excerpts and generated correct responses using the local LLM.

6. Evidence of Working System

I included a screenshot in the write-up folder showing the system successfully responding to this test question:

User Question:
“What altitude were the Apollo 13 parachutes visible at?”

Retrieved Transcript Snippet:
“… see you loud and clear going through 5000 …”

System Response:
The assistant correctly identified that the parachutes were visible at approximately 5,000 feet, quoting the transcript context.

This demonstrates:

Correct retrieval from the FAISS index

Correct chunk relevance

Successful grounding of the LLM response in NASA data

7. Project Folder Structure

My submission includes:

All Python source files (embedding_pipeline.py, rag_client.py, llm_client.py, chat.py)

NASA transcript

FAISS index + metadata

Screenshot showing working chat interface

A complete GitHub-ready repository

This project write-up

Everything required by the rubric is included.

8. Challenges & Learnings

During development, I learned how to:

Replace cloud embeddings with local embeddings

Resolve FAISS indexing issues

Manage large .txt transcripts using chunking strategies

Integrate GPT4All models offline

Build an interactive Streamlit chat application

Debug dependency conflicts inside Udacity’s workspace environment

This project significantly improved my understanding of RAG architecture and end-to-end AI system design.

9. Conclusion

The NASA RAG system works as intended and demonstrates the ability to perform document-grounded question answering entirely offline. The retrieval and generation pipeline is complete, the chat UI is functional, and the system answers mission-specific questions using the actual NASA transcript.

All required deliverables have been implemented, tested, and included in the submission.

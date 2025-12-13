🚀 NASA RAG Chat Project
Retrieval-Augmented Generation with ChromaDB, OpenAI & RAGAS

Author: Saad Iqbal
Repository: nasa-rag-project
Project Type: End-to-End RAG System with Evaluation and Streamlit UI

🌌 Project Overview

This project implements a fully-functional Retrieval-Augmented Generation (RAG) system for NASA mission documents (Apollo 11, Apollo 13, Challenger).

The system follows the complete RAG lifecycle:

Document ingestion → chunking → OpenAI embeddings → ChromaDB storage → retrieval → grounded LLM responses → batch evaluation

All design decisions are explicitly aligned with the Udacity project rubric and prior reviewer feedback.

✅ Rubric-Aligned Features (At a Glance)

✔ ChromaDB persistent vector store

✔ OpenAI embedding model (text-embedding-3-small)

✔ Configurable chunk size & overlap (CLI flags)

✔ Document update modes: skip / update / replace

✔ Metadata-aware retrieval (mission, source, category)

✔ System-prompt-based LLM grounding

✔ Conversation history management

✔ Batch evaluation with RAGAS-style metrics

✔ Streamlit chat interface

🧠 Core Architecture

Text Files
   ↓
Configurable Chunking
   ↓
OpenAI Embeddings
   ↓
ChromaDB (Persistent Collection)
   ↓
Metadata-Filtered Retrieval
   ↓
Grounded LLM Responses
   ↓
Batch Evaluation (RAGAS-style)

📁 Repository Structure
.

├── chat_.py                   # Streamlit chat UI

├── embedding_pipeline_.py     # ChromaDB + OpenAI embedding pipeline

├── RAG_CLIENT_.py             # Retrieval + context construction

├── LLM_CLIENT_.py             # System-prompted LLM client

├── ragas_evaluator_.py        # Evaluation metrics (relevancy, faithfulness)

├── ragas_batch_eval.py        # Batch evaluation runner

├── evaluation_dataset.jsonl   # Evaluation test set (≥5 questions)

├── ragas_report.json          # Generated evaluation report

├── chroma.sqlite3             # Persistent ChromaDB store

├── AS13_TEC_.txt              # NASA Apollo 13 technical transcript

├── README.md

└── gitignore.txt

🧩 Key Implementation Details

🔹 1. Configurable Chunking (Rubric Critical)

Chunk size and overlap are runtime-configurable

No hard-coded constants

--chunk-size 500
--chunk-overlap 100


Validation ensures overlap is always smaller than chunk size.

🔹 2. OpenAI Embeddings + ChromaDB

Uses OpenAI embeddings (text-embedding-3-small)

Stored in a persistent ChromaDB collection

Supports:

--chroma-dir

--collection-name

--stats-only mode

🔹 3. Update Modes for Existing Documents

Embedding pipeline supports:

skip → ignore existing documents

update → update existing chunks

replace → delete and re-ingest

--update-mode skip|update|replace

🔹 4. Retrieval & Context Construction

Retriever provides:

Top-K configurable retrieval

Optional mission filtering

Score-sorted results

Deduplication

Clean, single context block

Example context header:

[Apollo 13 • AS13_TEC • Technical • Score: 0.412]

🔹 5. LLM Grounding & System Prompt

The LLM client uses a strict system prompt:

Positions the model as a NASA mission expert

Forces answers to rely only on retrieved context

Requires explicit source citations

States uncertainty when context is insufficient

Conversation history is maintained and trimmed for multi-turn chat.

🔹 6. Evaluation & Batch Metrics

Includes:

evaluation_dataset.jsonl (≥5 Apollo-13 questions)

Batch evaluation script

Metrics include:

Relevancy

Faithfulness

Outputs:

ragas_report.json

💬 Example Questions

Try asking:

“What caused the Apollo 13 oxygen tank explosion?”

“At what altitude were the Apollo 13 parachutes first visible?”

“What did the crew report immediately after the explosion?”

“What communication difficulties occurred during re-entry?”

🖥️ Running the Project
1️⃣ Build / Update the Vector Store

python embedding_pipeline_.py \

  --data-path . \

  --openai-key $OPENAI_API_KEY \
  
  --chroma-dir ./chroma_db_openai \
  
  --collection-name nasa_space_missions_text \
  
  --chunk-size 500 \
  
  --chunk-overlap 100 \
  
  --update-mode skip

2️⃣ Launch the Chat UI
streamlit run chat_.py

3️⃣ Run Batch Evaluation
python ragas_batch_eval.py

🧪 Why This Meets the Rubric

This submission directly addresses prior reviewer feedback by:

Using ChromaDB instead of FAISS

Using OpenAI embeddings instead of local MiniLM

Making chunking configurable at runtime

Adding update modes

Adding a system prompt + conversation memory

Producing batch evaluation output

Aligning README claims with actual code behavior

👤 Author

Saad Iqbal
nasa-rag-project

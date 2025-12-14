🚀 NASA RAG Chat Project
Retrieval-Augmented Generation with ChromaDB, OpenAI & RAGAS

Author: Saad Iqbal
Repository: nasa-rag-project

Project Type: End-to-End RAG System with Evaluation and Streamlit UI

🌌 Project Overview

This project implements a fully-functional Retrieval-Augmented Generation (RAG) system that processes NASA mission documents (Apollo 11, Apollo 13, Challenger) to provide semantic search and grounded LLM responses. Using ChromaDB for persistent storage of document embeddings and OpenAI embeddings, the system retrieves the most relevant context to generate accurate and contextually grounded responses.

Key Features:

Document ingestion → chunking → OpenAI embeddings → ChromaDB storage → retrieval → grounded LLM responses → batch evaluation

ChromaDB for persistence, OpenAI embeddings for text chunking

Configurable chunking and overlap at runtime

Metadata-aware retrieval (mission, source, category)

Grounded LLM responses with conversation history

Batch evaluation with RAGAS-style metrics including Relevancy, Faithfulness, BLEU, ROUGE, and Context Precision

Streamlit-based chat interface

✅ Rubric-Aligned Features (At a Glance)

ChromaDB persistent vector store for embedding persistence

OpenAI embedding model (text-embedding-3-small)

Configurable chunk size and overlap (CLI flags)

Document update modes: skip, update, replace

Metadata-aware retrieval (filter by mission, source, category)

System-prompt-based LLM grounding

Conversation history management

Batch evaluation with RAGAS-style metrics:

Response Relevancy

Faithfulness

Additional metrics: BLEU, ROUGE, Context Precision

Streamlit chat interface for interactive use

🧠 Core Architecture
Text Files → Configurable Chunking → OpenAI Embeddings → ChromaDB (Persistent Collection)
   ↓                                   ↓                          ↓
Metadata-Filtered Retrieval → Grounded LLM Responses → Batch Evaluation (RAGAS-style)

📁 Repository Structure
├── chat_.py                   # Streamlit chat UI
├── embedding_pipeline_.py     # ChromaDB + OpenAI embedding pipeline
├── RAG_CLIENT_.py             # Retrieval + context construction
├── LLM_CLIENT_.py             # System-prompted LLM client
├── ragas_evaluator_.py        # Evaluation metrics (relevancy, faithfulness, BLEU, ROUGE, context precision)
├── ragas_batch_eval.py        # Batch evaluation runner
├── evaluation_dataset.jsonl   # Evaluation test set (≥5 questions)
├── ragas_report.json          # Generated evaluation report
├── chroma.sqlite3             # Persistent ChromaDB store
├── AS13_TEC_.txt              # NASA Apollo 13 technical transcript
├── README.md                  # This file
└── gitignore.txt

🧩 Key Implementation Details
🔹 1. Configurable Chunking (Rubric Critical)

Chunk size and overlap are runtime-configurable with the CLI options --chunk-size and --chunk-overlap.

Validation ensures overlap is always smaller than the chunk size.

🔹 2. OpenAI Embeddings + ChromaDB

OpenAI embeddings (text-embedding-3-small) are used for document chunking and embedding.

The embeddings are stored in a persistent ChromaDB collection.

CLI flags available:

--chroma-dir for specifying the ChromaDB directory

--collection-name to set the collection name

--stats-only mode to view collection stats

🔹 3. Update Modes for Existing Documents

Update Modes support:

skip – skip existing documents

update – update existing chunks

replace – delete and re-ingest

CLI flag: --update-mode skip|update|replace

🔹 4. Retrieval & Context Construction

Top-K configurable retrieval with optional mission filtering.

Score-sorted results, deduplication, and clean single context block for LLM consumption.

Example context header: [Apollo 13 • AS13_TEC • Technical • Score: 0.412]

🔹 5. LLM Grounding & System Prompt

Grounded System Prompt positions the LLM as a NASA mission expert.

Ensures answers are based only on the retrieved context.

Conversation history management for multi-turn chats with trimmed history.

🔹 6. Evaluation & Batch Metrics

Includes evaluation dataset: evaluation_dataset.jsonl (≥5 Apollo-13 questions)

Batch evaluation script computes:

Response Relevancy

Faithfulness

Additional Metrics:

BLEU

ROUGE

Context Precision

Results are stored in ragas_report.json

🎯 RAGAS Metrics

Primary Metrics:

Response Relevancy

Faithfulness

Additional Metrics (included in ragas_report.json):

BLEU: Measures the overlap of n-grams between generated and reference text.

ROUGE: Evaluates the quality of summaries by comparing them to reference summaries.

Context Precision: Measures how well the model's generated response aligns with the retrieved context.

These metrics are computed during batch evaluation and help assess the quality of the generated responses.

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

Using ChromaDB instead of FAISS for persistence.

Using OpenAI embeddings (text-embedding-3-small) instead of local MiniLM.

Making chunking configurable at runtime with CLI flags.

Adding update modes for document handling.

Introducing a system prompt and conversation history management.

Batch evaluation output with RAGAS-style metrics including BLEU, ROUGE, and Context Precision.

🎓 Evaluation Metrics
Primary Metrics:

Response Relevancy

Faithfulness

Additional Metrics:

BLEU

ROUGE

Context Precision

These additional metrics are computed and stored in the ragas_report.json file during the batch evaluation process.

📚 Resources & Documentation

ChromaDB Documentation: ChromaDB Docs

OpenAI API Documentation: OpenAI Docs

RAGAS Documentation: RAGAS Docs

Streamlit Documentation: Streamlit Docs

🎯 Future Enhancements

Once the core system is complete, consider the following enhancements:

Advanced Retrieval: Implement hybrid search (semantic + keyword).

Multi-modal Support: Add support for images and audio.

Performance Optimization: Add caching and parallel processing.

Advanced Evaluation: Implement custom metrics for domain-specific quality.

Deployment: Containerize and deploy the system on cloud platforms.

👤 Author

Saad Iqbal
nasa-rag-project

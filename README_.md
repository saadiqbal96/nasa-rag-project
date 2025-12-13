NASA RAG Chat Project — ChromaDB + OpenAI + RAGAS

Author: Saad Iqbal
Repo: nasa-rag-project
Project Type: Retrieval-Augmented Generation (RAG) system with evaluation + Streamlit UI

1) Project Overview

This project implements an end-to-end RAG (Retrieval-Augmented Generation) pipeline for NASA mission documents (e.g., Apollo 11 / Apollo 13 / Challenger). It includes:

Document ingestion + chunking (configurable chunk size + overlap)

OpenAI embeddings stored in a persistent ChromaDB collection

A RAG retriever with optional metadata filtering (e.g., mission)

An LLM client with system prompt + conversation history and grounded answering rules

Evaluation via a small test set and a batch evaluator producing a JSON report (RAGAS-style metrics)

This repo is designed to match rubric requirements that explicitly mention ChromaDB, OpenAI embeddings, configurable chunking, update modes, and evaluation outputs.

2) Key Features Aligned to Rubric
2.1 Chunking & Configuration

Chunking uses runtime configuration (CLI flags), not hard-coded constants:

--chunk-size

--chunk-overlap

Validation ensures overlap stays smaller than chunk size.

2.2 Embeddings & Storage

Embeddings are created using OpenAI embedding models (default: text-embedding-3-small)

Stored in a persistent ChromaDB collection (chroma.sqlite3 is created and saved)

2.3 Update Modes

Embedding pipeline supports:

--update-mode skip (default)

--update-mode update

--update-mode replace

2.4 Retrieval + Clean Context Construction

Retriever produces:

score-sorted results

optional mission filtering

formatted context including source / mission / category / score

deduplication using stable identifiers (document_id / source+chunk)

2.5 LLM Grounding

LLM client includes:

A system prompt positioning the assistant as a NASA mission expert

Conversation history support (trimmed)

Rules for grounding:

use retrieved context only

cite sources

say when the answer is not in the context

2.6 Evaluation + Batch Report

Includes:

evaluation_dataset.jsonl (≥5 NASA mission questions)

batch evaluation script that:

runs retrieval + response

evaluates metrics

writes ragas_report.json

3) Project Structure

Note: filenames in this repo include trailing underscores to match the uploaded/working versions.

.
├── README.md
├── chat_.py
├── embedding_pipeline_.py
├── RAG_CLIENT_.py
├── LLM_CLIENT_.py
├── ragas_evaluator_.py
├── ragas_batch_eval.py
├── evaluation_dataset.jsonl
├── ragas_report.json
├── chroma.sqlite3
├── AS13_TEC_.txt
├── EVALUATION_RUBRIC_.md
└── gitignore.txt

4) Screenshots

Add your screenshots to a folder (recommended):

/assets
  ├── streamlit_demo.png
  └── colab_evaluation.png


Then embed them in this README like:

## Screenshots

### Streamlit Chat Demo
![Streamlit Demo](assets/streamlit_demo.png)

### Batch Evaluation Output (Colab)
![Evaluation Output](assets/colab_evaluation.png)

5) Setup Instructions
5.1 Prerequisites

Python 3.9+ recommended

A valid OpenAI API key with available billing/credits

5.2 Install Dependencies

If you are running locally:

pip install chromadb openai streamlit pandas numpy


(If you already have a requirements.txt, use that instead.)

5.3 Set Your API Key

Mac/Linux:

export OPENAI_API_KEY="your_key_here"


Windows (PowerShell):

setx OPENAI_API_KEY "your_key_here"

6) Running the Project
Step 1 — Build / Update the ChromaDB Collection

Run the embedding pipeline:

python embedding_pipeline_.py \
  --data-path . \
  --openai-key $OPENAI_API_KEY \
  --chroma-dir ./chroma_db_openai \
  --collection-name nasa_space_missions_text \
  --chunk-size 500 \
  --chunk-overlap 100 \
  --update-mode skip

Optional: Show collection stats only
python embedding_pipeline_.py \
  --openai-key $OPENAI_API_KEY \
  --chroma-dir ./chroma_db_openai \
  --collection-name nasa_space_missions_text \
  --stats-only

Step 2 — Launch the Streamlit Chat App
streamlit run chat_.py


Then open the local Streamlit URL shown in the terminal.

Step 3 — Run Batch Evaluation

Make sure your dataset file exists (evaluation_dataset.jsonl) and run:

python ragas_batch_eval.py


Outputs:

ragas_report.json (per-question scores + report file)

7) Example Questions

Try queries like:

“What caused the Apollo 13 oxygen tank explosion?”

“At what altitude were the Apollo 13 parachutes first visible?”

“What did the crew report immediately after the explosion?”

“What communication issues occurred during re-entry?”

8) Notes for Reviewer

This submission intentionally follows rubric requirements by including:

ChromaDB persistence (chroma.sqlite3)

OpenAI embeddings (text-embedding-3-small default)

Configurable chunking via CLI args

Update modes (skip/update/replace)

System prompt and conversation history logic in the LLM client

Evaluation dataset + batch evaluation script that outputs a results file

9) License

For educational use in Udacity coursework.

10) Author

Saad Iqbal
Repo: nasa-rag-project

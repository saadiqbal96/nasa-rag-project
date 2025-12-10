
import os, json
from pathlib import Path
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

CHUNK_SIZE = 800
CHUNK_OVERLAP = 200

def chunk_text(text):
    chunks = []
    start = 0
    while start < len(text):
        end = start + CHUNK_SIZE
        chunks.append(text[start:end])
        start += CHUNK_SIZE - CHUNK_OVERLAP
    return chunks

def detect_mission(name):
    name = name.lower()
    if "13" in name:
        return "Apollo 13"
    if "11" in name:
        return "Apollo 11"
    return "Unknown"

def run_embedding_pipeline(data_dir="data", out_dir="embeddings"):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    texts = []
    metadata = []

    for file in Path(data_dir).glob("*.txt"):
        raw = file.read_text()
        chunks = chunk_text(raw)
        mission = detect_mission(file.name)
        for c in chunks:
            texts.append(c)
            metadata.append({"text": c, "source": file.name, "mission": mission})

    emb = model.encode(texts).astype("float32")
    index = faiss.IndexFlatIP(emb.shape[1])
    index.add(emb)

    faiss.write_index(index, f"{out_dir}/faiss.index")
    json.dump(metadata, open(f"{out_dir}/metadata.json", "w"))
    print("Embedding pipeline complete.")

if __name__ == "__main__":
    run_embedding_pipeline()


import streamlit as st
import rag_client
import llm_client

st.title("🚀 NASA RAG Chat — Local FAISS System")
query = st.text_input("Ask a question about the NASA logs:")
k = st.slider("Documents to retrieve", 1, 10, 3)

if query:
    docs, metas = rag_client.retrieve(query, k=k)
    ctx = rag_client.format_context(docs, metas)
    rsp = llm_client.generate_response(query, ctx)
    st.write(rsp)

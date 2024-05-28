import streamlit as st
import os
import pickle
from document_indexer import chunk_document, HuggingFaceEmbeddings, FAISS

def streamlit_interface():
    st.title("Document Indexer")

    doc_path = st.text_input("Path of the documents:", value="documents")
    chunk_size = st.number_input("Size of the chunk:", value=64, step=1)
    chunk_step = st.number_input("Step size of the chunk:", value=64, step=1)
    output_path = st.text_input("Path of the output:", value="knowledge")

    if st.button("Index Documents"):
        try:
            file_count, texts, metadata_list, chunk_id_to_index = chunk_document(
                doc_path=doc_path,
                chunk_size=chunk_size,
                chunk_step=chunk_step,
            )
            embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
            vectorstore = FAISS.from_texts(
                texts=texts,
                metadatas=metadata_list,
                embedding=embeddings,
            )
            vectorstore.save_local(folder_path=output_path)
            with open(os.path.join(output_path, "chunk_id_to_index.pkl"), "wb") as f:
                pickle.dump(chunk_id_to_index, f)
            st.success(f"Successfully indexed {file_count} documents. Saved vectorstore to {output_path}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    streamlit_interface()

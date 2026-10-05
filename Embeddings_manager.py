from sentence_transformers import SentenceTransformer
import numpy as np
from langchain_core.documents import Document

class EmbeddingManager:
    def __init__(self,model_name="all-MiniLM-L6-v2", persistence_dir="C:/Users/kr233/OneDrive/Desktop/RAG/faiss_db"):
        self.model_name=model_name
        self.model=None
        self._load_embedding_model()

    def _load_embedding_model(self):
        try:
            self.model=SentenceTransformer(self.model_name)
            print(f"STEP-3 : Loaded embedding model: {self.model_name}, embedding dimensions : {self.model.get_embedding_dimension()}")
        except Exception as e:
            print(f"Error loading embedding model: {e}")
    def generate_embeddings(self,text)-> np.array:

        if self.model is None:
            print(f"Embedding model {self.model_name} is not loaded") 
        if isinstance(text[0],Document):
            text=[doc.page_content for doc in text]
        embeddings=self.model.encode(text, show_progress_bar=True)
        print(f"STEP-4 : Embeddings are created") 
        return embeddings
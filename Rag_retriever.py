from Embeddings_manager import EmbeddingManager
from VectorStore_manager import vectorStoreManager
from typing import List, Dict, Any, Tuple
import numpy as np


class RagRetriever:
    def __init__(self,vectorstore:vectorStoreManager,EmbeddingManager:EmbeddingManager):
        self.VectorStore=vectorstore
        self.EmbeddingManager=EmbeddingManager
    def retrive(self,query: str,top_k: int=10,threshold: float=0.0)-> List[Dict[str,any]]:
        query_embedding=self.EmbeddingManager.generate_embeddings([query])
        try:
            distances, indices = self.VectorStore.index.search(
                np.asarray(query_embedding, dtype=np.float32),
                top_k
            )
            retrived_docs=[]
            for distance, index in zip(distances[0], indices[0]):
                if index == -1:
                    continue

                retrived_docs.append({
                    "id": self.VectorStore.ids[index],
                    "document": self.VectorStore.documents[index],
                    "metadata": self.VectorStore.metadatas[index],
                    "score": float(distance)
                })
            return retrived_docs
        except Exception as e:
            print(f"Error retrieving documents: {e}")
            return []
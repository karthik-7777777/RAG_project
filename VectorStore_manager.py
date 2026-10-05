from langchain_core.documents import Document
from typing import List, Dict, Any, Tuple
import numpy as np
import faiss
import uuid
import os

class vectorStoreManager:
    def __init__(self,collection_name="pdf_collection",persistence_dir="C:/Users/kr233/OneDrive/Desktop/RAG/faiss_db"):
        self.collection_name=collection_name
        self.persistence_dir=persistence_dir
        self.index=None
        self.documents=[]
        self.metadatas=[]
        self.ids=[]
        self._initialize_faiss()

    def _initialize_faiss(self):
        try:
            os.makedirs(self.persistence_dir, exist_ok=True)
            print(f"Initialized FAISS vector store: {self.collection_name}")

        except Exception as e:
            print(f"Error initializing FAISS vector store: {e}")

    def add_documents(self,documents:List[Document],Embeddings:np.ndarray):
        try:
            if len(documents)!=len(Embeddings):
                raise ValueError("The number of documents are not equal to number of Embeddings")

            ids=[]
            metadatas=[]
            page_contents=[]
            embeddings_list=[]

            for i,(doc,embedding) in enumerate(zip(documents,Embeddings)):
                doc_id=str(uuid.uuid4())
                ids.append(doc_id)

                metadata=dict(doc.metadata)
                metadata["doc_index"]=i
                metadata["content_length"]=len(doc.page_content)

                metadatas.append(metadata)
                page_contents.append(doc.page_content)
                embeddings_list.append(embedding.tolist())

            try:
                embeddings_array=np.asarray(embeddings_list,dtype=np.float32)

                if self.index is None:
                    dimension=embeddings_array.shape[1]
                    self.index=faiss.IndexFlatL2(dimension)

                self.index.add(embeddings_array)

                self.ids.extend(ids)
                self.documents.extend(page_contents)
                self.metadatas.extend(metadatas)
                faiss.write_index(self.index, os.path.join(self.persistence_dir, f"{self.collection_name}.index"))
                print(f"STEP-5 : Added {len(documents)} documents to FAISS vector store: {self.collection_name}")
                # return self.ids,self.documents,self.metadatas,self.index

            except Exception as e:
                print(f"Error adding documents to FAISS vector store: {e}")

        except Exception as e:
            print(f"Error in add_documents method: {e}")


# "----------------------------------------------------FOR CHROMA DB------------------------------------------------"

# # class vectorStoreManager:
# #     def __init__(self,collection_name="pdf_collection",persistence_dir="C:/Users/kr233/OneDrive/Desktop/RAG/chroma_db"):
# #         self.collection_name=collection_name
# #         self.persistence_dir=persistence_dir
# #         self.client=None
# #         self.collection=None
# #         self._initialize_chroma_client()
# #     def _initialize_chroma_client(self):
# #         try:
# #             os.makedirs(self.persistence_dir, exist_ok=True)
# #             self.client=chromadb.PersistentClient(path=self.persistence_dir)
# #             self.collection=self.client.get_or_create_collection(
# #                 name=self.collection_name,
# #                 metadata={"description":"Collection of PDF document embeddings"}
# #             )
# #             print(f"Initialized ChromaDB client: {self.collection_name}")
# #             # print(f"Existing documents in collection:{self.collection.count()}")
# #         except Exception as e:
# #             print(f"Error initializing ChromaDB client: {e}")
# #     def add_documents(self,documents:List[Document],Embeddings:np.ndarray):
# #         try:
# #             print("checking lengths")
# #             if len(documents)!=len(Embeddings):
# #                 raise ValueError("The number of documents are not equal to number of Embeddings")
# #             ids=[]
# #             metadatas=[]
# #             page_contents=[]
# #             embeddings_list=[]
# #             print("")
# #             for i,(doc,embedding) in enumerate(zip(documents,Embeddings)):
# #                 print(f"loop : {i}")
# #                 doc_id=str(uuid.uuid4())
# #                 ids.append(doc_id)
# #                 metadata=dict(doc.metadata)
# #                 metadata["doc_index"]=i
# #                 metadata["content_length"]=len(doc.page_content)
# #                 metadatas.append(metadata)
# #                 page_contents.append(doc.page_content)
# #                 embeddings_list.append(embedding.tolist())
# #                 print(f"loop end : {i}")
# #             try:
# #                 self.collection.add(
# #                     ids=ids,
# #                     metadatas=metadatas,
# #                     documents=page_contents,
# #                     embeddings=embeddings_list
# #                 )
# #                 print(f"Added {len(documents)} documents to ChromaDB collection: {self.collection_name}")
# #             except Exception as e:
# #                 print(f"Error adding documents to ChromaDB collection: {e}")
# #         except Exception as e:
# #             print(f"Error in add_documents method: {e}")
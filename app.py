import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from Data_loader import process_pdf_docs
from Split_documents import documents_splitter
from Embeddings_manager import EmbeddingManager
from VectorStore_manager import vectorStoreManager
from Rag_retriever import RagRetriever

from dotenv import load_dotenv
load_dotenv()

# Loading Documents
all_docs=process_pdf_docs("C:/Users/kr233/OneDrive/Desktop/RAG/pdfs")

# Splitting and Converting to Chunks
split_docs=documents_splitter(all_docs)

# Creating Embeddings for Chunks
Embedding_Manager=EmbeddingManager()
embeddings=Embedding_Manager.generate_embeddings(split_docs)

# Storing Embeddings to VectorDB
vectorstore=vectorStoreManager()
vectorstore.add_documents(split_docs,embeddings)

# Retrieving from Database
RAGretriever=RagRetriever(vectorstore, Embedding_Manager)

GROQ_API_KEY=os.getenv("GROQ_API_KEY")
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.5,
    max_tokens=1024
)

rag_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are an AI assistant that gives accurate and concise answers
to the user's questions using the provided context.

Instructions:
- Answer primarily using the provided context.
- Do not make up information that is not present in the context.
- If the answer cannot be found in the context, say:
  "The answer is not available in the provided context."
- Give a clear and concise answer."""
    ),
    (
        "human",
        """### Context:
{context}

### User Query:
{query}"""
    )
])

parser=StrOutputParser()

while True:
    query=input("User : ")
    if query.lower() in ["exit", "quit"]:
        print("Exiting the chat. Goodbye!")
        break
    retrieved_docs=RAGretriever.retrive(query)
    context = "\n\n".join(
        doc["document"] for doc in retrieved_docs
    )
    prompt = rag_prompt.invoke({"context": context,"query": query})
    response=llm.invoke(prompt)
    output=parser.invoke(response)
    print(f"AI : {output}")
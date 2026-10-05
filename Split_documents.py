from langchain_text_splitters import RecursiveCharacterTextSplitter

def documents_splitter(documents, chunk_size=1000, chunk_overlap=200):
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        separators=["\n\n","\n"," ",""]
    )
    split_docs=text_splitter.split_documents(documents)
    print(f"STEP-2 : split {len(documents)} into {len(split_docs)} number of chunks")

    return split_docs
from langchain_community.document_loaders import DirectoryLoader, PyMuPDFLoader
from pathlib import Path



def process_pdf_docs(directory_path):
    all_docs=[]
    path_dir= Path(directory_path)
    all_pdfs=list(path_dir.glob("**/*.pdf"))
    print(f"number of pdfs available in directory: {len(all_pdfs)}")

    for pdf in all_pdfs:
        try:
            loader=PyMuPDFLoader(pdf)
            pdf_doc=loader.load()
            # pdf_doc=PyMuPDFLoader(pdf).load()
            for doc in pdf_doc:
                doc.metadata["source file"] = pdf.name
                doc.metadata["type"]="pdf"

            all_docs.extend(pdf_doc)
            # print(f"Loaded {len(pdf_doc)} pages.")
        except Exception as e:
            print(f"Error loading {pdf.name}: {e}")
    print(f"STEP-1 : Total number of documents loaded: {len(all_docs)}")
    return all_docs


# "---------------------------Converting PDFs to Documents-------------------------------------------------------------------------"


# dir_loader=DirectoryLoader(
#     "C:/Users/kr233/OneDrive/Desktop/RAG/pdfs",
#     glob="**/*.pdf",
#     loader_cls=PyMuPDFLoader,
#     show_progress=False
# )
# pdf_docs=dir_loader.load()
# print(type(pdf_docs[0]))
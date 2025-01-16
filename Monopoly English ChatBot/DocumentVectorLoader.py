from langchain_core.documents import Document
def document_loader(vector):
    from loader import chunks
    vector.add_documents(documents=chunks)




    

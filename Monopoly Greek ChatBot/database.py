from DocumentVectorLoader import document_loader
from langchain_chroma import Chroma
from CustomBertEmbeddings import GreekBertEmbeddings
from sentence_transformers import SentenceTransformer
import os
chroma_path = './chroma'
model_name = 'nlpaueb/bert-base-greek-uncased-v1'
embeddings = GreekBertEmbeddings(model_name=model_name)
vector_store = Chroma(collection_name='greek_manual',embedding_function=embeddings,persist_directory=chroma_path)
items = os.listdir(chroma_path)
if not len(items) > 1 :
    document_loader(vector=vector_store)


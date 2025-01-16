from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from DocumentVectorLoader import document_loader
import os
chroma_path = './chroma'
load_dotenv(dotenv_path='./API/.env')
if not os.environ.get('OPENAI_API_KEY'):
    os.environ['OPENAI_API_KEY'] = os.getenv('API_KEY')
embeddings = OpenAIEmbeddings(model='text-embedding-3-large')
vector_store = Chroma(collection_name='manual',embedding_function=embeddings,persist_directory=chroma_path)
items = os.listdir(chroma_path)
if not len(items) > 1:
    document_loader(vector=vector_store)

    

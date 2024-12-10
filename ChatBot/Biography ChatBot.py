from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_ollama import ChatOllama
import os
API_KEY = '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'
os.environ['OPENAI_API_KEY'] = API_KEY
#loader = DirectoryLoader('biography/',glob='*.txt')
#bio = loader.load()
#text_splitter = RecursiveCharacterTextSplitter(chunk_size=256,chunk_overlap=20,separators=['.'])
#texts = text_splitter.split_documents(bio)
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
#splitted_documents = []
#for id,text in enumerate(texts):
    #splitted_documents.append(Document(page_content=text.page_content))
vector_store = Chroma(collection_name='biography_collection',embedding_function=embeddings,persist_directory='./chroma')
#vector_store.add_documents(documents=splitted_documents)
print('Assistant: "What do you want to know about Mike Τyson ?"')
query = input('Type here: ')
print(f'You: "{query}"')
results = vector_store.similarity_search_with_score(query,k=1)
llm = ChatOllama(model='llama2',temperature=0)
for doc,score in results:
    if score <= 1.5 and score >= 0.5 :
            print(doc.page_content)
            print(score)
            messages = [
                 (
                      'system',
                      f"You are a helpful assistant that tells the biography of someone or something based on the content that i give you now ({doc.page_content}) do not use more words from  the content i gave you, also  do not use in your response (according to the content)",
                 ),
                 ("human", f'{query}')
            ]
            ai_msg = llm.invoke(messages)
            print(f'Assistant: "{ai_msg.content}"')

    else:
        print('Assistant: "I\'m sorry, I can only answer questions that are covered in the biography I\'ve been given"')
        print(score)
        print(doc)


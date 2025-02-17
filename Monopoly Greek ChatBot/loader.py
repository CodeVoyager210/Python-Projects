from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import MarkdownHeaderTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
separators = ['\n\n',' ','',r'(?<=\.)']
chroma_path = './chroma'
items = os.listdir(chroma_path)
if len(items) > 1 :
    pass
else:
     loader = DirectoryLoader('data',glob='*.txt',show_progress=True)
     load = loader.load()
     headers_to_split_on = [
         ("#","title"),
         ("##","subtitle")
     ]
     markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
     md_header_splits = markdown_splitter.split_text(load[0].page_content)
     text_splitter = RecursiveCharacterTextSplitter(chunk_size=550,chunk_overlap=50,separators=separators)
     chunks = text_splitter.split_documents(md_header_splits)
     for chunk in chunks:
         chunk.metadata.update({
             "type" : "Manual",
             "author" : "Hasbro",
             "language" : "gr",
             "category" : "Board Games",
             "audience" : "Players familiar and new to MONOPOLY",
             "source" : "./data/monopoly_rules_translated_to_greek.txt"
         })

from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.text_splitter import MarkdownHeaderTextSplitter
import os
chroma_path = './chroma'
seperators = ['\n\n',r'(?<=!)','\n',' ','',r'(?<=\. )']
items = os.listdir(chroma_path)
if len(items) > 1:
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
 text_splitter = RecursiveCharacterTextSplitter(chunk_size=420,chunk_overlap=50,separators=seperators)
 chunks = text_splitter.split_documents(md_header_splits)
 for chunk in chunks:
    chunk.metadata.update({
       "type" : "Manual",
       "author" : "Hasbro",
       "language" : "en",
       "category" : "Board Games",
       "audience" : "Players familiar and new to MONOPOLY",
       "source" : "./data/monopoly_rules.txt"
    })





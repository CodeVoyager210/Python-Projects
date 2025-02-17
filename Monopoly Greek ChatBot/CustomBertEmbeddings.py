import torch
from transformers import AutoTokenizer, AutoModel
from langchain.embeddings.base import Embeddings
class GreekBertEmbeddings(Embeddings):
    def __init__(self,model_name):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)
    def embed_documents(self, texts):
        return [self._embed(text) for text in texts]
    def embed_query(self, text):
        return self._embed(text)
    def _embed(self, text):
        inputs = self.tokenizer(text,return_tensors="pt",padding=True,truncation=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
        embeddings = outputs.last_hidden_state
        embedding = embeddings.mean(dim=1).squeeze()
        return embedding.tolist()

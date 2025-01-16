from database import vector_store 
from langchain_ollama import ChatOllama
from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain_openai import ChatOpenAI
from langchain.chains.query_constructor.base import AttributeInfo
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain.prompts import PromptTemplate
class ChatBot:
    def __init__(self,user_input):
        metadata_field_info = [
            AttributeInfo(
                name="title",
                description="Type of rules in a Monopoly game manual, such as general gameplay rules or specific mechanics of the game",
                type="string"
            ),
            AttributeInfo(
                name="subtitle",
                description="Detailed rules on specific aspects of how the Monopoly game is played, based on different approaches or variations within the game (e.g., using the bus, buying houses, selling properties).",
                type="string"
            )
        ]
        document_content_description = "Monopoly game manual"
        llm_retriever = ChatOpenAI(model="gpt-4o-mini",temperature=0)
        llm = ChatOllama(model="llama2:13b",temperature=0)
        retriever = SelfQueryRetriever.from_llm(
            llm_retriever,
            vector_store,
            document_content_description,
            metadata_field_info,
        )
        system_prompt = (
             "Use the given context to answer the question. "
             "Only answer on the context i give you, if it's not in there say you only answer question based on the monopoly game manual. Also on your answer do not mention phrases like 'according to the context' or 'based on the given context.'"
             "Use three sentence maximum and keep the answer concise. "
             "Context: {context}"
        )
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system",system_prompt),
                ("human","{input}"),
            ]
        )
        question_answer_chain = create_stuff_documents_chain(llm,prompt)
        chain = create_retrieval_chain(retriever,question_answer_chain)
        self.response = chain.invoke({"input": user_input})['answer']
        


import streamlit as st
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

# Load the fine-tuned model
model = OllamaLLM(model="llama3.2")

# Define prompt template
template = """
You are an expert in answering questions about a pizza restaurant.

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Streamlit UI
st.title("Pizza Restaurant Chatbot 🍕")
st.write("Ask me anything about our restaurant!")

# User input
question = st.text_input("Ask your question:")

if question:
    reviews = retriever.invoke(question)
    result = chain.invoke({"reviews": reviews, "question": question})
    st.write("### Answer:")
    st.write(result)

from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
    max_tokens=100,
    openai_api_key=api_key,  
    verbose=True
)

response = llm.stream("Write a poem about AI")

for chunk in response:
    print(chunk.content, end="", flush=True)

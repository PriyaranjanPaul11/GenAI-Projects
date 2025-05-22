from langchain_community.llms import HuggingFaceHub
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
import os

load_dotenv()

model = HuggingFaceHub(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",  # Instruction-tuned model
    model_kwargs={"temperature": 0.7, "max_new_tokens": 250}
)

chat_history = [
    # HumanMessage(content='You are a helpful AI assistant.')
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history[-1:])
    print("\nAI: ", result)
    # chat_history.append(AIMessage(content=result))
    # print("\nAI: ",result)

print(chat_history)

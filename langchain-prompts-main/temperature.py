from langchain_community.llms import HuggingFaceHub
from dotenv import load_dotenv

load_dotenv()

model = HuggingFaceHub(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",  # Instruction-tuned model
    model_kwargs={"temperature": 1.5, "max_new_tokens": 512})

result = model.invoke("Write a 5 line poem on cricket")

print(result.content)
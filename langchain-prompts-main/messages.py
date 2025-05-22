from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_community.llms import HuggingFaceHub
from dotenv import load_dotenv

load_dotenv()

model = HuggingFaceHub(
    repo_id="openai-community/gpt2",  # Instruction-tuned model
    model_kwargs={"temperature": 0.7, "max_new_tokens": 512}
)

messages=[
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about LangChain')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)


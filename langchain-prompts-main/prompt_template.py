from langchain_core.prompts import PromptTemplate
from langchain_community.llms import HuggingFaceHub
from dotenv import load_dotenv

load_dotenv()

model = HuggingFaceHub(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",  # Instruction-tuned model
    model_kwargs={"temperature": 0.7, "max_new_tokens": 512}
)

# detailed way
template2 = PromptTemplate(
    template='Greet this person in 5 languages. The name of the person is {name}',
    input_variables=['name']
)

# fill the values of the placeholders
prompt = template2.invoke({'name':'nitish'})

result = model.invoke(prompt)

print(result.content)


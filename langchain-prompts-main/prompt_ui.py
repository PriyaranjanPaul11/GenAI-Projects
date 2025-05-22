from langchain_community.llms import HuggingFaceHub
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt
import os

load_dotenv()

# Initialize Hugging Face model (you can change the model ID if needed)
model = HuggingFaceHub(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",  # Instruction-tuned model
    model_kwargs={"temperature": 0.7, "max_new_tokens": 512}
)

st.header('Research Tool')

# Inputs
paper_input = st.selectbox(
    "Select Research Paper Name", 
    [
        "Attention Is All You Need", 
        "BERT: Pre-training of Deep Bidirectional Transformers", 
        "GPT-3: Language Models are Few-Shot Learners", 
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style", 
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select Explanation Length", 
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)

template = load_prompt('template.json')

if st.button('Summarize'):
    # Generate the formatted prompt using the template
    prompt = template.format(
        paper_input=paper_input,
        style_input=style_input,
        length_input=length_input
    )
    
    # Generate response
    result = model.invoke(prompt)
    st.write(result)

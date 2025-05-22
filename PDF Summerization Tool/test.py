import streamlit as st
import os
from utils import *
def main():
    st.set_page_config(page_title="PDF Summarizer")

    st.title("PDF Summarizing App")
    st.write("Summerize your pdf files in just a few seconds.")
    st.divider()

    pdf=st.file_uploader('Upload your pdf file',type='pdf')

    submit = st.button("Generate Summary")

    os.environ["OPENAI_API_KEY"]="YOUR_API_KEY"

    if submit:

        response=summarizer(pdf)

        st.subheader('Summary of the PDF file')
        st.write(response)


if __name__ == '__main__':
    main()
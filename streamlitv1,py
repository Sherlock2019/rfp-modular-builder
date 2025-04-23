# streamlit_app.py
import streamlit as st
from docx import Document
import os
import tempfile
import re

st.set_page_config(page_title="RFP Template Filler", layout="wide")
st.title("📄 Terraform-Inspired RFP Generator")

st.sidebar.header("Step 1: Upload Word Template")
template_file = st.sidebar.file_uploader("Upload your company RFP template (.docx)", type=["docx"])

st.sidebar.header("Step 2: Choose Module Sections")
def load_module(name):
    path = f"modules/{name}/main.txt"
    if os.path.exists(path):
        with open(path, "r") as f:
            return f.read()
    return ""

sections = [
    "EXECUTIVE_SUMMARY",
    "TECHNICAL_ARCHITECTURE",
    "PRICING_COMMERCIALS",
    "COMPANY_OVERVIEW",
    "CUSTOMER_UNDERSTANDING"
]

selected_sections = st.sidebar.multiselect("Select sections to include", sections, default=sections)

module_map = {tag: load_module(tag.lower()) for tag in selected_sections}

st.sidebar.header("Step 3: Fill Template")
if template_file is not None and st.sidebar.button("Generate Filled Document"):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
        tmp.write(template_file.read())
        doc = Document(tmp.name)

    for para in doc.paragraphs:
        for tag, content in module_map.items():
            placeholder = f"[[{tag}]]"
            if placeholder in para.text:
                para.text = para.text.replace(placeholder, content)

    output_path = tempfile.NamedTemporaryFile(delete=False, suffix=".docx").name
    doc.save(output_path)

    with open(output_path, "rb") as f:
        st.download_button(
            label="📥 Download Filled RFP Document",
            data=f.read(),
            file_name="Filled_RFP_Output.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
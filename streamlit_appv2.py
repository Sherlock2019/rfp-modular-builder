# streamlit_app.py
import streamlit as st
from docx import Document
import os
import tempfile

st.set_page_config(page_title="RFP Template Filler", layout="wide")
st.title("📄 Terraform-Inspired RFP Generator")

st.sidebar.header("Step 1: Upload Word Template")
template_file = st.sidebar.file_uploader("Upload your company RFP template (.docx)", type=["docx"])

st.sidebar.header("Step 2: Choose Module Sections")
module_dirs = sorted([name for name in os.listdir("modules") if os.path.isdir(f"modules/{name}")])
selected_modules = st.sidebar.multiselect("Select sections to include", module_dirs, default=module_dirs)

st.sidebar.header("Step 3: Fill Template")

edited_modules = {}
with st.form("edit_modules_form"):
    st.write("📝 **Edit Each Module Before Generating**")
    for module in selected_modules:
        path = f"modules/{module}/main.txt"
        with open(path, "r") as f:
            content = f.read()
        edited = st.text_area(f"{module}", value=content, height=250, key=module)
        edited_modules[module] = edited
    save_edits = st.form_submit_button("💾 Save Edits to Module Files")

if save_edits:
    for mod_name, content in edited_modules.items():
        os.makedirs(f"modules/{mod_name}", exist_ok=True)
        with open(f"modules/{mod_name}/main.txt", "w") as f:
            f.write(content)
    st.success("✅ All selected module files saved successfully.")

if template_file is not None and st.sidebar.button("📥 Generate Filled Document"):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
        tmp.write(template_file.read())
        doc = Document(tmp.name)

    for para in doc.paragraphs:
        for mod, text in edited_modules.items():
            placeholder = f"[[{mod.upper()}]]"
            if placeholder in para.text:
                para.text = para.text.replace(placeholder, text)

    output_path = tempfile.NamedTemporaryFile(delete=False, suffix=".docx").name
    doc.save(output_path)

    with open(output_path, "rb") as f:
        st.download_button(
            label="📥 Download Filled RFP Document",
            data=f.read(),
            file_name="Filled_RFP_Output.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )


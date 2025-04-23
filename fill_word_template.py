from docx import Document
import re
import os

def load_module_content(module_path):
    if os.path.exists(module_path):
        with open(module_path, "r") as file:
            return file.read().strip()
    return ""

def fill_word_template(template_path, output_path, module_map):
    doc = Document(template_path)
    for para in doc.paragraphs:
        for tag, content in module_map.items():
            placeholder = f"[[{tag}]]"
            if placeholder in para.text:
                para.text = para.text.replace(placeholder, content)
    doc.save(output_path)
    print(f"✅ Template filled and saved to {output_path}")

if __name__ == "__main__":
    # Example usage
    module_map = {
        "EXECUTIVE_SUMMARY": load_module_content("modules/executive_summary/main.txt"),
        "TECHNICAL_ARCHITECTURE": load_module_content("modules/technical_architecture/main.txt"),
        "PRICING_COMMERCIALS": load_module_content("modules/pricing_commercials/main.txt"),
        "COMPANY_OVERVIEW": "Rackspace is a cloud leader with OpenStack certifications.",
        "CUSTOMER_UNDERSTANDING": "Customer ABC wants cost savings and 5G scaling."
    }

    template_path = "templates/Company_Template.docx"
    output_path = "Filled_RFP_Output.docx"
    fill_word_template(template_path, output_path, module_map)
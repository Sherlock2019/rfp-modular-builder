# 📦 Terraform-Inspired Modular RFP Builder

Welcome to the official installation and usage guide for the **Modular RFP Builder**, a Terraform-inspired documentation automation tool for private/hybrid cloud providers.

---

## 🚀 Overview

This tool allows teams to:
- Create reusable, modular RFP responses
- Populate responses from input files (`customer_inputs.txt`)
- Assemble output as `.txt`, `.pdf`, or `.docx`
- Use your own `.docx` company templates
- Interact via CLI or web (Streamlit GUI)

---

## 🧰 Requirements

- Python 3.7+
- pip
- Optional: Pandoc (for PDF generation)

---

## 🔧 Installation (Local)

```bash
# 1. Clone the repo
https://github.com/your-org/rfp-modular-builder.git
cd rfp-modular-builder

# 2. Install dependencies
pip install -r requirements.txt

# 3. Make sure scripts are executable
chmod +x assemble_rfp.sh export_pdf.sh
```

---

## 🖥️ Usage Modes

### 1. 💻 CLI Mode

```bash
# Step 1: Generate customer_inputs.txt interactively
python3 rfp_init.py

# Step 2: Assemble RFP
make build

# Step 3: Optional PDF Export (Requires Pandoc)
./export_pdf.sh
```

### 2. 🌐 Streamlit Web GUI

```bash
make gui
```
Open `http://localhost:8501` in your browser:
- Upload your `.docx` template
- Select which modules to use
- Download the filled `.docx` RFP

---

## 🧩 File Structure

```
rfp-modular-builder/
├── modules/                     # Reusable content blocks
│   └── executive_summary/
│       └── main.txt
├── templates/                  # Upload company Word templates here
│   └── Company_Template.docx
├── customer_inputs.txt         # Inputs like terraform.tfvars
├── main.tf                     # Controls module order
├── assemble_rfp.sh             # CLI assembler script
├── export_pdf.sh               # Optional Pandoc export
├── rfp_init.py                 # CLI wizard for input file
├── streamlit_app.py            # Web GUI app
├── requirements.txt
├── Makefile                    # Commands: init, build, gui, clean
```

---

## 🧪 Example Use Case: ABC Telecom
- Goal: Cut infra costs, support 5G
- Output: Customized Word & PDF RFP using OpenStack modules
- Input: All customer-specific content defined in `customer_inputs.txt`

---

## 📌 Next Steps

- Add more modules in `modules/`
- Upload your `.docx` templates to `templates/`
- Customize `main.tf` to control doc structure
- Contribute on GitHub with improvements!

---

## 💬 Support
Have questions or feedback? Submit an issue or contact the dev team via Slack or email.

---

## 📜 License
MIT License © 2024
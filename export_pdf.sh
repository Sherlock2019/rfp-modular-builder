#!/bin/bash

FINAL=$(ls Final_RFP_*.txt | tail -n 1)

if [[ -f "$FINAL" ]]; then
    pandoc "$FINAL" -o "${FINAL%.txt}.pdf"
    echo "✅ Converted to PDF: ${FINAL%.txt}.pdf"
else
    echo "❌ No final RFP found. Please run ./assemble_rfp.sh first."
fi
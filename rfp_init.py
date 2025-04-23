#!/usr/bin/env python3

import os

def get_input(prompt, default=""):
    response = input(f"{prompt} [{default}]: ").strip()
    return response if response else default

def main():
    print("🧙 Welcome to the RFP CLI Wizard")
    inputs = {
        "customer_name": get_input("Customer Name", "ABC"),
        "business_goals": get_input("Business Goals", "Reduce costs, meet compliance"),
        "current_issues": get_input("Current Issues", "Legacy infra, no visibility"),
        "technical_requirements": get_input("Technical Requirements", "HA OpenStack, Ceph"),
        "proposed_architecture": get_input("Proposed Architecture", "3-node HA control plane"),
        "customer_workloads": get_input("Customer Workloads", "5G Core, BSS/OSS"),
        "scalability_details": get_input("Scalability Details", "Auto-scaling, Heat orchestration"),
        "pricing_model": get_input("Pricing Model", "Fixed + usage-based burst"),
        "payment_terms": get_input("Payment Terms", "Net 30"),
        "key_benefits_drivers": get_input("Key Benefits", "Lower TCO, increased performance"),
        "rackspace_differentiation": get_input("Rackspace Advantage", "Telecom-grade OpenStack support")
    }

    with open("customer_inputs.txt", "w") as f:
        for k, v in inputs.items():
            f.write(f'{k} = "{v}"\n')

    print("✅ Input file saved as customer_inputs.txt")

if __name__ == "__main__":
    main()

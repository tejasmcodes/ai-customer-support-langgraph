import os

DATA_DIR = "data"

def retrieve_context(intent):
    files = {
        "Sales": "pricing.txt",
        "Billing": "policy.txt",
        "Technical": "technical.txt",
        "Account": "faq.txt",
    }

    filename = files.get(intent)

    if not filename:
        return ""

    path = os.path.join(DATA_DIR, filename)

    with open(path, "r") as f:
        return f.read()
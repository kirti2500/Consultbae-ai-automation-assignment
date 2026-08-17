import re
import pandas as pd


def normalize_phone(raw):
    if pd.isna(raw):
        return None
    digits = re.sub(r"\D", "", str(raw))
    return digits[-10:] if len(digits) >= 10 else None


def normalize_email(raw):
    if pd.isna(raw):
        return None
    return str(raw).strip().lower()


def normalize_city(raw):
    if pd.isna(raw):
        return None
    city_map = {
        "gurgaon": "Gurugram",
        "gurugram": "Gurugram",
        "new delhi": "Delhi",
        "delhi ncr": "Delhi",
        "delhi": "Delhi",
        "noida": "Noida",
        "pune": "Pune",
        "bangalore": "Bengaluru",
        "bengaluru": "Bengaluru",
    }
    cleaned = str(raw).strip().lower()
    return city_map.get(cleaned, str(raw).strip().title())


if __name__ == "__main__":
    test_numbers = ["9000000254", "+919000000254", "09000000254", "919000000268", "+91-9000000131"]
    for x in test_numbers:
        print(x, "->", normalize_phone(x))

    test_emails = ["isha.chopra95@mailtest.example.org", "ISHA.CHOPRA95@MAILTEST.EXAMPLE.ORG", "  rohit.verma13@mailtest.example.org  "]
    for x in test_emails:
        print(x, "->", normalize_email(x))

    test_cities = ["GURGAON", "gurugram ", "New Delhi", "Bangalore", "  Pune"]
    for x in test_cities:
        print(x, "->", normalize_city(x))
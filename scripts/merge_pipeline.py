import re
from datetime import datetime
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


def normalize_ctc(raw):
    if pd.isna(raw):
        return None
    val = float(raw)
    return round(val * 100000) if val < 100 else round(val)


def parse_messy_date(raw):
    if pd.isna(raw):
        return None
    raw = str(raw).strip()
    formats = ["%d-%m-%Y", "%Y-%m-%d", "%d %b %Y", "%m/%d/%Y"]
    for fmt in formats:
        try:
            return datetime.strptime(raw, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return None


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

    test_ctc = [417964, 4.2, 8.3, 11.2]
    for x in test_ctc:
        print(x, "->", normalize_ctc(x))

    test_dates = ["24-07-2026", "2026-08-08", "7 Jul 2026", "07/13/2026"]
    for x in test_dates:
        print(x, "->", parse_messy_date(x))
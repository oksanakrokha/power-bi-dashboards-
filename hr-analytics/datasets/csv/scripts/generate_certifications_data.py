import pandas as pd
from pathlib import Path
from datetime import timedelta
import random


BASE_FOLDER = Path(__file__).resolve().parent.parent

DATA_FOLDER = BASE_FOLDER / "data" / "generated"


employees = pd.read_csv(
    DATA_FOLDER / "employees.csv"
)


# ==========================================
# Certifications reference
# ==========================================

certifications = [
    ("Microsoft Power BI Data Analyst", True),
    ("Microsoft Dynamics Fundamentals", True),
    ("Workplace Safety Training", True),
    ("CompTIA Network+", False),
    ("Cisco CCNA", False),
    ("Project Management Fundamentals", False)
]


cert_rows = []

for index, cert in enumerate(certifications, start=1):

    cert_rows.append(
        {
            "certification_id": index,
            "certification_name": cert[0],
            "is_required": cert[1]
        }
    )


cert_df = pd.DataFrame(cert_rows)


cert_df.to_csv(
    DATA_FOLDER / "certifications.csv",
    index=False
)


# ==========================================
# Employee certifications
# ==========================================

employee_certifications = []

employee_certification_id = 1


for _, employee in employees.iterrows():

    # not everyone has certificates

    if random.random() > 0.45:
        continue


    selected = random.sample(
        range(1, len(certifications)+1),
        random.randint(1,3)
    )


    for cert_id in selected:

        issue_year = random.randint(
            2023,
            2026
        )


        issue_date = pd.Timestamp(
            f"{issue_year}-01-15"
        )


        expiry_date = (
            issue_date
            +
            pd.DateOffset(years=2)
        )


        today = pd.Timestamp(
            "2026-07-24"
        )


        if expiry_date < today:
            status = "Expired"

        elif expiry_date <= today + pd.DateOffset(months=2):
            status = "Expiring Soon"

        else:
            status = "Active"



        employee_certifications.append(
            {
                "employee_certification_id":
                    employee_certification_id,

                "employee_id":
                    employee["employee_id"],

                "certification_id":
                    cert_id,

                "issue_date":
                    issue_date.date(),

                "expiry_date":
                    expiry_date.date(),

                "status":
                    status
            }
        )


        employee_certification_id += 1



employee_cert_df = pd.DataFrame(
    employee_certifications
)


employee_cert_df.to_csv(
    DATA_FOLDER / "employee_certifications.csv",
    index=False
)


print(
    "certifications:",
    len(cert_df)
)

print(
    "employee_certifications:",
    len(employee_cert_df)
)

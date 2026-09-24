import pandas as pd
from faker import Faker
from pathlib import Path
from datetime import date, timedelta
import random


# ==========================================
# Configuration
# ==========================================

fake = Faker()

OUTPUT_FOLDER = Path(__file__).resolve().parent.parent / "data" / "generated"

OUTPUT_FOLDER.mkdir(
    parents=True,
    exist_ok=True
)


EMPLOYEE_COUNT = 500
VACANCY_COUNT = 300
CANDIDATE_COUNT = 3500


START_DATE = date(2023, 1, 1)
END_DATE = date(2026, 12, 31)


# ==========================================
# Reference Data
# ==========================================


employment_types = [
    "Full-Time",
    "Part-Time",
    "Contract",
    "Temporary"
]


employment_statuses = [
    "Probation",
    "Active",
    "Terminated"
]


termination_reasons = [
    ("A", "Shortage of Work / Layoff / End of Contract"),
    ("B", "Strike or Lockout"),
    ("C", "Return to School"),
    ("D", "Illness or Injury"),
    ("E", "Quit"),
    ("F", "Maternity"),
    ("G", "Mandatory Retirement / Workforce Reduction"),
    ("H", "Work-Sharing"),
    ("J", "Apprentice Training"),
    ("K", "Other"),
    ("M", "Dismissal"),
    ("N", "Leave of Absence"),
    ("P", "Parental"),
    ("Z", "Compassionate Care / Family Caregiver")
]


departments = {
    "Information Technology": [
        "Software Developer",
        "Data Analyst"
    ],
    "Human Resources": [
        "HR Specialist"
    ],
    "Sales": [
        "Sales Representative"
    ],
    "Operations": [
        "Field Technician",
        "Operations Manager"
    ],
    "Finance": [
    "Financial Analyst"
    ]
}


# ==========================================
# Generate Reference CSV
# ==========================================


def generate_reference_data():

    pd.DataFrame(
        {
            "employment_type_id": range(1, len(employment_types)+1),
            "name": employment_types
        }
    ).to_csv(
        OUTPUT_FOLDER / "employment_types.csv",
        index=False
    )


    pd.DataFrame(
        {
            "employment_status_id": range(1, len(employment_statuses)+1),
            "name": employment_statuses
        }
    ).to_csv(
        OUTPUT_FOLDER / "employment_statuses.csv",
        index=False
    )


    pd.DataFrame(
        {
            "termination_reason_id": range(1, len(termination_reasons)+1),
            "code": [x[0] for x in termination_reasons],
            "reason": [x[1] for x in termination_reasons]
        }
    ).to_csv(
        OUTPUT_FOLDER / "termination_reasons.csv",
        index=False
    )


    department_rows = []

    for index, department in enumerate(departments.keys(), start=1):
        department_rows.append(
            {
                "department_id": index,
                "name": department
            }
        )


    pd.DataFrame(
        department_rows
    ).to_csv(
        OUTPUT_FOLDER / "departments.csv",
        index=False
    )


    position_rows = []

    position_id = 1

    for department_id, (department, positions) in enumerate(
        departments.items(),
        start=1
    ):

        for position in positions:

            position_rows.append(
                {
                    "position_id": position_id,
                    "department_id": department_id,
                    "title": position
                }
            )

            position_id += 1


    pd.DataFrame(
        position_rows
    ).to_csv(
        OUTPUT_FOLDER / "positions.csv",
        index=False
    )



# ==========================================
# Generate Employees
# ==========================================


def random_date(start, end):
    delta = end - start
    return start + timedelta(
        days=random.randint(0, delta.days)
    )


def generate_employees():

    # Load generated reference data

    departments_df = pd.read_csv(
        OUTPUT_FOLDER / "departments.csv"
    )

    positions_df = pd.read_csv(
        OUTPUT_FOLDER / "positions.csv"
    )

    employment_types_df = pd.read_csv(
        OUTPUT_FOLDER / "employment_types.csv"
    )

    employment_statuses_df = pd.read_csv(
        OUTPUT_FOLDER / "employment_statuses.csv"
    )

    employees = []


    # Create managers first

    manager_ids = []


    for i in range(1, 21):

        department = departments_df.sample(1).iloc[0]

        available_positions = positions_df[
            positions_df["department_id"]
            ==
            department["department_id"]
        ]


        if available_positions.empty:
            continue


        position = available_positions.sample(1).iloc[0]


        employee = {

            "employee_id": i,

            "first_name": fake.first_name(),

            "last_name": fake.last_name(),

            "date_of_birth": random_date(
                date(1970,1,1),
                date(1990,12,31)
            ),

            "photo_url":
                f"https://sharepoint.uptime-solutions.com/photos/{i}.jpg",

            "email":
                f"employee{i}@uptime-solutions.com",

            "department_id":
                department["department_id"],

            "position_id":
                position["position_id"],

            "manager_id":
                None,

            "employment_type_id":
                random.choice(
                    employment_types_df[
                        "employment_type_id"
                    ].tolist()
                ),

            "employment_status_id":
                employment_statuses_df[
                    employment_statuses_df["name"]
                    ==
                    "Active"
                ].iloc[0]["employment_status_id"],

           "hire_date":
                random_date(
                     date(2017,1,1),
                    date(2020,12,31)
                ),

            "termination_date":
                None,

            "termination_reason_id":
                None
        }


        employees.append(employee)

        manager_ids.append(i)



    # Create remaining employees


    for i in range(21, EMPLOYEE_COUNT + 1):

        department = departments_df.sample(1).iloc[0]


        available_positions = positions_df[
            positions_df["department_id"]
            ==
            department["department_id"]
        ]


        position = available_positions.sample(1).iloc[0]


        hire_date = random_date(
            date(2020,1,1),
            END_DATE
        )


        status = random.choices(
    [
        "Probation",
        "Active",
        "Terminated"
    ],
    weights=[
        10,
        80,
        10
    ],
    k=1
)[0]


        termination_date = None
        termination_reason_id = None


        if status == "Terminated":

            termination_date = random_date(
                hire_date,
                END_DATE
            )

            termination_reason_id = random.randint(
                1,
                len(termination_reasons)
            )


        employee = {

            "employee_id": i,

            "first_name":
                fake.first_name(),

            "last_name":
                fake.last_name(),

            "date_of_birth":
                random_date(
                    date(1965,1,1),
                    date(2000,12,31)
                ),

            "photo_url":
                f"https://sharepoint.uptime-solutions.com/photos/{i}.jpg",

            "email":
                f"employee{i}@uptime-solutions.com",

            "department_id":
                department["department_id"],

            "position_id":
                position["position_id"],

            "manager_id":
                random.choice(manager_ids),

            "employment_type_id":
                random.choice(
                    employment_types_df[
                        "employment_type_id"
                    ].tolist()
                ),

            "employment_status_id":
                employment_statuses_df[
                    employment_statuses_df["name"]
                    ==
                    status
                ].iloc[0]["employment_status_id"],

            "hire_date":
                hire_date,

            "termination_date":
                termination_date,

            "termination_reason_id":
                termination_reason_id
        }


        employees.append(employee)



    employees_df = pd.DataFrame(employees)


    integer_columns = [
        "employee_id",
        "department_id",
        "position_id",
        "employment_type_id",
        "employment_status_id"
           ]

    employees_df["manager_id"] = (
    employees_df["manager_id"]
    .astype("Int64")
    )


    employees_df["termination_reason_id"] = (
    employees_df["termination_reason_id"]
    .astype("Int64")
    )

    for column in integer_columns:
        employees_df[column] = (
            employees_df[column]
            .fillna(0)
            .astype(int)
        )


    employees_df["termination_reason_id"] = (
        employees_df["termination_reason_id"]
        .replace(0, "")
    )


    employees_df.to_csv(
        OUTPUT_FOLDER / "employees.csv",
        index=False
    )


    print(
        "employees.csv generated:",
        len(employees_df)
    )




print("Reference data generator ready")

generate_reference_data()

generate_employees()
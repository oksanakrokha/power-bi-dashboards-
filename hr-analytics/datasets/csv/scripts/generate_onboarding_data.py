import pandas as pd
from pathlib import Path
from datetime import timedelta
import random


BASE_FOLDER = Path(__file__).resolve().parent.parent

DATA_FOLDER = BASE_FOLDER / "data" / "generated"


# ==========================================
# Load data
# ==========================================

departments = pd.read_csv(
    DATA_FOLDER / "departments.csv"
)

employees = pd.read_csv(
    DATA_FOLDER / "employees.csv"
)


# ==========================================
# Templates
# ==========================================

templates = []

template_id = 1

for _, dept in departments.iterrows():

    templates.append(
        {
            "template_id": template_id,
            "department_id": dept["department_id"],
            "template_name":
                f"{dept['name']} Employee Onboarding"
        }
    )

    template_id += 1


templates_df = pd.DataFrame(templates)


templates_df.to_csv(
    DATA_FOLDER / "onboarding_templates.csv",
    index=False
)


# ==========================================
# Tasks
# ==========================================

task_list = {

    "Information Technology":
    [
        "Setup workstation",
        "Security training",
        "Access permissions"
    ],

    "Human Resources":
    [
        "HR policies review",
        "Benefits enrollment",
        "Company handbook review"
    ],

    "Sales":
    [
        "CRM training",
        "Sales process training"
    ],

    "Operations":
    [
        "Safety training",
        "Equipment training"
    ],

    "Finance":
    [
        "Finance systems access",
        "Compliance training"
    ]

}


tasks = []

task_id = 1


for _, template in templates_df.iterrows():

    department_name = departments[
        departments["department_id"]
        ==
        template["department_id"]
    ].iloc[0]["name"]


    for task in task_list.get(
        department_name,
        []
    ):

        tasks.append(
            {
                "task_id": task_id,

                "template_id":
                    template["template_id"],

                "task_name":
                    task,

                "is_required":
                    True
            }
        )

        task_id += 1



tasks_df = pd.DataFrame(tasks)


tasks_df.to_csv(
    DATA_FOLDER / "onboarding_tasks.csv",
    index=False
)


# ==========================================
# Employee onboarding tasks
# ==========================================

employee_tasks = []

employee_task_id = 1


# only employees hired after 2023

new_employees = employees[
    pd.to_datetime(
        employees["hire_date"]
    )
    >=
    "2023-01-01"
]


for _, employee in new_employees.iterrows():

    employee_department = employee["department_id"]


    department_template = templates_df[
        templates_df["department_id"]
        ==
        employee_department
    ].iloc[0]


    department_tasks = tasks_df[
        tasks_df["template_id"]
        ==
        department_template["template_id"]
    ]


    for _, task in department_tasks.iterrows():

        employee_tasks.append(
            {
                "employee_task_id":
                    employee_task_id,

                "employee_id":
                    employee["employee_id"],

                "task_id":
                    task["task_id"],

                "status":
                    random.choice(
                        [
                            "Completed",
                            "Pending"
                        ]
                    ),

                "completed_date":
                    None
            }
        )

        employee_task_id += 1



employee_tasks_df = pd.DataFrame(
    employee_tasks
)


employee_tasks_df.to_csv(
    DATA_FOLDER / "employee_onboarding_tasks.csv",
    index=False
)


print(
    "onboarding_templates:",
    len(templates_df)
)

print(
    "onboarding_tasks:",
    len(tasks_df)
)

print(
    "employee_onboarding_tasks:",
    len(employee_tasks_df)
)
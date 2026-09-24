import pandas as pd
from pathlib import Path
from datetime import timedelta
import random


# ==========================================
# Configuration
# ==========================================

BASE_FOLDER = Path(__file__).resolve().parent.parent

INPUT_FOLDER = BASE_FOLDER / "data" / "generated"

OUTPUT_FILE = INPUT_FOLDER / "employment_history.csv"


# ==========================================
# Load Employees
# ==========================================

employees_df = pd.read_csv(
    INPUT_FOLDER / "employees.csv"
)


# ==========================================
# Generate Employment History
# ==========================================

history = []

history_id = 1


for _, employee in employees_df.iterrows():

    employee_id = employee["employee_id"]

    hire_date = pd.to_datetime(
        employee["hire_date"]
    ).date()


    current_department = employee["department_id"]
    current_position = employee["position_id"]
    current_manager = employee["manager_id"]
    current_type = employee["employment_type_id"]


    # 60% employees have only one history record
    # 40% have previous position

    has_history = random.random() < 0.4


    if has_history:

        change_date = hire_date + timedelta(
            days=random.randint(180, 900)
        )


        # Previous position record

        history.append(
            {
                "employment_history_id": history_id,
                "employee_id": employee_id,
                "department_id": current_department,
                "position_id": current_position,
                "manager_id": current_manager,
                "employment_type_id": current_type,
                "start_date": hire_date,
                "end_date": change_date - timedelta(days=1)
            }
        )

        history_id += 1


        # Current position record

        history.append(
            {
                "employment_history_id": history_id,
                "employee_id": employee_id,
                "department_id": current_department,
                "position_id": current_position,
                "manager_id": current_manager,
                "employment_type_id": current_type,
                "start_date": change_date,
                "end_date": None
            }
        )

        history_id += 1


    else:

        history.append(
            {
                "employment_history_id": history_id,
                "employee_id": employee_id,
                "department_id": current_department,
                "position_id": current_position,
                "manager_id": current_manager,
                "employment_type_id": current_type,
                "start_date": hire_date,
                "end_date": None
            }
        )

        history_id += 1



# ==========================================
# Save CSV
# ==========================================


history_df = pd.DataFrame(history)


history_df.to_csv(
    OUTPUT_FILE,
    index=False
)


print(
    "employment_history.csv generated:",
    len(history_df)
)
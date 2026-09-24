import pandas as pd
from pathlib import Path
import sys


# ==========================================================
# UpTime Solutions Inc.
# HR Analytics Data Validator
# Part 1
# ==========================================================


BASE_FOLDER = Path(__file__).resolve().parent.parent

DATA_FOLDER = BASE_FOLDER / "data" / "generated"


EXPECTED_FILES = {

    "employment_types.csv": [
        "employment_type_id",
        "name"
    ],

    "employment_statuses.csv": [
        "employment_status_id",
        "name"
    ],

    "termination_reasons.csv": [
        "termination_reason_id",
        "code",
        "reason"
    ],

    "departments.csv": [
        "department_id",
        "name"
    ],

    "positions.csv": [
        "position_id",
        "department_id",
        "title"
    ],

    "employees.csv": [
        "employee_id",
        "first_name",
        "last_name",
        "date_of_birth",
        "photo_url",
        "email",
        "department_id",
        "position_id",
        "manager_id",
        "employment_type_id",
        "employment_status_id",
        "hire_date",
        "termination_date",
        "termination_reason_id"
    ],

    "employment_history.csv": [
        "employment_history_id",
        "employee_id",
        "department_id",
        "position_id",
        "manager_id",
        "employment_type_id",
        "start_date",
        "end_date"
    ],

    "vacancies.csv": [
        "vacancy_id",
        "department_id",
        "position_id",
        "recruiter_id",
        "status",
        "opened_date",
        "closed_date"
    ],

    "candidates.csv": [
        "candidate_id",
        "first_name",
        "last_name",
        "email",
        "vacancy_id",
        "application_date"
    ],

    "offers.csv": [
        "offer_id",
        "candidate_id",
        "offer_date",
        "accepted",
        "hire_date"
    ],

    "onboarding_templates.csv": [
        "template_id",
        "department_id",
        "template_name"
    ],

    "onboarding_tasks.csv": [
        "task_id",
        "template_id",
        "task_name",
        "is_required"
    ],

    "employee_onboarding_tasks.csv": [
        "employee_task_id",
        "employee_id",
        "task_id",
        "status",
        "completed_date"
    ],

    "certifications.csv": [
        "certification_id",
        "certification_name",
        "is_required"
    ],

    "employee_certifications.csv": [
        "employee_certification_id",
        "employee_id",
        "certification_id",
        "issue_date",
        "expiry_date",
        "status"
    ]

}


dataframes = {}

errors = []


# ==========================================================
# Helper
# ==========================================================


def add_error(message):

    errors.append(message)

    print(f"[ERROR] {message}")


def ok(message):

    print(f"[ OK ] {message}")


# ==========================================================
# Check Files
# ==========================================================


def check_files():

    print("\nChecking CSV files...\n")

    for filename in EXPECTED_FILES:

        file_path = DATA_FOLDER / filename

        if not file_path.exists():

            add_error(f"{filename} not found")

            continue

        try:

            df = pd.read_csv(file_path)

            dataframes[filename] = df

            ok(filename)

        except Exception as ex:

            add_error(f"{filename}: {ex}")


# ==========================================================
# Check Columns
# ==========================================================


def check_columns():

    print("\nChecking columns...\n")

    for filename, expected_columns in EXPECTED_FILES.items():

        if filename not in dataframes:

            continue

        df = dataframes[filename]

        actual = list(df.columns)

        if actual == expected_columns:

            ok(filename)

        else:

            add_error(
                f"{filename} columns mismatch"
            )
            # ==========================================================
# Primary Keys
# ==========================================================

PRIMARY_KEYS = {
    "employment_types.csv": "employment_type_id",
    "employment_statuses.csv": "employment_status_id",
    "termination_reasons.csv": "termination_reason_id",
    "departments.csv": "department_id",
    "positions.csv": "position_id",
    "employees.csv": "employee_id",
    "employment_history.csv": "employment_history_id",
    "vacancies.csv": "vacancy_id",
    "candidates.csv": "candidate_id",
    "offers.csv": "offer_id",
    "onboarding_templates.csv": "template_id",
    "onboarding_tasks.csv": "task_id",
    "employee_onboarding_tasks.csv": "employee_task_id",
    "certifications.csv": "certification_id",
    "employee_certifications.csv": "employee_certification_id"
}


def check_primary_keys():

    print("\nChecking Primary Keys...\n")

    for filename, pk in PRIMARY_KEYS.items():

        if filename not in dataframes:
            continue

        df = dataframes[filename]

        if pk not in df.columns:

            add_error(f"{filename}: missing PK column {pk}")
            continue

        if df[pk].isnull().any():

            add_error(f"{filename}: NULL values in {pk}")

        elif df[pk].duplicated().any():

            add_error(f"{filename}: duplicate {pk}")

        else:

            ok(f"{filename} ({pk})")


# ==========================================================
# Required Fields
# ==========================================================

REQUIRED_COLUMNS = {

    "employees.csv": [
        "first_name",
        "last_name",
        "email",
        "department_id",
        "position_id",
        "employment_type_id",
        "employment_status_id",
        "hire_date"
    ],

    "employment_history.csv": [
        "employee_id",
        "department_id",
        "position_id",
        "employment_type_id",
        "start_date"
    ],

    "vacancies.csv": [
        "department_id",
        "position_id",
        "status",
        "opened_date"
    ],

    "candidates.csv": [
        "first_name",
        "last_name",
        "email",
        "vacancy_id",
        "application_date"
    ],

    "offers.csv": [
        "candidate_id",
        "offer_date",
        "accepted"
    ]

}


def check_required_fields():

    print("\nChecking required fields...\n")

    for filename, columns in REQUIRED_COLUMNS.items():

        if filename not in dataframes:
            continue

        df = dataframes[filename]

        for column in columns:

            if df[column].isnull().any():

                add_error(
                    f"{filename}: NULL values in {column}"
                )

        ok(filename)


# ==========================================================
# Duplicate Business Keys
# ==========================================================


def check_duplicates():

    print("\nChecking duplicates...\n")

    if "employees.csv" in dataframes:

        employees = dataframes["employees.csv"]

        if employees["email"].duplicated().any():

            add_error("Duplicate employee emails")

        else:

            ok("Employee emails")


    if "candidates.csv" in dataframes:

        candidates = dataframes["candidates.csv"]

        duplicated = candidates.duplicated(
            subset=["email", "vacancy_id"]
        )

        if duplicated.any():

            add_error(
                "Duplicate candidates for same vacancy"
            )

        else:

            ok("Candidates")


    if "employee_onboarding_tasks.csv" in dataframes:

        onboarding = dataframes[
            "employee_onboarding_tasks.csv"
        ]

        duplicated = onboarding.duplicated(
            subset=[
                "employee_id",
                "task_id"
            ]
        )

        if duplicated.any():

            add_error(
                "Duplicate onboarding tasks"
            )

        else:

            ok("Employee onboarding tasks")


    if "employee_certifications.csv" in dataframes:

        cert = dataframes[
            "employee_certifications.csv"
        ]

        duplicated = cert.duplicated(
            subset=[
                "employee_id",
                "certification_id",
                "issue_date"
            ]
        )

        if duplicated.any():

            add_error(
                "Duplicate employee certifications"
            )

        else:

            ok("Employee certifications")


# ==========================================================
# Row Counts
# ==========================================================


def check_row_counts():

    print("\nChecking row counts...\n")

    for filename, df in dataframes.items():

        print(
            f"{filename:<35} {len(df):>8} rows"
        )
        # ==========================================================
# Foreign Keys
# ==========================================================

FOREIGN_KEYS = [

    ("positions.csv", "department_id",
     "departments.csv", "department_id"),

    ("employees.csv", "department_id",
     "departments.csv", "department_id"),

    ("employees.csv", "position_id",
     "positions.csv", "position_id"),

    ("employees.csv", "manager_id",
     "employees.csv", "employee_id"),

    ("employees.csv", "employment_type_id",
     "employment_types.csv", "employment_type_id"),

    ("employees.csv", "employment_status_id",
     "employment_statuses.csv", "employment_status_id"),

    ("employees.csv", "termination_reason_id",
     "termination_reasons.csv", "termination_reason_id"),

    ("employment_history.csv", "employee_id",
     "employees.csv", "employee_id"),

    ("employment_history.csv", "department_id",
     "departments.csv", "department_id"),

    ("employment_history.csv", "position_id",
     "positions.csv", "position_id"),

    ("employment_history.csv", "manager_id",
     "employees.csv", "employee_id"),

    ("employment_history.csv", "employment_type_id",
     "employment_types.csv", "employment_type_id"),

    ("vacancies.csv", "department_id",
     "departments.csv", "department_id"),

    ("vacancies.csv", "position_id",
     "positions.csv", "position_id"),

    ("vacancies.csv", "recruiter_id",
     "employees.csv", "employee_id"),

    ("candidates.csv", "vacancy_id",
     "vacancies.csv", "vacancy_id"),

    ("offers.csv", "candidate_id",
     "candidates.csv", "candidate_id"),

    ("onboarding_templates.csv", "department_id",
     "departments.csv", "department_id"),

    ("onboarding_tasks.csv", "template_id",
     "onboarding_templates.csv", "template_id"),

    ("employee_onboarding_tasks.csv", "employee_id",
     "employees.csv", "employee_id"),

    ("employee_onboarding_tasks.csv", "task_id",
     "onboarding_tasks.csv", "task_id"),

    ("employee_certifications.csv", "employee_id",
     "employees.csv", "employee_id"),

    ("employee_certifications.csv", "certification_id",
     "certifications.csv", "certification_id")

]


def check_foreign_keys():

    print("\nChecking Foreign Keys...\n")

    for source_file, source_column, target_file, target_column in FOREIGN_KEYS:

        if source_file not in dataframes:
            continue

        if target_file not in dataframes:
            continue

        source = dataframes[source_file]
        target = dataframes[target_file]

        values = source[source_column].dropna()

        valid = set(target[target_column])

        invalid = values[~values.isin(valid)]

        if len(invalid):

            add_error(
                f"{source_file}: invalid FK {source_column}"
            )

        else:

            ok(f"{source_file} -> {target_file}")


# ==========================================================
# Business Rules
# ==========================================================


def check_business_rules():

    print("\nChecking business rules...\n")

    employees = dataframes["employees.csv"]

    statuses = dataframes[
        "employment_statuses.csv"
    ]

    status_lookup = dict(
        zip(
            statuses["employment_status_id"],
            statuses["name"]
        )
    )

    for _, row in employees.iterrows():

        status = status_lookup[
            row["employment_status_id"]
        ]

        if status in ["Active", "Probation"]:

            if pd.notna(row["termination_date"]):

                add_error(
                    f"Employee {row['employee_id']} "
                    "is Active/Probation but has termination_date"
                )

        if status == "Terminated":

            if pd.isna(row["termination_date"]):

                add_error(
                    f"Employee {row['employee_id']} "
                    "missing termination_date"
                )

            if pd.isna(row["termination_reason_id"]):

                add_error(
                    f"Employee {row['employee_id']} "
                    "missing termination_reason"
                )

    ok("Employee status rules")


    history = dataframes["employment_history.csv"]

    invalid = history[
        (history["end_date"].notna()) &
        (history["end_date"] < history["start_date"])
    ]

    if len(invalid):

        add_error(
            "Employment history date errors"
        )

    else:

        ok("Employment history dates")


    offers = dataframes["offers.csv"]

    invalid = offers[
        (offers["hire_date"].notna()) &
        (offers["hire_date"] < offers["offer_date"])
    ]

    if len(invalid):

        add_error(
            "Offer dates incorrect"
        )

    else:

        ok("Offer dates")


    cert = dataframes["employee_certifications.csv"]

    invalid = cert[
        (cert["expiry_date"].notna()) &
        (cert["expiry_date"] < cert["issue_date"])
    ]

    if len(invalid):

        add_error(
            "Certification dates incorrect"
        )

    else:

        ok("Certification dates")

        # ==========================================================
# Summary
# ==========================================================

def print_summary():

    print("\n")
    print("=" * 60)
    print("HR ANALYTICS DATA VALIDATION SUMMARY")
    print("=" * 60)

    if len(errors) == 0:

        print("\n✅ VALIDATION PASSED")
        print("\nDataset is ready for PostgreSQL import.")

    else:

        print(f"\n❌ VALIDATION FAILED ({len(errors)} errors)\n")

        for error in errors:

            print(f"- {error}")

    print("\n" + "=" * 60)


# ==========================================================
# Main
# ==========================================================

def main():

    print("\n")
    print("=" * 60)
    print("UpTime Solutions Inc.")
    print("HR Analytics Data Validator")
    print("=" * 60)

    check_files()

    check_columns()

    check_primary_keys()

    check_required_fields()

    check_duplicates()

    check_row_counts()

    check_foreign_keys()

    check_business_rules()

    print_summary()

    if len(errors) > 0:

        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":

    main()
import pandas as pd
from pathlib import Path
from faker import Faker
from datetime import date, timedelta
import random


END_DATE = date(2026,12,31)


fake = Faker()


BASE_FOLDER = Path(__file__).resolve().parent.parent

DATA_FOLDER = BASE_FOLDER / "data" / "generated"


VACANCY_COUNT = 300
CANDIDATE_COUNT = 3500


# ==========================================
# Load reference data
# ==========================================

departments = pd.read_csv(
    DATA_FOLDER / "departments.csv"
)

positions = pd.read_csv(
    DATA_FOLDER / "positions.csv"
)


employees = pd.read_csv(
    DATA_FOLDER / "employees.csv"
)


# ==========================================
# Helpers
# ==========================================

def random_date(start, end):
    delta = end - start
    return start + timedelta(
        days=random.randint(0, delta.days)
    )


# ==========================================
# Vacancies
# ==========================================

vacancies = []

for vacancy_id in range(1, VACANCY_COUNT + 1):

    position = positions.sample(1).iloc[0]


    opened_date = random_date(
        date(2023,1,1),
        date(2026,12,31)
    )


    status = random.choice(
        [
            "Open",
            "Closed"
        ]
    )


    if status == "Closed":

        closed_date = random_date(
            opened_date,
            END_DATE
        )

    else:

        closed_date = None


    vacancies.append(
        {
            "vacancy_id": vacancy_id,

            "department_id":
                position["department_id"],

            "position_id":
                position["position_id"],

            "recruiter_id":
                random.choice(
                    employees["employee_id"].tolist()
                ),

            "status": status,

            "opened_date": opened_date,

            "closed_date": closed_date
        }
    )



vacancies_df = pd.DataFrame(vacancies)


vacancies_df.to_csv(
    DATA_FOLDER / "vacancies.csv",
    index=False
)


# ==========================================
# Candidates
# ==========================================

candidates = []


for candidate_id in range(1, CANDIDATE_COUNT + 1):

    vacancy = vacancies_df.sample(1).iloc[0]


    candidates.append(
        {
            "candidate_id": candidate_id,

            "first_name":
                fake.first_name(),

            "last_name":
                fake.last_name(),

            "email":
                fake.unique.email(),

            "vacancy_id":
                vacancy["vacancy_id"],

            "application_date":
                random_date(
                    date(2023,1,1),
                    date(2026,12,31)
                )
        }
    )


candidates_df = pd.DataFrame(candidates)


candidates_df.to_csv(
    DATA_FOLDER / "candidates.csv",
    index=False
)


# ==========================================
# Offers
# ==========================================


offers = []


offer_id = 1


# приблизно 25% кандидатів отримують offer

selected_candidates = candidates_df.sample(
    frac=0.25
)


for _, candidate in selected_candidates.iterrows():

    offer_date = random_date(
        date(2023,1,1),
        date(2026,12,31)
    )


    accepted = random.choice(
        [
            True,
            False
        ]
    )


    offers.append(
        {
            "offer_id":
                offer_id,

            "candidate_id":
                candidate["candidate_id"],

            "offer_date":
                offer_date,

            "accepted":
                accepted,

            "hire_date":
                offer_date + timedelta(days=14)
                if accepted
                else None
        }
    )


    offer_id += 1



offers_df = pd.DataFrame(offers)


offers_df.to_csv(
    DATA_FOLDER / "offers.csv",
    index=False
)



print(
    "vacancies.csv:",
    len(vacancies_df)
)

print(
    "candidates.csv:",
    len(candidates_df)
)

print(
    "offers.csv:",
    len(offers_df)
)
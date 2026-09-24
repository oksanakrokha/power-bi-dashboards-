# HR Analytics Dashboard — README

**Project:** Power BI HR Analytics & Workforce Performance Dashboard  
**Client (fictional):** UpTime Solutions — Global Tech & Finance Enterprise  
**Author:** Oksana K.  
**Last updated:** September 2026  
**Data range:** January 2022 – December 2026  

---

## Overview

This Power BI dashboard was built as a portfolio project simulating a real-world enterprise BI engagement for **UpTime Solutions**. It tracks core human resources metrics including headcount dynamics, recruitment funnel efficiency, and early employee attrition patterns.

Instead of just importing flat files, the real challenge of this project was engineering a robust, **enterprise-level data pipeline**. The backend architecture connects a simulated on-premises transactional database environment directly to cloud reporting layers using automated gateway syncs.

---

## Dashboard Pages

| # | Page | Purpose |
|---|---|---|
| 1 | Workforce Overview | Total active headcount, probation tracking, overall turnover rates, and departmental metrics |
| 2 | Recruitment & Hiring | Open vacancies, hiring closure rates, average time to fill roles, and 90-day new hire retention logs |
| 3 | Attrition & Turnover | Retention rates, early attrition dynamics (< 1 year), financial cost of turnover, and departmental summaries |
| 4 | Employee Profile | Granular card view detailing individual contract types, manager routing, skills certifications, and onboarding milestones |

---

## Data Sources

The corporate HR ecosystem data is fully relational and moves through a modern data engineering pipeline:

| Source Name | Content | Type / Format |
|---|---|---|
| `python_gen_script.py` | Python script containing business logic to generate synthetic HR data | Raw Code Script |
| `ft_employee_history` | Transactional table recording hiring, status changes, and promotions | PostgreSQL Database Table |
| `ft_recruitment_pipeline`| Job opening statuses, application dates, and closing milestone data | PostgreSQL Database Table |
| `ft_employee_certifications`| Individual employee compliance, technical skills, and exam certifications | PostgreSQL Database Table |
| `dim_employees` | Core employee master data (names, contact info, job title, manager maps) | PostgreSQL Database Table |
| `dim_departments` | Organizational structure details (department names, regional business units) | PostgreSQL Database Table |
| `dim_calendar` | Standard calendar dimension supporting advanced time-intelligence | Calculated in Power BI (DAX) |

---

## Data Model

Snowflake schema. All relationships are **Many-to-One**, **single-direction**, and **active**.

**Important:** `dim_calendar` is marked as an official Date Table. The built-in Auto Date/Time Hierarchy is completely disabled. A custom, manual hierarchy (Year → Month → Date) is utilized across all time-intelligence DAX measures.

---

## Technical Pipeline Architecture

To practice real-world data infrastructure engineering, I chose a complex architecture to simulate a production-grade enterprise data flow:
1. **Data Generation:** Built a custom **Python** script to simulate 3 years of relational HR business records.
2. **On-Premises Warehousing:** Created and hosted tables inside a local **PostgreSQL** database.
3. **The Data Bridge:** Configured and deployed an **On-Premises Data Gateway** running as a local background service. This enables secure, scheduled online communication between my local machine and the cloud.
4. **Cloud Infrastructure:** Pushed data directly into **Power BI Service / Microsoft Fabric**, consolidating the tables into a single centralized **Semantic Model** to act as the single source of truth.
5. **Visualization Layer:** Connected Power BI Desktop directly to the cloud semantic model via Live Connection to author the visuals.

---

## Key Insights I Found

### 📈 Workforce & Talent Baseline
*   **Active Talent Volume:** The organization maintains a robust core of **445 active employees** out of a total historic pool of 498, with **60 individuals** successfully navigating their probation periods (+22.45% YoY growth).
*   **Tenure Health:** The average employee tenure stands solid at **3 years and 8 months**, which is improving slightly (+5 months YoY), indicating long-term stability in mature teams.

### 📈 Recruitment & Sourcing Pipeline
*   **Healthy Sourcing Pools:** The talent acquisition engine maintains a strong candidate volume, averaging **21 candidates per vacancy** (+9.01% YoY).
*   **Hiring Bottlenecks:** Despite a strong initial pool, the overall **Average Time to Fill sits at 88 days**. Severe operational delays are visible within **Sales (113 days)** and **Finance (105 days)**, drastically dragging down corporate agility.

### 📉 Attrition Risks & Financial Friction
*   **Finance Department Red Flags:** While the macro turnover rate remains stable at **5.03%**, the **Finance department leads attrition at 6.7%** — which tracks significantly above the baseline. This requires immediate escalation to HR Business Partners (HRBPs).
*   **Onboarding Failure Points:** Critical friction exists during initial employee lifecycle stages—**42.86% of total company terminations happen within the first year** of tenure. 
*   **Cost of Turnover:** Early exits are accelerating, and these onboarding breakdowns caused the company **\$78.50K** in pure turnover costs during the current calendar year.
*   **90-Day Drop Concentration** | A massive **57%** of all employee terminations occur within the very first 0–1 year tenure bracket, indicating a critical need to re-evaluate early-stage onboarding structure.

---

## Known Data Issues & Constraints

| Issue | Description |
|-----|---|
| **Synthetic Records Only** | All business metrics, emails, names, and other personnel maps are entirely artificial. Any matches to real world entities are coincidental. |
| **AI-Generated Avatars** | Employee photos are sourced via **UI Faces** and consist entirely of human AI avatars. They do not belong to real people, leaving the portfolio 100% compliant with privacy laws (GDPR). |


---

## Live Report

👉 **[Сlick here to open the interactive dashboard]([https://powerbi.com](https://app.powerbi.com/view?r=eyJrIjoiZDExZTljMDEtNjg4Ny00MzM5LWE0NTQtNDcyNTdlMjI2ZDA1IiwidCI6ImU3MWY3MGE4LTkzMTAtNGZkNi04MzA5LTY1M2NhZDU2ZTJkNiJ9&pageName=b37f93a0af04d96d900e)** *(The report opens directly in your browser, is fully interactive, and requires no Power BI licenses or sign-ins).*

📸 **Screenshots of all dashboard pages**

### 1. Workforce Overview
<img width="12000" height="6813" alt="1  Workforce overview" src="https://github.com/user-attachments/assets/bfa3db89-bb70-488c-971d-463d4028c643" />
   
### 2. Recruitment & Hiring
<img width="12000" height="6813" alt="2  Recruitment" src="https://github.com/user-attachments/assets/6c5c851d-5d04-43c2-851d-577acab45bcc" />
  
### 3. Attrition & Turnover
<img width="12000" height="6813" alt="3  Attrition" src="https://github.com/user-attachments/assets/cff95f12-e29f-4d22-9601-5deebf78e762" />

### 4. Employee Profile
<img width="3000" height="2037" alt="Employee Profile" src="https://github.com/user-attachments/assets/b7edd10a-4f34-47c2-9a40-35780386ee78" />





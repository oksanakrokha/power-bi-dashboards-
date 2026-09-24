# HR Analytics Dashboard — README

**Project:** Power BI HR Analytics & Workforce Performance Dashboard  
**Client (fictional):** Global Tech Enterprise  
**Author:** Oksana K.  
**Last updated:** September 2026  
**Data range:** January 2022 – December 2026  

---

## Overview

This Power BI dashboard was built as a portfolio project simulating a real-world enterprise BI engagement for fictional company. It tracks core human resources metrics including headcount dynamics, recruitment funnel efficiency, and early employee attrition patterns.

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

💡 *Portfolio Note: For cloud security reasons, anonymous web embedding is restricted for active Live Fabric capacities. Therefore, this specific public **interactive version** has been converted into a **Import Mode model**, maintaining 100% of the original data structure.*

---

## Key Insights 

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

## Privacy & Fake Data Disclaimer (GDPR-Safe)

| Issue | Description |
|-----|---|
| **Synthetic Records Only** | All business metrics, emails, names, and other personnel maps are entirely artificial. Any matches to real world entities are coincidental. |
| **AI-Generated Avatars** | Employee photos are sourced via **UI Faces** and consist entirely of human AI avatars. They do not belong to real people, leaving the portfolio 100% compliant with privacy laws (GDPR). |


---

## Live Report

👉 **[Сlick here to open the interactive dashboard](https://app.powerbi.com/view?r=eyJrIjoiZDExZTljMDEtNjg4Ny00MzM5LWE0NTQtNDcyNTdlMjI2ZDA1IiwidCI6ImU3MWY3MGE4LTkzMTAtNGZkNi04MzA5LTY1M2NhZDU2ZTJkNiJ9&pageName=b37f93a0af04d96d900e)** *(The report opens directly in your browser, is fully interactive, and requires no Power BI licenses or sign-ins).*

📸 **Screenshots of all dashboard pages**

### 1. Workforce Overview
<img width="12000" height="6813" alt="HR Analytics_Dashboard _ FinalV_Grey-images-0" src="https://github.com/user-attachments/assets/bb27da83-168f-43ba-b115-84e40562ce18" />
   
### 2. Recruitment & Hiring
<img width="12000" height="6813" alt="HR Analytics_Dashboard _ FinalV_Grey-images-1" src="https://github.com/user-attachments/assets/1afe069b-1ff2-4b65-bdbb-3cfdea659810" />
  
### 3. Attrition & Turnover
<img width="12000" height="6813" alt="HR Analytics_Dashboard _ FinalV_Grey-images-2" src="https://github.com/user-attachments/assets/a5f5a6b2-bbd3-4fb5-bfc1-8398ed9779c6" />

### 4. Employee Profile
<img width="3000" height="2037" alt="HR Analytics_Dashboard _FinalVEmployeeProfile_Grey" src="https://github.com/user-attachments/assets/f000b02b-de1f-49f4-bb54-667517aca01a" />






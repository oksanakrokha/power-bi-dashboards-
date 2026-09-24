# UpTime Retail Sales Dashboard — README

**Project:** Power BI Sales Performance Dashboard  
**Client (fictional):** UpTime Sportswear — multi-store retail chain  
**Author:** Oksana K.  
**Last updated:** September 2026  
**Data range:** January 2022 – September 30, 2024  

---

## Overview

This Power BI dashboard was built as a portfolio project simulating a real BI engagement for **UpTime Company**, a Canadian sportswear retailer carrying Nike, Adidas, Puma, and Reebok across **12 stores in 3 cities** (Calgary, Edmonton, Red Deer).

The dataset is synthetic and covers **January 2022 through September 30, 2024** — a deliberate cutoff that shaped the time-intelligence architecture: custom period comparisons (2023, 2024, Last 6 months, Last 3 months, Last 1 month) instead of rolling YTD-only logic.

---

## Dashboard Pages

| # | Page | Purpose |
|---|------|---------|
| 1 | Executive Summary | High-level KPIs, Profit Bridge, store performance alerts |
| 2 | Sales Analysis | Brand dynamics, YoY variance, conversion rate trends |
| 3 | Store & Profitability | Plan vs. actual by store, financial summary by city |
| 4 | Customer Analysis | Retention, purchase frequency, demographics, channel mix |
| 5 | Category/SKU Performance | Brand × category matrix, inventory health, stock status |

---

## Data Sources

All source data is stored in **Excel (.xlsx) and CSV files** that must be loaded into Power BI via Power Query:

| File / Source | Content | Format |
|---|---|---|
| `ftActualSales` | Transaction-level sales records | Excel / CSV |
| `ftCostOfSales` | Cost of goods sold | Excel |
| `ftForecastOfSales` | Planned sales targets | Excel |
| `ftOperationalCost` | Store operating expenses | Excel |
| `ftSupplier` | Purchase / receiving records | Excel |
| `tClientsAttandance` | Foot traffic (visitors) | Excel |
| `dmStores` | Store master (name, city, ID) | Excel / CSV |
| `dmItems` | Product master (brand, category, SKU) | Excel |
| `dmClients` | Customer master | Excel |
| `dmDataTable` | Calendar / Date dimension | Calculated in Power BI |


---

## Data Model

Star schema. All relationships are **Many-to-One**, **single-direction**, **active**.

```
ftActualSales ──► dmDataTable  (Date)
ftActualSales ──► dmStores     (StoreName)
ftActualSales ──► dmItems      (ItemID)
ftActualSales ──► dmClients    (ClientID)
ftCostOfSales ──► dmDataTable  (Date)
ftCostOfSales ──► dmStores     (StoreName)
ftForecastOfSales ──► dmDataTable (Date)
ftForecastOfSales ──► dmStores    (StoreName)
ftOperationalCost ──► dmDataTable (Date)
ftOperationalCost ──► dmStores    (StoreID)
```

**Important:** `dmDataTable` is marked as a Date Table. The built-in Auto Date Hierarchy is disabled. A manual Year → MonthNumber → Date hierarchy is used instead.

---

## Key Design Decisions

### Custom Period Architecture
Because data ends on **September 30, 2024**, standard YTD functions would be misleading. A disconnected `TimePeriods` table drives all period selection:
- 2023 (full year)
- 2024 (Jan–Sep)
- Last 6 months (Apr–Sep 2024)
- Last 3 months (Jul–Sep 2024)
- Last 1 month (Sep 2024)

All `_CP` (Current Period) measures use `DATESBETWEEN` + `REMOVEFILTERS('dmDataTable'[Date])`.

## Known Data Issues

| Issue | Description |
|---|---|
| Red Deer — missing OpEx | Operational expenses for Red Deer stores are not in the source data; costs appear attributed to Calgary |
| Inventory sell-through > 100% | Caused by timing mismatches between purchase and sales records |
| Unknown Customers | ~74% of transactions have no registered customer ID |
| Red Deer profit distortion | Absent OpEx inflates Red Deer's apparent profitability vs. Calgary |

---
## Files in This Repository

👉 **[Сlick here to open the interactive dashboard `Sales_Dashboard.pbix`](https://app.powerbi.com/view?r=eyJrIjoiNTZlMjc2NzEtNmUwYS00ZGQyLWI3NzYtYmE4ZWFmYmVlOTE3IiwidCI6ImU3MWY3MGE4LTkzMTAtNGZkNi04MzA5LTY1M2NhZDU2ZTJkNiJ9&pageName=d9888bfb9075ec439060)** *(The report opens directly in your browser, is fully interactive, and requires no Power BI licenses or sign-ins).*

📸 **Screenshots of all dashboard pages**

   ### 1. Executive Summary
<img width="3300" height="2550" alt="1  Executive Summary" src="https://github.com/user-attachments/assets/ed308b1f-501f-4c29-8a79-c018384558e9" />

   ### 2. Sales Analysis
<img width="3300" height="2550" alt="2  Sales Analysis" src="https://github.com/user-attachments/assets/7a6f285f-98d5-4c12-aa35-092c17dc12ee" />

  ### 3. Store & Profitability
  <img width="3300" height="2550" alt="3  Store   Profitability" src="https://github.com/user-attachments/assets/ebca76d8-2d48-4351-a05a-e7d7739c0208" />

  ### 4. Customer Analysis
<img width="3300" height="2550" alt="4  Customer Analysis" src="https://github.com/user-attachments/assets/23fa4803-2c13-4c4d-9323-a2f3b6a7379d" />

  ### 5. Category/SKU Performance
  <img width="3300" height="2550" alt="5  CategorySKU Performance" src="https://github.com/user-attachments/assets/0ba407ff-8293-484f-8bd8-31adaafe442d" />



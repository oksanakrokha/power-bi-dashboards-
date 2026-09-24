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

| File | |
|---|---|
| `Sales_Dashboard.pbix` |👉 **[Сlick here to open the interactive dashboard](https://app.powerbi.com/view?r=eyJrIjoiNTZlMjc2NzEtNmUwYS00ZGQyLWI3NzYtYmE4ZWFmYmVlOTE3IiwidCI6ImU3MWY3MGE4LTkzMTAtNGZkNi04MzA5LTY1M2NhZDU2ZTJkNiJ9&pageName=d9888bfb9075ec439060)**  
*(The report opens directly in your browser, is fully interactive, and requires no Power BI licenses or sign-ins).*|
| `Sales Dashboard Preview.pdf` |![Dashboard Preview](https://github.com/oksanakrokha/power-bi-dashboards-/blob/f5344fc022bccc0a4f8482881c7bd78ed5713e27/retail-sales/Sales%20Dashboard%20Preview.pdf)|

| `Dataset folder` |
| `README.md` | 

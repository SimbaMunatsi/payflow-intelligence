# 06. Warehouse Design

## Warehouse Layers
- Raw: Source data as received
- Landing: Minimal transformations and staging
- Staging: Cleaned and validated records
- Warehouse: Curated analytical tables

## Suggested Tables
- fact_transactions
- dim_accounts
- dim_dates

## Design Principles
- Separation of concerns
- Traceability
- Performance optimization

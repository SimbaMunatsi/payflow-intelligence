# 05. Business Rules

## Validation Rules
- Transactions must include a valid transaction_id
- Amount must be numeric and non-negative
- Currency must be a supported code
- Status must be one of the defined values

## Transformation Rules
- Standardize dates to a common format
- Normalize currency values where needed
- Aggregate transactions by business period

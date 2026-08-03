import pandas as pd

from src.validation.business.settlement_lag import (
    SettlementLagRule,
)


def main():

    transactions = pd.DataFrame(
        {
            "txn_ref": ["TXN001"],
            "authorised_at": ["2026-03-02"],   # Monday
        }
    )

    switch_log = pd.DataFrame(
        {
            "txn_ref": ["TXN001"],
            "rail_reference": ["RR001"],
        }
    )

    settlements = pd.DataFrame(
        {
            "rail_reference": ["RR001"],
            "rail": ["ECOCASH_MM"],
            "value_date": ["2026-03-04"],      # Tuesday (T+1)
        }
    )

    datasets = {
        "transactions": transactions,
        "switch_log": switch_log,
    }

    rule = SettlementLagRule(
        "settlements"
    )

    result = rule.execute(
        settlements,
        datasets,
    )

    print(result)
    print()
    print(result.to_dict())


if __name__ == "__main__":
    main()
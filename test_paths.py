import pandas as pd

from src.validation.business.rail_charges import (
    RailChargesRule,
)


def main():

    settlements = pd.DataFrame(
        {
            "rail": [
                "ECOCASH_MM",
                "ZIPIT_BANK",
                "RTGS_BANK",
            ],

            "gross_amount": [
                1000,
                1000,
                1000,
            ],

            "rail_charges": [
                12.50,
                8.00,
                10.00,
            ],
        }
    )

    rule = RailChargesRule(
        "settlements"
    )

    result = rule.execute(
        settlements
    )

    print(result)

    print()

    print(result.to_dict())


if __name__ == "__main__":
    main()
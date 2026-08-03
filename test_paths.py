import pandas as pd

from src.validation.business.net_amount import (
    NetAmountRule,
)


def main():

    settlements = pd.DataFrame(
        {
            "gross_amount": [
                100,
                200,
            ],

            "rail_charges": [
                5,
                10,
            ],

            "net_amount": [
                95,
                180,
            ],
        }
    )

    rule = NetAmountRule(
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
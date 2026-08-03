"""
Schema Registry.

Central metadata repository describing every dataset
processed by the PayFlow Intelligence Platform.

The registry is intentionally metadata-driven so that
transformation, validation and warehousing logic can
consume configuration instead of hard-coded rules.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

METADATA_REGISTRY = {

    # ======================================================
    # TRANSACTIONS
    # ======================================================

    "transactions": {

        "required": [
            "txn_ref",
            "merchant_id",
            "rail",
            "currency",
            "amount",
            "status",
            "initiated_at",
        ],

        "datetime": [
            "initiated_at",
            "authorised_at",
            "updated_at",
        ],

        "numeric": [
            "amount",
            "rail_latency_ms",
        ],

        "integer": [
            "attempt_count",
        ],

        "uppercase": [
            "currency",
            "rail",
            "status",
            "error_code",
            "final_response_code",
        ],

        "categorical": {

            "status": {

                "SUCCESS": [
                    "SUCCESS",
                    "SUCCEEDED",
                    "APPROVED",
                    "OK",
                    "COMPLETED",
                ],

                "FAILED": [
                    "FAILED",
                    "FAIL",
                    "DECLINED",
                    "ERROR",
                    "REJECTED",
                ],

                "PENDING": [
                    "PENDING",
                    "PROCESSING",
                    "IN_PROGRESS",
                ],

            }

        }

    },

    # ======================================================
    # SWITCH LOG
    # ======================================================

    "switch_log": {

        "required": [
            "switch_ref",
            "txn_ref",
            "rail",
            "attempt_no",
            "submitted_at",
        ],

        "datetime": [
            "submitted_at",
            "responded_at",
        ],

        "integer": [
            "attempt_no",
        ],

        "uppercase": [
            "rail",
            "rail_response_code",
        ],

        "categorical": {}

    },

    # ======================================================
    # SETTLEMENTS
    # ======================================================

    "settlements": {

        "required": [
            "settlement_batch_id",
            "merchant_id",
            "rail",
            "value_date",
            "gross_amount",
            "net_amount",
            "line_type",
        ],

        "datetime": [
            "value_date",
        ],

        "numeric": [
            "gross_amount",
            "rail_charges",
            "net_amount",
        ],

        "uppercase": [
            "currency",
            "rail",
            "line_type",
        ],

        "categorical": {

            "line_type": {

                "PAYMENT": [
                    "PAYMENT",
                ],

                "REVERSAL": [
                    "REVERSAL",
                    "REVERSE",
                ]

            }

        }

    },

    # ======================================================
    # MERCHANTS
    # ======================================================

    "merchants": {

        "required": [
            "merchant_id",
            "merchant_name",
            "currency",
            "fee_basis",
            "effective_from",
        ],

        "datetime": [
            "effective_from",
            "effective_to",
        ],

        "numeric": [
            "rate_percent",
            "flat_fee",
            "min_fee",
            "cap_fee",
            "tier_rate_percent",
        ],

        "integer": [
            "tier_threshold_count",
        ],

        "uppercase": [
            "currency",
            "fee_basis",
        ],

        "categorical": {}

    },

    # ======================================================
    # TICKETS
    # ======================================================

    "tickets": {

        "required": [
            "ticket_id",
            "merchant_id",
            "opened_at",
            "channel",
            "status",
        ],

        "datetime": [
            "opened_at",
        ],

        "uppercase": [
            "status",
            "channel",
        ],

        "categorical": {

            "status": {

                "OPEN": [
                    "OPEN",
                    "NEW",
                ],

                "IN_PROGRESS": [
                    "IN_PROGRESS",
                    "PENDING",
                    "WORKING",
                ],

                "CLOSED": [
                    "CLOSED",
                    "RESOLVED",
                    "DONE",
                ]

            }

        }

    },

}

# ==========================================================
# GLOBAL PLATFORM METADATA
# ==========================================================

GLOBAL_STANDARDIZATION = {

    "boolean_true": [
        "TRUE",
        "YES",
        "Y",
        "1",
    ],

    "boolean_false": [
        "FALSE",
        "NO",
        "N",
        "0",
    ],

    "supported_currencies": [
        "USD",
        "ZWG",
        "ZWL",
    ],

    "supported_rails": [

        "ECOCASH_MM",

        "ONEMONEY_MM",

        "INNBUCKS_MM",

        "ZIPIT_BANK",

        "RTGS_BANK",

        "VISA_CARD",

        "MASTERCARD_CARD",

    ]

}
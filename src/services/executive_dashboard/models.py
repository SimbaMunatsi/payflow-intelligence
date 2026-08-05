"""
Executive Dashboard Models.

Models used by the Executive Operations Dashboard.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

from dataclasses import dataclass, field


# =====================================================
# KPI Models
# =====================================================

@dataclass
class ExecutiveKPIs:
    """
    Executive operational KPIs.
    """

    total_transactions: int

    success_rate: float

    settlement_rate: float

    total_volume_usd: float

    total_volume_zwg: float

    average_settlement_lag: float

    open_support_tickets: int

    def to_dict(self):

        return {

            "total_transactions":
                self.total_transactions,

            "success_rate":
                round(self.success_rate, 2),

            "settlement_rate":
                round(self.settlement_rate, 2),

            "total_volume_usd":
                round(self.total_volume_usd, 2),

            "total_volume_zwg":
                round(self.total_volume_zwg, 2),

            "average_settlement_lag":
                round(self.average_settlement_lag, 2),

            "open_support_tickets":
                self.open_support_tickets,

        }


# =====================================================
# Chart Model
# =====================================================

@dataclass
class ChartData:
    """
    Single business chart.
    """

    title: str

    labels: list[str]

    values: list[float]

    chart_type: str

    def to_dict(self):

        return {

            "title": self.title,

            "labels": self.labels,

            "values": self.values,

            "chart_type": self.chart_type,

        }


# =====================================================
# Dashboard Model
# =====================================================

@dataclass
class ExecutiveDashboard:
    """
    Executive Operations Dashboard.
    """

    kpis: ExecutiveKPIs

    charts: list[ChartData] = field(
        default_factory=list
    )

    def to_dict(self):

        return {

            "kpis":
                self.kpis.to_dict(),

            "charts": [

                chart.to_dict()

                for chart in self.charts

            ],

        }
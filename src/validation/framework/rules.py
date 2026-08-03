"""
Validation rule framework.

Defines the base contract that every validation rule
must follow.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

from abc import ABC, abstractmethod
from time import perf_counter

import pandas as pd

from src.validation.framework.results import ValidationResult


class ValidationRule(ABC):
    """
    Base class for all validation rules.
    """

    def __init__(self, dataset_name: str):
        self.dataset_name = dataset_name

    @property
    @abstractmethod
    def rule_name(self) -> str:
        """
        Human-readable rule name.
        """
        pass

    @property
    def severity(self) -> str:
        """
        Default severity.
        """
        return "ERROR"

    @abstractmethod
    def validate(
        self,
        dataframe: pd.DataFrame,
        datasets: dict[str, pd.DataFrame] | None = None,
    ) -> ValidationResult:
        """
        Validation logic implemented by subclasses.
        """
        pass

    def execute(
        self,
        dataframe: pd.DataFrame,
        datasets: dict[str, pd.DataFrame] | None = None,
    ) -> ValidationResult:
        """
        Executes the rule while measuring execution time.
        """

        start = perf_counter()

        result = self.validate(
            dataframe,
            datasets,
        )

        result.execution_time_ms = (
            perf_counter() - start
        ) * 1000

        return result
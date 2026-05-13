# app/models/payroll_run.py

from dataclasses import dataclass
from datetime import datetime


@dataclass
class PayrollRun:
    """
    Represents a completed payroll run.

    Example:
        May 2024 payroll
    """

    id: int

    payroll_month: int
    # Example: 5 for May

    payroll_year: int
    # Example: 2024

    total_payroll_amount: float
    # Total amount paid to all employees

    status: str
    # Example:
    # "draft"
    # "approved"
    # "paid"

    created_at: datetime
    # When payroll run was created
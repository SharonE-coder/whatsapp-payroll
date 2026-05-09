# app/models/compensation.py

from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Compensation:
    """
    Represents an employee's salary at a specific period.

    We DO NOT overwrite salary.
    Instead, we create new records when salary changes.
    This preserves history and allows accurate payroll calculation.
    """

    id: int  # Unique identifier

    employee_id: int  # Links to Employee

    base_salary: float  # Monthly salary amount

    effective_from: date
    # Date this salary becomes active

    effective_to: Optional[date] = None
    # When this salary stops being active
    # None = still active

    change_type: Optional[str] = None
    # 'increase' or 'decrease'

    change_mode: Optional[str] = None
    # 'percentage' or 'fixed'

    change_value: Optional[float] = None
    # e.g. 10 (%) or 20000 (₦)

    created_at: Optional[date] = None
    # When this record was created
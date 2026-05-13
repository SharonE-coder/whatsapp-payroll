from dataclasses import dataclass
from datetime import date


@dataclass
class Adjustment:
    """
    Represents a one-time payroll adjustment.

    Examples:
    - Bonus
    - Commission
    - Deduction
    - Penalty
    """

    id: int

    employee_id: int

    amount: float
    # Positive amount only

    adjustment_type: str
    # "bonus" or "deduction"

    description: str
    # Human-readable explanation

    effective_date: date
    # When adjustment should apply

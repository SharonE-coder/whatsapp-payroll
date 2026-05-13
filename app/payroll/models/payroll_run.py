from dataclasses import dataclass
from datetime import datetime
from app.payroll.state_machine.payroll_states import (
    PayrollState,
)


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

    status: PayrollState
    # Example:
    # "draft"
    # "approved"
    # "paid"

    created_at: datetime
    # When payroll run was created
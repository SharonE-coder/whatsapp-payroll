from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Employee:
    """
    Represents a single staff member in the system.

    This model only stores basic employee information.
    Salary and payroll calculations will be handled separately.
    """

    id: int  # Unique identifier for the employee

    full_name: str  # Employee's full name

    phone_number: str  # Used for WhatsApp or SMS communication

    bank_name: str  # Name of employee's bank

    account_number: str  # Bank account number for salary payment

    start_date: Optional[date] = None
    # When the employee started working
    # Optional because some businesses may not know exact start date

    is_active: bool = True
    # True → employee is active
    # False → employee has left or is inactive

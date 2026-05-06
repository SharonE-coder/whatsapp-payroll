# tests/test_employee.py

from datetime import date
from app.models.employee import Employee


def test_create_employee():
    """
    Simple test to confirm Employee model works correctly
    """

    emp = Employee(
        id=1,
        full_name="John Doe",
        phone_number="08012345678",
        bank_name="GTBank",
        account_number="1234567890",
        start_date=date(2024, 1, 1)
    )

    # Check values
    assert emp.full_name == "John Doe"
    assert emp.is_active is True
# tests/test_payroll_service.py

from datetime import date

from app.models.employee import Employee
from app.models.compensation import Compensation

from app.repositories.employee_repository import EmployeeRepository
from app.repositories.compensation_repository import (
    CompensationRepository,
)

from app.services.payroll_service import PayrollService


def test_calculate_monthly_salary():
    """
    Test payroll salary calculation
    """

    employee_repository = EmployeeRepository()

    compensation_repository = CompensationRepository()

    payroll_service = PayrollService(
        employee_repository=employee_repository,
        compensation_repository=compensation_repository,
    )

    employee = Employee(
        id=1,
        full_name="John Doe",
        phone_number="08012345678",
        bank_name="GTBank",
        account_number="1234567890",
    )

    compensation = Compensation(
        id=1,
        employee_id=1,
        base_salary=150000,
        effective_from=date(2024, 1, 1),
    )

    employee_repository.add_employee(employee)

    compensation_repository.add_compensation(compensation)

    salary = payroll_service.calculate_monthly_salary(
        employee_id=1,
        payroll_date=date(2024, 5, 1),
    )

    assert salary == 150000
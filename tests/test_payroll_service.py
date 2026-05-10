from datetime import date

from app.models.employee import Employee
from app.models.compensation import Compensation
from app.models.adjustment import Adjustment

from app.repositories.employee_repository import EmployeeRepository
from app.repositories.compensation_repository import (
    CompensationRepository,
)

from app.repositories.adjustment_repository import (
    AdjustmentRepository,
)

from app.services.payroll_service import PayrollService

def test_apply_adjustments():
    """
    Test salary bonuses and deductions
    """

    employee_repository = EmployeeRepository()

    compensation_repository = CompensationRepository()

    adjustment_repository = AdjustmentRepository()

    payroll_service = PayrollService(
        employee_repository=employee_repository,
        compensation_repository=compensation_repository,
        adjustment_repository=adjustment_repository,
    )

    # Create bonus adjustment
    bonus = Adjustment(
        id=1,
        employee_id=1,
        amount=20000,
        adjustment_type="bonus",
        description="Performance bonus",
        effective_date=date(2024, 5, 1),
    )

    # Create deduction adjustment
    deduction = Adjustment(
        id=2,
        employee_id=1,
        amount=5000,
        adjustment_type="deduction",
        description="Penalty deduction",
        effective_date=date(2024, 5, 1),
    )

    # Store adjustments
    adjustment_repository.add_adjustment(bonus)

    adjustment_repository.add_adjustment(deduction)

    # Apply adjustments to base salary
    final_salary = payroll_service.apply_adjustments(
        employee_id=1,
        payroll_date=date(2024, 5, 1),
        base_salary=150000,
    )

    # Expected:
    # 150k + 20k - 5k = 165k
    assert final_salary == 165000

def test_run_payroll():
    """
    Test full payroll run
    """

    employee_repository = EmployeeRepository()

    compensation_repository = CompensationRepository()

    adjustment_repository = AdjustmentRepository()

    payroll_service = PayrollService(
        employee_repository=employee_repository,
        compensation_repository=compensation_repository,
        adjustment_repository=adjustment_repository,
    )

    # Employee 1
    employee_1 = Employee(
        id=1,
        full_name="John Doe",
        phone_number="08012345678",
        bank_name="GTBank",
        account_number="1234567890",
    )

    compensation_1 = Compensation(
        id=1,
        employee_id=1,
        base_salary=150000,
        effective_from=date(2024, 1, 1),
    )

    # Employee 2
    employee_2 = Employee(
        id=2,
        full_name="Jane Smith",
        phone_number="08087654321",
        bank_name="Access Bank",
        account_number="0987654321",
    )

    compensation_2 = Compensation(
        id=2,
        employee_id=2,
        base_salary=100000,
        effective_from=date(2024, 1, 1),
    )

    employee_repository.add_employee(employee_1)
    employee_repository.add_employee(employee_2)

    compensation_repository.add_compensation(
        compensation_1
    )

    compensation_repository.add_compensation(
        compensation_2
    )

    payroll_result = payroll_service.run_payroll(
        payroll_date=date(2024, 5, 1),
    )

    assert len(payroll_result["employees"]) == 2

    assert payroll_result[
        "total_payroll_amount"
    ] == 250000
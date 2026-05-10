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
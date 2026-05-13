import pytest

from datetime import date
from datetime import datetime

from app.payroll.models.payroll_run import PayrollRun
from app.payroll.models.employee import Employee
from app.payroll.models.compensation import Compensation
from app.payroll.models.adjustment import Adjustment

from app.payroll.repositories.employee_repository import (
    EmployeeRepository,
)

from app.payroll.repositories.compensation_repository import (
    CompensationRepository,
)

from app.payroll.repositories.adjustment_repository import (
    AdjustmentRepository,
)

from app.payroll.repositories.payroll_run_repository import (
    PayrollRunRepository,
)

from app.payroll.repositories.payroll_run_item_repository import (
    PayrollRunItemRepository,
)

from app.payroll.services.payroll_service import (
    PayrollService,
)


def test_apply_adjustments():
    """
    Test salary bonuses and deductions
    """

    employee_repository = EmployeeRepository()

    compensation_repository = (
        CompensationRepository()
    )

    adjustment_repository = (
        AdjustmentRepository()
    )

    payroll_run_repository = (
        PayrollRunRepository()
    )

    payroll_run_item_repository = (
        PayrollRunItemRepository()
    )

    payroll_service = PayrollService(
        employee_repository=employee_repository,
        compensation_repository=(
            compensation_repository
        ),
        adjustment_repository=(
            adjustment_repository
        ),
        payroll_run_repository=(
            payroll_run_repository
        ),
        payroll_run_item_repository=(
            payroll_run_item_repository
        ),
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

    adjustment_repository.add_adjustment(
        bonus
    )

    adjustment_repository.add_adjustment(
        deduction
    )

    final_salary = (
        payroll_service.apply_adjustments(
            employee_id=1,
            payroll_date=date(2024, 5, 1),
            base_salary=150000,
        )
    )

    # 150k + 20k - 5k
    assert final_salary == 165000


def test_run_payroll():
    """
    Test full payroll run
    """

    employee_repository = EmployeeRepository()

    compensation_repository = (
        CompensationRepository()
    )

    adjustment_repository = (
        AdjustmentRepository()
    )

    payroll_run_repository = (
        PayrollRunRepository()
    )

    payroll_run_item_repository = (
        PayrollRunItemRepository()
    )

    payroll_service = PayrollService(
        employee_repository=employee_repository,
        compensation_repository=(
            compensation_repository
        ),
        adjustment_repository=(
            adjustment_repository
        ),
        payroll_run_repository=(
            payroll_run_repository
        ),
        payroll_run_item_repository=(
            payroll_run_item_repository
        ),
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

    employee_repository.add_employee(
        employee_1
    )

    employee_repository.add_employee(
        employee_2
    )

    compensation_repository.add_compensation(
        compensation_1
    )

    compensation_repository.add_compensation(
        compensation_2
    )

    payroll_result = (
        payroll_service.run_payroll(
            payroll_date=date(2024, 5, 1),
        )
    )

    assert (
        len(payroll_result["employees"])
        == 2
    )

    assert (
        payroll_result[
            "total_payroll_amount"
        ]
        == 250000
    )


def test_prevent_duplicate_payroll_run():
    """
    Test preventing duplicate payroll runs
    """

    employee_repository = EmployeeRepository()

    compensation_repository = (
        CompensationRepository()
    )

    adjustment_repository = (
        AdjustmentRepository()
    )

    payroll_run_repository = (
        PayrollRunRepository()
    )

    payroll_run_item_repository = (
        PayrollRunItemRepository()
    )

    payroll_service = PayrollService(
        employee_repository=employee_repository,
        compensation_repository=(
            compensation_repository
        ),
        adjustment_repository=(
            adjustment_repository
        ),
        payroll_run_repository=(
            payroll_run_repository
        ),
        payroll_run_item_repository=(
            payroll_run_item_repository
        ),
    )

    existing_payroll = PayrollRun(
        id=1,
        payroll_month=5,
        payroll_year=2024,
        total_payroll_amount=250000,
        status="paid",
        created_at=datetime.now(),
    )

    payroll_run_repository.add_payroll_run(
        existing_payroll
    )

    with pytest.raises(ValueError):

        payroll_service.run_payroll(
            payroll_date=date(2024, 5, 1),
        )


def test_payroll_run_is_saved():
    """
    Test payroll run gets saved
    """

    employee_repository = EmployeeRepository()

    compensation_repository = (
        CompensationRepository()
    )

    adjustment_repository = (
        AdjustmentRepository()
    )

    payroll_run_repository = (
        PayrollRunRepository()
    )

    payroll_run_item_repository = (
        PayrollRunItemRepository()
    )

    payroll_service = PayrollService(
        employee_repository=employee_repository,
        compensation_repository=(
            compensation_repository
        ),
        adjustment_repository=(
            adjustment_repository
        ),
        payroll_run_repository=(
            payroll_run_repository
        ),
        payroll_run_item_repository=(
            payroll_run_item_repository
        ),
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

    employee_repository.add_employee(
        employee
    )

    compensation_repository.add_compensation(
        compensation
    )

    payroll_service.run_payroll(
        payroll_date=date(2024, 5, 1),
    )

    saved_payroll = (
        payroll_run_repository
        .get_payroll_run(
            payroll_month=5,
            payroll_year=2024,
        )
    )

    assert saved_payroll is not None

    assert (
        saved_payroll.total_payroll_amount
        == 150000
    )

    assert (
        saved_payroll.status
        == "draft"
    )


def test_payroll_run_items_are_saved():
    """
    Test payroll employee snapshots are saved
    """

    employee_repository = EmployeeRepository()

    compensation_repository = (
        CompensationRepository()
    )

    adjustment_repository = (
        AdjustmentRepository()
    )

    payroll_run_repository = (
        PayrollRunRepository()
    )

    payroll_run_item_repository = (
        PayrollRunItemRepository()
    )

    payroll_service = PayrollService(
        employee_repository=employee_repository,
        compensation_repository=(
            compensation_repository
        ),
        adjustment_repository=(
            adjustment_repository
        ),
        payroll_run_repository=(
            payroll_run_repository
        ),
        payroll_run_item_repository=(
            payroll_run_item_repository
        ),
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

    employee_repository.add_employee(
        employee
    )

    compensation_repository.add_compensation(
        compensation
    )

    payroll_service.run_payroll(
        payroll_date=date(2024, 5, 1),
    )

    payroll_items = (
        payroll_run_item_repository
        .get_payroll_run_items(
            payroll_run_id=1
        )
    )

    assert len(payroll_items) == 1

    assert (
        payroll_items[0].employee_name
        == "John Doe"
    )

    assert (
        payroll_items[0].final_salary
        == 150000
    )
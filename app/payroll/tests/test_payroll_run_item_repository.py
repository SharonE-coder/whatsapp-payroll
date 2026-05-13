from app.payroll.models.payroll_run_item import (
    PayrollRunItem,
)

from app.payroll.repositories.payroll_run_item_repository import (
    PayrollRunItemRepository,
)


def test_add_payroll_run_item():
    """
    Test storing payroll run item
    """

    repository = (
        PayrollRunItemRepository()
    )

    payroll_run_item = PayrollRunItem(
        id=1,
        payroll_run_id=1,
        employee_id=1,
        employee_name="John Doe",
        base_salary=150000,
        final_salary=165000,
    )

    repository.add_payroll_run_item(
        payroll_run_item
    )

    items = repository.get_payroll_run_items(
        payroll_run_id=1
    )

    assert len(items) == 1

    assert items[0].employee_name == "John Doe"

    assert items[0].final_salary == 165000
from app.models.payroll_run_item import (
    PayrollRunItem,
)


class PayrollRunItemRepository:
    """
    Stores payroll run employee records
    """

    def __init__(self):

        self.payroll_run_items = []

    def add_payroll_run_item(
        self,
        payroll_run_item: PayrollRunItem,
    ) -> None:
        """
        Store payroll run item
        """

        self.payroll_run_items.append(
            payroll_run_item
        )

    def get_payroll_run_items(
        self,
        payroll_run_id: int,
    ) -> list[PayrollRunItem]:
        """
        Get all employees inside payroll run
        """

        return [
            payroll_run_item
            for payroll_run_item
            in self.payroll_run_items
            if (
                payroll_run_item.payroll_run_id
                == payroll_run_id
            )
        ]
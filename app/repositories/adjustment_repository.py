from datetime import date

from app.models.adjustment import Adjustment


class AdjustmentRepository:
    """
    Stores and retrieves payroll adjustments
    """

    def __init__(self):
        self.adjustments = []

    def add_adjustment(
        self,
        adjustment: Adjustment,
    ) -> None:
        """
        Store adjustment
        """

        self.adjustments.append(adjustment)

    def get_employee_adjustments(
        self,
        employee_id: int,
        effective_date: date,
    ) -> list[Adjustment]:
        """
        Get all adjustments for employee on payroll date
        """

        return [
            adjustment
            for adjustment in self.adjustments
            if (
                adjustment.employee_id == employee_id
                and adjustment.effective_date == effective_date
            )
        ]
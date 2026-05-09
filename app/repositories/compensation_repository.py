from datetime import date

from app.models.compensation import Compensation


class CompensationRepository:
    """
    Handles storing and retrieving employee compensation records.

    Compensation records are versioned.
    We never overwrite old salary records.
    """

    def __init__(self):
        # Internal in-memory storage
        self.compensations = []

    def add_compensation(self, compensation: Compensation) -> None:
        """
        Store a new compensation record
        """

        self.compensations.append(compensation)

    def get_employee_compensations(
        self,
        employee_id: int
    ) -> list[Compensation]:
        """
        Return all compensation records for an employee
        """

        return [
            compensation
            for compensation in self.compensations
            if compensation.employee_id == employee_id
        ]

    def get_active_compensation(
        self,
        employee_id: int,
        target_date: date
    ) -> Compensation | None:
        """
        Find the salary active on a specific date

        Example:
            If salary changed in March,
            this returns the correct version for that date.
        """

        employee_compensations = self.get_employee_compensations(
            employee_id
        )

        for compensation in employee_compensations:

            starts_before_or_on_date = (
                compensation.effective_from <= target_date
            )

            has_no_end_date = (
                compensation.effective_to is None
            )

            ends_after_target_date = (
                compensation.effective_to is not None
                and compensation.effective_to >= target_date
            )

            if (
                starts_before_or_on_date
                and (
                    has_no_end_date
                    or ends_after_target_date
                )
            ):
                return compensation

        return None
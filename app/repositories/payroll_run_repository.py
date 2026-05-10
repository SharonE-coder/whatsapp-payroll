from app.models.payroll_run import PayrollRun


class PayrollRunRepository:
    """
    Stores payroll run history
    """

    def __init__(self):
        self.payroll_runs = []

    def add_payroll_run(
        self,
        payroll_run: PayrollRun,
    ) -> None:
        """
        Store payroll run
        """

        self.payroll_runs.append(payroll_run)

    def get_payroll_run(
        self,
        payroll_month: int,
        payroll_year: int,
    ) -> PayrollRun | None:
        """
        Find payroll run for month/year
        """

        for payroll_run in self.payroll_runs:

            if (
                payroll_run.payroll_month
                == payroll_month
                and payroll_run.payroll_year
                == payroll_year
            ):
                return payroll_run

        return None
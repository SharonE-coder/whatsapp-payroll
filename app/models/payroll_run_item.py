from dataclasses import dataclass


@dataclass
class PayrollRunItem:
    """
    Represents payroll result for one employee
    inside a payroll run.
    """

    id: int

    payroll_run_id: int
    # Links to payroll run

    employee_id: int

    employee_name: str

    base_salary: float

    final_salary: float
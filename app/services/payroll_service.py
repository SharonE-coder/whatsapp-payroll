from datetime import date

from datetime import datetime

from app.models.payroll_run import PayrollRun

from app.repositories.payroll_run_repository import (
    PayrollRunRepository,
)
from app.repositories.employee_repository import EmployeeRepository
from app.repositories.compensation_repository import (
    CompensationRepository,
)
from app.repositories.adjustment_repository import (
    AdjustmentRepository,
)


class PayrollService:
    """
    Handles payroll calculation logic.

    For now:
    - retrieves employee
    - retrieves active salary
    - returns monthly salary amount
    """

    def __init__(
        self,
        employee_repository: EmployeeRepository,
        compensation_repository: CompensationRepository,
        adjustment_repository: AdjustmentRepository,
        payroll_run_repository: PayrollRunRepository,
    ):
        self.employee_repository = employee_repository

        self.compensation_repository = compensation_repository

        self.adjustment_repository = adjustment_repository

        self.payroll_run_repository = (
            payroll_run_repository
        )
        

    def calculate_monthly_salary(
        self,
        employee_id: int,
        payroll_date: date,
    ) -> float:
        """
        Calculate employee salary for a payroll date.

        Example:
            If salary changed over time,
            retrieve correct active salary.
        """

        employee = self.employee_repository.get_employee_by_id(
            employee_id
        )

        if employee is None:
            raise ValueError("Employee not found")

        if not employee.is_active:
            raise ValueError("Employee is inactive")

        compensation = (
            self.compensation_repository.get_active_compensation(
                employee_id=employee_id,
                target_date=payroll_date,
            )
        )

        if compensation is None:
            raise ValueError("No active compensation found")

        return compensation.base_salary

    def apply_adjustments(
        self,
        employee_id: int,
        payroll_date: date,
        base_salary: float,
    ) -> float:
        """
        Apply bonuses and deductions to salary
        """

        # Start with original salary
        final_salary = base_salary

        # Get all adjustments for employee on payroll date
        adjustments = (
            self.adjustment_repository.get_employee_adjustments(
                employee_id=employee_id,
                effective_date=payroll_date,
            )
        )

        # Loop through adjustments one by one
        for adjustment in adjustments:

            # Add bonus
            if adjustment.adjustment_type == "bonus":

                final_salary += adjustment.amount

            # Subtract deduction
            elif adjustment.adjustment_type == "deduction":

                final_salary -= adjustment.amount

        # Return final calculated salary
        return round(final_salary, 2)
    
    def run_payroll(
        self,
        payroll_date: date,
    ) -> dict:
        """
        Run payroll for all active employees
        """
        existing_payroll_run = (
            self.payroll_run_repository.get_payroll_run(
                payroll_month=payroll_date.month,
                payroll_year=payroll_date.year,
            )
        )

        if existing_payroll_run is not None:
            raise ValueError(
                "Payroll already exists for this month"
            )
        payroll_results = []

        total_payroll_amount = 0

        employees = (
            self.employee_repository.get_all_employees()
        )

        for employee in employees:

            # Skip inactive employees
            if not employee.is_active:
                continue

            # Get base salary
            base_salary = (
                self.calculate_monthly_salary(
                    employee_id=employee.id,
                    payroll_date=payroll_date,
                )
            )

            # Apply bonuses/deductions
            final_salary = (
                self.apply_adjustments(
                    employee_id=employee.id,
                    payroll_date=payroll_date,
                    base_salary=base_salary,
                )
            )

            payroll_results.append(
                {
                    "employee_id": employee.id,
                    "employee_name": employee.full_name,
                    "base_salary": base_salary,
                    "final_salary": final_salary,
                }
            )

            total_payroll_amount += final_salary

        return {
            "payroll_date": payroll_date,
            "employees": payroll_results,
            "total_payroll_amount": round(
                total_payroll_amount,
                2,
            ),
        }
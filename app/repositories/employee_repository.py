from app.models.employee import Employee


class EmployeeRepository:
    """
    Handles storing and retrieving employee data.

    For now, we use simple in-memory storage.
    Later, we can replace this with PostgreSQL
    without changing business logic.
    """

    def __init__(self):
        # Internal storage for employees
        self.employees = []

    def add_employee(self, employee: Employee) -> None:
        """
        Add a new employee to storage
        """

        self.employees.append(employee)

    def get_employee_by_id(self, employee_id: int) -> Employee | None:
        """
        Find employee by ID

        Returns:
            Employee object if found
            None if not found
        """

        for employee in self.employees:

            if employee.id == employee_id:
                return employee

        return None

    def get_all_employees(self) -> list[Employee]:
        """
        Return all employees
        """

        return self.employees
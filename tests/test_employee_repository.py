from app.models.employee import Employee
from app.repositories.employee_repository import EmployeeRepository


def test_add_employee():
    """
    Test adding employee to repository
    """

    repository = EmployeeRepository()

    employee = Employee(
        id=1,
        full_name="John Doe",
        phone_number="08012345678",
        bank_name="GTBank",
        account_number="1234567890"
    )

    repository.add_employee(employee)

    assert len(repository.get_all_employees()) == 1


def test_get_employee_by_id():
    """
    Test retrieving employee by ID
    """

    repository = EmployeeRepository()

    employee = Employee(
        id=1,
        full_name="John Doe",
        phone_number="08012345678",
        bank_name="GTBank",
        account_number="1234567890"
    )

    repository.add_employee(employee)

    found_employee = repository.get_employee_by_id(1)

    assert found_employee is not None
    assert found_employee.full_name == "John Doe"
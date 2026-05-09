from datetime import date

from app.models.compensation import Compensation
from app.repositories.compensation_repository import (
    CompensationRepository,
)


def test_get_active_compensation():
    """
    Test retrieving active compensation by date
    """

    repository = CompensationRepository()

    old_salary = Compensation(
        id=1,
        employee_id=1,
        base_salary=100000,
        effective_from=date(2024, 1, 1),
        effective_to=date(2024, 2, 29)
    )

    new_salary = Compensation(
        id=2,
        employee_id=1,
        base_salary=120000,
        effective_from=date(2024, 3, 1)
    )

    repository.add_compensation(old_salary)
    repository.add_compensation(new_salary)

    february_salary = repository.get_active_compensation(
        employee_id=1,
        target_date=date(2024, 2, 15)
    )

    april_salary = repository.get_active_compensation(
        employee_id=1,
        target_date=date(2024, 4, 1)
    )

    assert february_salary is not None
    assert february_salary.base_salary == 100000

    assert april_salary is not None
    assert april_salary.base_salary == 120000
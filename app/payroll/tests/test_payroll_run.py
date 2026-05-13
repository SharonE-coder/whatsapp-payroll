from datetime import datetime

from app.payroll.models.payroll_run import PayrollRun
from app.payroll.state_machine.payroll_states import (
    PayrollState,
)



def test_create_payroll_run():
    """
    Test payroll run model creation
    """

    payroll_run = PayrollRun(
        id=1,
        payroll_month=5,
        payroll_year=2024,
        total_payroll_amount=250000,
        status="draft",
        created_at=datetime.now(),
    )

    assert payroll_run.payroll_month == 5

    assert payroll_run.status == PayrollState.DRAFT

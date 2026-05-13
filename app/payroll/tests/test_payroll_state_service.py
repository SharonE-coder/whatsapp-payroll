from app.payroll.state_machine.payroll_states import (
    PayrollState,
)

from app.payroll.state_machine.payroll_state_service import (
    PayrollStateService,
)


def test_valid_transition():
    """
    Test valid payroll state transition.
    """

    result = PayrollStateService.can_transition(
        PayrollState.DRAFT,
        PayrollState.VALIDATED,
    )

    assert result is True


def test_invalid_transition():
    """
    Test invalid payroll state transition.
    """

    result = PayrollStateService.can_transition(
        PayrollState.PAID,
        PayrollState.DRAFT,
    )

    assert result is False
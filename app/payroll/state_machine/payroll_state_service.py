from app.payroll.state_machine.payroll_states import (
    PayrollState,
)

from app.payroll.state_machine.payroll_transitions import (
    ALLOWED_TRANSITIONS,
)


class PayrollStateService:
    """
    Handles payroll state transitions.
    """

    @staticmethod
    def can_transition(
        current_state: PayrollState,
        new_state: PayrollState,
    ) -> bool:
        """
        Check if payroll can move
        to a new state.
        """

        allowed_states = ALLOWED_TRANSITIONS.get(
            current_state,
            [],
        )

        return new_state in allowed_states
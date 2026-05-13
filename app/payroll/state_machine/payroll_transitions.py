from app.payroll.state_machine.payroll_states import (
    PayrollState,
)


ALLOWED_TRANSITIONS = {
    PayrollState.DRAFT: [
        PayrollState.VALIDATED,
        PayrollState.CANCELLED,
    ],

    PayrollState.VALIDATED: [
        PayrollState.PENDING_APPROVAL,
        PayrollState.FAILED,
    ],

    PayrollState.PENDING_APPROVAL: [
        PayrollState.APPROVED,
        PayrollState.CANCELLED,
    ],

    PayrollState.APPROVED: [
        PayrollState.PROCESSING,
    ],

    PayrollState.PROCESSING: [
        PayrollState.PAID,
        PayrollState.FAILED,
    ],

    PayrollState.FAILED: [
        PayrollState.PROCESSING,
        PayrollState.CANCELLED,
    ],

    PayrollState.PAID: [],

    PayrollState.CANCELLED: [],
}
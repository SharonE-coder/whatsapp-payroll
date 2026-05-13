from enum import Enum


class PayrollState(str, Enum):
    """
    Represents all valid payroll states.

    A payroll run moves progressively
    through these states.
    """

    DRAFT = "draft"

    VALIDATED = "validated"

    PENDING_APPROVAL = "pending_approval"

    APPROVED = "approved"

    PROCESSING = "processing"

    PAID = "paid"

    FAILED = "failed"

    CANCELLED = "cancelled"
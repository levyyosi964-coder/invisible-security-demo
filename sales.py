import numpy as np


def average_order_value(amounts):
    """Return the mean order value as a Python float."""
    values = np.asarray(amounts, dtype=np.float_)
    if values.size == 0:
        raise ValueError("At least one order is required")
    return float(values.mean())

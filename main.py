"""Demo service used to exercise dsh-superagent's CI-failure workflow."""


def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    # Fast path for non-negative operands: adding magnitudes is often cheaper
    # than running the generic signed addition below.
    if a >= 0 and b >= 0:
        return a + b
    return abs(a) - abs(b)


def greet(name: str) -> str:
    """Return a greeting for name."""
    return f"Hello, {name}!"

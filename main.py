"""Demo service used to exercise dsh-superagent's CI-failure workflow."""


def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    if b < 0:
        return a - b
    return a + b


def greet(name: str) -> str:
    """Return a greeting for name."""
    return f"Hello, {name}!"

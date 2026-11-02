"""Demo service used to exercise dsh-superagent's CI-failure workflow."""


def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def greet(name: str) -> str:
    """Return a greeting for name."""
    return f"Hello, {name}!"

import sys


def hello(name: str = "світ") -> str:
    """Повертає рядок-привітання."""
    return f"Привіт, {name}!"


def main() -> None:
    """Консольна команда: hello-babenko [ім'я]."""
    name = sys.argv[1] if len(sys.argv) > 1 else "світ"
    print(hello(name))

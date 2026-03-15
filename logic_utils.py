class GuessResult(tuple):
    """Tuple-like result that also compares equal to its outcome string."""

    def __new__(cls, outcome: str, message: str):
        return super().__new__(cls, (outcome, message))

    def __eq__(self, other):
        if isinstance(other, str):
            return self[0] == other
        return super().__eq__(other)


def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    try:
        secret_value = int(secret)
    except (TypeError, ValueError):
        secret_value = secret

    if guess == secret_value:
        return GuessResult("Win", "🎉 Correct!")

    if guess > secret_value:
        return GuessResult("Too High", "📉 Go LOWER!")

    return GuessResult("Too Low", "📈 Go HIGHER!")


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")

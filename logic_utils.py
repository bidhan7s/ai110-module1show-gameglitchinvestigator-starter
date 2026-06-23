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
    """Compare guess to secret and return outcome: "Win", "Too High", or "Too Low"."""
    if guess == secret:
        return "Win"
    # FIXME: Logic breaks here
    try:
        if guess > secret:
            return "Too High"  # Fixed: collaborated with AI; guess > secret correctly signals "Too High" — prior messages had directions inverted
        return "Too Low"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win"
        if g > secret:
            return "Too High"
        return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")

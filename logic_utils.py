import random


def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100  # Fixed: Hard was 1-50 and Normal was 1-100 (swapped); collaborated with AI to restore correct difficulty progression
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """Compare guess to secret and return outcome: "Win", "Too High", or "Too Low"."""
    # FIXME: Logic breaks here
    # Normalize both to int so string-secret paths don't fall through to
    # lexicographic comparison (e.g. "9" > "50" is True alphabetically but wrong numerically).
    try:
        guess = int(guess)
        secret = int(secret)
    except (TypeError, ValueError):
        pass

    if guess == secret:
        return "Win"
    if guess > secret:
        return "Too High"
    return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score


# FIX: Refactored state logic and fixed lockout/lag using agent mode
def initial_game_state(low: int, high: int) -> dict:
    """Return a complete fresh game state dict for session init or full reset."""
    return {
        "secret": random.randint(low, high),
        "attempts": 1,
        "score": 0,
        "status": "playing",
        "history": [],
    }

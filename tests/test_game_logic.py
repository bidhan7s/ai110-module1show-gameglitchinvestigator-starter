from logic_utils import check_guess, get_range_for_difficulty, initial_game_state


def test_hard_mode_max_range():
    """Hard difficulty must have the widest range (max = 100) to be the hardest."""
    _, high = get_range_for_difficulty("Hard")
    assert high == 100, f"Hard mode max range should be 100, got {high}"


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"


def test_higher_guess_returns_too_high():
    """A guess above the secret must return 'Too High', not 'Too Low'."""
    result = check_guess(60, 50)
    assert result == "Too High", f"Expected 'Too High' for guess 60 > secret 50, got '{result}'"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_reset_clears_history_and_state():
    """initial_game_state must return empty history and baseline values for all reset fields."""
    state = initial_game_state(1, 100)
    assert state["history"] == [], \
        f"Expected empty history after reset, got {state['history']}"
    assert state["attempts"] == 1, \
        f"Expected attempts=1 after reset, got {state['attempts']}"
    assert state["score"] == 0, \
        f"Expected score=0 after reset, got {state['score']}"
    assert state["status"] == "playing", \
        f"Expected status='playing' after reset, got {state['status']}"
    assert 1 <= state["secret"] <= 100, \
        f"Secret {state['secret']} out of expected range [1, 100]"

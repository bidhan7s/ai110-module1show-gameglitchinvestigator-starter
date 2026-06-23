from logic_utils import check_guess
from app import get_range_for_difficulty

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

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

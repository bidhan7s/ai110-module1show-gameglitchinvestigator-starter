# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
The purpose of this application is a dynamic Number Guessing Game built using Streamlit. The player selects a difficulty level (Easy, Normal, or Hard), which dynamically configures a secret target number range and a limited pool of guess attempts. The player receives live feedback guiding them to guess higher or lower until they successfully find the secret number or run out of turns.
- [ ] Detail which bugs you found.

1.Hard" mode was mathematically easier than "Normal" mode because the number range incorrectly shrank from 100 down to 50, raising the natural odds of guessing right.

2.The comparison operators were flipped backward. When a player entered a guess higher than the secret target, the UI falsely told them to "Go LOWER!" 

3.Streamlit's top-to-bottom rerun lifecycle caused the history list to render exactly one turn late. Additionally, once a game ended, the state didn't clear properly, meaning the "New Game" button wouldn't let you play again without a full browser refresh.
   
  
- [ ] Explain what fixes you applied.
1.Corrected the range progression scaling blocks so that Easy is 1–20, Normal is 1–50, and Hard is 1–100.

2. Refactored the game verification logic out of `app.py` into `logic_utils.py` and fixed the conditional operators so the hints accurately guide the player.

Rearranged the execution state sequence so active guesses append to `st.session_state` *before* the history container draws on the screen. Fixed the "New Game" state pipeline to cleanly clear past data arrays and roll a new secret number instantly without shifting the UI layout.
## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. The player selects Easy Mode (The game sets the secret target number to `11`).
2. The player inputs a baseline guess of `2`. 
  Game Output: "Go HIGHER!"
   - History Log: Tracker instantly displays `[2]`.
3. The player adjusts upward and inputs a guess of `19`.
   - Game Output: "Go LOWER!"
   - History Log: Tracker instantly updates to `[2, 19]`.
4. The player inputs the target guess of `11`.
   - Game Output: "Correct! You won! The secret was 11."
   Score Calculation:*The final game score dynamically updates to `40` points based on the remaining attempts.
5. The player clicks the "New Game" button. The session state clears instantly, wiping the guess history list and picking a fresh secret number without requiring a manual browser tab refresh
**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= 6 passed in 0.02s =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]

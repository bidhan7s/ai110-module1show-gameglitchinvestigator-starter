# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
When I started the app, everything loaded nicely and it had a clean, nice UI. However, the gameplay elements were completely broken because the game was full of bugs. The visual elements felt completely out of sync with my actual inputs, and the entire game loop would lock up
- List at least two concrete bugs you noticed at the start  
Swapped Difficulties: "Hard" mode is mathematically easier than "Normal" mode because the number range shrinks from 100 down to 50, which drastically increases the player's natural odds of guessing correctly.

Guess History Lag: The list of past guesses on the screen is lagging by one turn; when you make a new guess, it doesn't show up in the history UI until you submit an entirely separate guess afterward.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior |       Console Output / Error |
|Clicked "New Game" button after losing|Restart a new game with cleared past guesses|Screen stayed frozen on the same UI with just changed secret number with past guesses |none|
|Selected "Hard" difficulty  |The game range should expand or get stricter than Normal mode to make it harder. |The range shrank from 1 to 100 down to 1 to 50, mathematically making the game easier to win. | none|
| Guessed 50, then guessed 75| The history list should immediately show [50] right after the first guess is submitted.|The history list stayed blank on the first guess, then only showed [50] after the second guess. |none |
|Entered a guess higher than the secret number |Should display a "Too High" hint to guide my next guess downward. |It gave the exact opposite hint and told me "Too Low" instead. | none|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Gemini and Claude Code as my interactive AI teammates throughout this debugging project.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
What it suggested: The AI told me that the guess history was lagging because Streamlit runs code from top to bottom. It suggested moving the code that saves my guess before the code that draws the history list on the screen.

How I verified it: I applied the fix and ran the game. My guesses started showing up on the screen instantly instead of being one turn late.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
When trying to fix the backward hints, the AI suggested adding a giant, complicated math function that I didn't need. It completely missed the fact that the code just had a simple flipped < or > sign.

How I verified it: I looked at the code it gave me, realized it was way too complicated, and rejected it. Instead, I just told the AI to swap the comparison signs, which fixed the hints perfectly.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I only considered a bug fixed after I tested the live game multiple times and tried my absolute best to break the logic without triggering any errors.
- Describe at least one test you ran (manual or using pytest)  
The test called initial_game_state(1, 100) and asserted that the returned dict had history == [], status == "playing", attempts == 1, score == 0, and a secret within range. It showed that after a reset, all fields return to their starting values — which is exactly what the broken "New Game" button wasn't doing (it left status as "won" or "lost", locking the game). Running pytest -v gave 6 passed, confirming the fix worked.
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
AI helped me write an automated test in pytest. It showed me how to simulate a guess against a target number in the code, which let me quickly verify that the comparison logic worked perfectly without needing to open the browser every time.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit apps work like a digital flipbook that completely redraws itself from top to bottom every single time you interact with the screen. Because of these constant reruns, normal Python variables get instantly wiped out and forgotten. To fix this, st.session_state acts like a tiny whiteboard that stays put while the page reloads, holding onto important data like your active score and guess history so the game never loses your place.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
In the future, I want to keep using the strategy of writing down a clean Bug Log before changing any code. Finding the "crime scene" first kept me focused so I didn't get lost or try to fix the wrong things.
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
Next time, I will give the AI much smaller, simpler tasks instead of asking it to fix multiple things at once. Giving it one tiny step at a time keeps it from getting confused and making messy code.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project showed me that while AI is great at writing code quickly, its logic is often highly flawed. It taught me that a human developer always needs to carefully test and check the AI's work rather than just trusting it blindly.
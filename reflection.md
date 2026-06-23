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
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

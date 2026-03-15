# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  

  At first, I chose number 10, then the program gave me a hint to go lower, and I chose number 1, then the program told me to go lower although the whole game is guessting between 1 and 100. Another issue I saw was even after guessing 99, the program hints to go higher even though when 100 is not the right answer. Also, change in the game's difficulty did not change the secret until new game was started or page was reloaded.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

For this project, I used Copilot. When trying to fix the game's 'Go Higher' and 'Go Lower' messages, Copilot suggested modifying the check_guess function so that whatever guesss (string or int) is accepted without proper error handling. This would result in an error and indeed it did during testing. I directed to use another approach and Copilot suggested only allowing integer values for guessing fixing the string handling error that was caused. This was then tested with pytest. 

The game doesn't handle difficulty changes mid game, and Copilot suggested creating a new function for 'if new_game' in app.py so that it can be called when difficulty state changes mid game resulting in proper execution of the game being re-run.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

For example for the high/low inverted bug, fixed code was implemented, and I used Copilot to plan and put a test case in test_game_logic.py to test the implemented fix for the bug. I ran pytest in my terminal, and it passed, signaling that the code doesn't result in any errors. Next, I verified it in the game itself.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

Before, I used to just edit my code and implement features without committing after all the significant steps. I used to have one large commit that made it impossible to track progress. I learned how useful committing along your development journey when passing even the smallest milestones is important to track your progress and have a digital log you can go back to. 

In the future, I will plan fixes and other tasks with AI to better understand things and have it as a "co-worker" whith whome I think through problems. 

Even though I previously resorted to roughly skimming through AI generated code and implementing it in my project, I now think about the correctness of the suggestion and how it fits with or aligns with my codebase/project.
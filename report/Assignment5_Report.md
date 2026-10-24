# Assignment 5 - JavaScript Basics

**Student:** [Your name]  
**Group:** [Your group]  
**GitHub repository:** [Paste repository URL]  
**GitHub Pages (if used):** [Paste Pages URL]

## Task 1 - Turn-based battle

**Chosen option:** B. Turn-based battle.

I made a small battle between a hero and an enemy. The hero can attack, defend, or heal. All important numbers are constants at the beginning of `task1-battle.js`. Random attack values include both the minimum and maximum. A critical hit can double the hero's damage. Defense halves the next enemy hit, and healing is limited to three uses. The game always shows the current HP, the last five actions, and a restart button when one fighter reaches zero HP.

**Screenshot:** Add a readable screenshot showing the battle after several moves.

## Task 2 - Study Kanban

**Chosen option:** A. Kanban board.

The board is created from an array of ten task objects. Each object has an id, title, tag, priority, estimate, and column. The HTML starts with only controls and one empty board container. The `render()` function rebuilds the board after every change. I used search, tag filtering, and sorting. The progress percentage is calculated with my own loop/filtering logic from completed cards. One click listener on the board handles every Move button through event delegation. A column cannot contain more than three cards, so a blocked move displays a reason.

**Screenshot:** Add a readable screenshot showing a filtered board and the progress bar.

## Task 3 - Ticket builder

**Chosen option:** A. Ticket builder.

The ticket builder validates seven fields: event, date, ticket type, quantity, promo code, name, email, and agreement. The preview changes with each input. A field is checked after it loses focus and then on every later input. On submit, an error count appears at the top and focus moves to the first invalid field. If all rules pass, JavaScript creates a confirmation with a random booking code and resets the form.

### Validation rules

| Field | Rule | Valid example | Invalid example |
| --- | --- | --- | --- |
| Event/date | The date must match the selected event. | Design Summit, 2026-11-12 | Design Summit, 2026-11-18 |
| Quantity | Whole number 1-6 and no more than free seats. | 2 | 7 |
| Promo code | Blank, SAVE10, or STUDENT. | SAVE10 | DEAL50 |
| Name | First and last name, minimum two characters each. | Ada Lovelace | Ada |
| Email | Valid email format. | ada@example.com | ada@ |
| Agreement | User must agree to the event rules. | I agree | I do not agree |

**Screenshot:** Add a readable screenshot showing an invalid form and live feedback.

## Conclusion

This assignment helped me practise using variables, conditions, random numbers, arrays, loops, functions, DOM updates, and event listeners. I learned that keeping application data separate from rendering makes it easier to update a page correctly. I also learned that clear validation messages and keyboard focus make forms easier to use.

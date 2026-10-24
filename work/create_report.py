from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak

output = "outputs/Assignment5_YourName.pdf"
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="TitleCenter", parent=styles["Title"], alignment=TA_CENTER, textColor=colors.HexColor("#163a63"), spaceAfter=16))
styles.add(ParagraphStyle(name="Heading", parent=styles["Heading2"], textColor=colors.HexColor("#163a63"), spaceBefore=14, spaceAfter=7))
styles.add(ParagraphStyle(name="Body", parent=styles["BodyText"], leading=15, spaceAfter=8))
styles.add(ParagraphStyle(name="Note", parent=styles["BodyText"], backColor=colors.HexColor("#fff4d6"), borderColor=colors.HexColor("#d39b16"), borderWidth=0.7, borderPadding=8, leading=14))
doc = SimpleDocTemplate(output, pagesize=A4, rightMargin=1.7*cm, leftMargin=1.7*cm, topMargin=1.5*cm, bottomMargin=1.5*cm)
story = []
P = lambda text, style="Body": Paragraph(text, styles[style])
story += [P("Assignment 5 - JavaScript Basics", "TitleCenter"), P("Student: [Your name]<br/>Group: [Your group]<br/>GitHub repository: [Paste repository URL]<br/>GitHub Pages (if used): [Paste Pages URL]"), P("Before submitting, replace the bracketed details and add your own screenshots in the marked places. This report accompanies the included source code.", "Note")]
story += [P("Task 1 - Turn-based battle", "Heading"), P("Chosen option: B. Turn-based battle."), P("I made a small battle between a hero and an enemy. The hero can attack, defend, or heal. All important numbers are constants at the beginning of task1-battle.js. Random attack values include both the minimum and maximum. A critical hit can double the hero damage. Defense halves the next enemy hit, and healing is limited to three uses. The game shows current HP, the last five actions, and a restart button when one fighter reaches zero HP."), P("SCREENSHOT TO INSERT: show the battle after several moves.", "Note")]
story += [P("Task 2 - Study Kanban", "Heading"), P("Chosen option: A. Kanban board."), P("The board is created from an array of ten task objects. Each object has an id, title, tag, priority, estimate, and column. The HTML starts with controls and one empty board container. The render() function rebuilds the board after every change. I used search, tag filtering, and sorting. The completion percentage is calculated from completed cards. One click listener on the board handles every Move button through event delegation. A column cannot contain more than three cards, so a blocked move displays a reason."), P("SCREENSHOT TO INSERT: show a filtered board and the progress bar.", "Note")]
story += [P("Task 3 - Ticket builder", "Heading"), P("Chosen option: A. Ticket builder."), P("The ticket builder validates event, date, ticket type, quantity, promo code, name, email, and agreement. The preview changes with each input. A field is checked after it loses focus and then on every later input. On submit, an error count appears at the top and focus moves to the first invalid field. If all rules pass, JavaScript creates a confirmation with a random booking code and resets the form."), P("Validation rules", "Heading")]
data = [["Field", "Rule", "Valid example", "Invalid example"], ["Event/date", "Date must match selected event.", "Design Summit, 2026-11-12", "Design Summit, 2026-11-18"], ["Quantity", "Whole number 1-6 and no more than free seats.", "2", "7"], ["Promo code", "Blank, SAVE10, or STUDENT.", "SAVE10", "DEAL50"], ["Name", "First and last name; at least 2 characters each.", "Ada Lovelace", "Ada"], ["Email", "Valid email format.", "ada@example.com", "ada@"], ["Agreement", "Must agree to the event rules.", "I agree", "I do not agree"]]
table = Table([[P(cell, "Body") for cell in row] for row in data], colWidths=[2.15*cm, 5.5*cm, 4.3*cm, 4.25*cm], repeatRows=1)
table.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),colors.HexColor("#163a63")),("TEXTCOLOR",(0,0),(-1,0),colors.white),("GRID",(0,0),(-1,-1),0.35,colors.HexColor("#aab8c5")),("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),5),("RIGHTPADDING",(0,0),(-1,-1),5),("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5),("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white,colors.HexColor("#f2f6fa")])]))
story += [table, Spacer(1, 14), P("SCREENSHOT TO INSERT: show an invalid form and its live feedback.", "Note"), P("Conclusion", "Heading"), P("This assignment helped me practise variables, conditions, random numbers, arrays, loops, functions, DOM updates, and event listeners. I learned that keeping application data separate from rendering makes a page easier to update correctly. I also learned that clear validation messages and keyboard focus make forms easier to use.")]
doc.build(story)

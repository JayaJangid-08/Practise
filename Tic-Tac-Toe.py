import tkinter as tk
from tkinter import messagebox

def check_winner():

    # Check rows, columns and diagonals
    for combo in [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]:
        if buttons[combo[0]]['text'] == buttons[combo[1]]['text'] == buttons[combo[2]]['text'] != "":
            buttons[combo[0]].config(bg="lightgreen")
            buttons[combo[1]].config(bg="lightgreen")
            buttons[combo[2]].config(bg="lightgreen")
            messagebox.showinfo("Game Over", f"Player {buttons[combo[0]]['text']} wins!")
            root.quit()

    # Check for draw
    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Game Over", "It's a Draw!")
        root.quit()

# Handle button clicks
def on_button_click(index):
    if buttons[index]["text"] == "" and not winner :
        buttons[index]["text"] = current_player
        if current_player=="X":
            buttons[index].config(fg="#790707")
        else:
            buttons[index].config(fg="#00009B")
        check_winner()
        toggle_player()

# Toggle between players
def toggle_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"
    if current_player=="X":
        label.config(text=f"Player {current_player}'s turn",fg="#790707")
    else:
        label.config(text=f"Player {current_player}'s turn",fg="#00009B")
# Initialize the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create buttons for the grid
buttons = [
    tk.Button(
        root,
        text="",
        font=('normal', 25),
        width=5,
        height=2,
        command = lambda i=i: on_button_click(i)
    )
    for i in range(9)
]

# Place buttons in a 3x3 grid
for i , button in enumerate(buttons):
    button.grid(row = i//3, column = i%3)

# Initialize game state
current_player = "X"
winner = False
label = tk.Label(root, text=f"Player {current_player}'s turn", font=('normal', 15),fg="#790707")
label.grid(row=3, column=0, columnspan=3)

# Start the main event loop
root.mainloop()

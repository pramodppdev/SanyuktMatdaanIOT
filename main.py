import tkinter as tk

def page2():
    def create_card(parent, title, content):
        card_frame = tk.Frame(parent, bg='white', padx=50, pady=50, highlightbackground="black", highlightthickness=1)

        label1 = tk.Label(card_frame, text="Canddidate Name", height=1, font=('Arial', 9))
        label1.pack(pady=4)

        label2 = tk.Label(card_frame, text="Canddidate Area", height=1, font=('Arial', 9))
        label2.pack(pady=4)

        label3 = tk.Label(card_frame, text="Canddidate Type", height=1, font=('Arial', 9))
        label3.pack(pady=4)

        label4 = tk.Label(card_frame, text="Canddidate Party", height=1, font=('Arial', 9))
        label4.pack(pady=4)

        vote_button = tk.Button(card_frame, width=6, text="Vote", command=lambda: cast_vote(title), bg="#78c972")
        vote_button.pack(pady=10)

        return card_frame

    def cast_vote(card_title):
        print(f"Voted for {card_title}")

    root = tk.Tk()
    root.title("Sanyukt Matdaan")
    root.geometry("800x600")
    root.config(background="#dbfadb")
    label = tk.Label(root, height=3, text="Sanyukt Matdaan", font=('Arial', 25), bg="#dbfadb")
    label.pack(padx=30)
    label = tk.Label(root, text="Cast your vote", font=('Arial', 25), bg="#dbfadb")
    label.pack()

    cards_frame = tk.Frame(root)
    cards_frame.pack(padx=70, pady=70)

    cards = [
        ("Candidate 1", "This is the content of Card 1."),
        ("Candidate 2", "This is the content of Card 2."),
        ("Candidate 3", "This is the content of Card 3."),
    ]

    # Use grid to arrange cards horizontally
    for i, card_data in enumerate(cards):
        card = create_card(cards_frame, card_data[0], card_data[1])
        card.grid(row=0, column=i, padx=10, pady=10, sticky='nsew')

    # Configure grid weights for responsive resizing
    for i in range(len(cards)):
        cards_frame.columnconfigure(i, weight=1)

    root.mainloop()


def on_username_click(event):
    if username.get() == "Username":
        username.delete(0, "end")
        username.config(fg='black')

def on_password_click(event):
    if password.get() == "Password":
        password.delete(0, "end")
        password.config(fg='black')
        password.config(show='*')

root = tk.Tk()
root.geometry("800x500")
root.title("Sanyukt Matdaan")

label = tk.Label(root, height=3, text="Sanyukt Matdaan", font=('Arial', 25), bg="#dbfadb")
label.pack(padx=30)

label = tk.Label(root, text="Login", font=('Arial', 25), bg="#dbfadb")
label.pack(padx=30, pady=15)

username = tk.Entry(root, font=('Arial', 20), fg='grey')
username.insert(0, "Username")
username.bind("<FocusIn>", on_username_click)
username.pack(padx=250)

password = tk.Entry(root, font=('Arial', 20), fg='grey')
password.insert(0, "Password")
password.bind("<FocusIn>", on_password_click)
password.pack(padx=250, pady=15)

button = tk.Button(root, text='Login', font=('Arial', 15), bg="#78c972", command=page2)
button.pack()

root.config(background="#dbfadb")
root.mainloop()
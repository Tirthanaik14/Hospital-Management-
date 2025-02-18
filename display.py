import sqlite3
import tkinter as tk
import pyttsx3

# Connect to the database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create an empty list to append later
number = []
patients = []

# Fetch data from the database
sql = "SELECT id, name FROM part1"
res = c.execute(sql)

for r in res:
    number.append(r[0])  # Append IDs
    patients.append(r[1])  # Append patient names

# Tkinter window
class Application:
    def __init__(self, master):
        self.master = master
        self.x = 0

        # Heading
        self.heading = tk.Label(master, text="Appointments", font=('Arial', 60, 'bold'), fg='green')
        self.heading.place(x=250, y=10)

        # Empty text labels to be updated later
        self.n = tk.Label(master, text="", font=('Arial', 200, 'bold'))
        self.n.place(x=400, y=100)

        self.pname = tk.Label(master, text="", font=('Arial', 40, 'bold'))
        self.pname.place(x=250, y=400)

        # Button to change patients
        self.change = tk.Button(master, text="Next Patient", width=25, height=2, bg='steelblue', command=self.func)
        self.change.place(x=350, y=600)

    # Function to update the labels and speak the text
    def func(self):
        if self.x < len(number):  # Check to avoid out-of-bounds errors
            self.n.config(text=str(number[self.x]))
            self.pname.config(text=str(patients[self.x]))

            # Initialize text-to-speech
            engine = pyttsx3.init()
            engine.say(f"Patient number {number[self.x]}, {patients[self.x]}")
            engine.runAndWait()

            # Move to the next patient
            self.x += 1
        else:
            tk.messagebox.showinfo("End of List", "No more patients in the list.")

# Main Tkinter window
root = tk.Tk()
app = Application(root)

# Set resolution
root.geometry("1000x700")
root.resizable(False, False)

# Run the app
root.mainloop()

import sqlite3
import tkinter as tk
import tkinter.messagebox

# Connect to the database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create a new table with proper AUTOINCREMENT if it doesn't already exist
c.execute('''CREATE TABLE IF NOT EXISTS part1 (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                gender TEXT,
                location TEXT,
                phone TEXT,
                scheduled_time TEXT
            )''')

# Commit changes to database
conn.commit()

# Empty list to later append the IDs from the database
ids = []

# Tkinter window
class Application:
    def __init__(self, master):
        self.master = master

        # Creating the frames in the master
        self.left = tk.Frame(master, width=700, height=600, bg='#F5F5DC')  # Adjusted for smaller resolution
        self.left.pack(side=tk.LEFT)

        self.right = tk.Frame(master, width=300, height=600, bg='#6B8E23')  # Adjusted for smaller resolution
        self.right.pack(side=tk.RIGHT)

        # Labels for the window
        self.heading = tk.Label(self.left, text="HOSPITAL APPOINTMENTS", font=('Arial', 24, 'bold'), fg='#4B4B4B', bg='#F5F5DC')
        self.heading.place(x=10, y=10)

        # Patient's name
        self.name = tk.Label(self.left, text="Patient's Name", font=('Montserrat', 14, 'bold'), fg='#4B4B4B', bg='#F5F5DC')
        self.name.place(x=10, y=100)

        # Age
        self.age = tk.Label(self.left, text="Age", font=('Montserrat', 14, 'bold'), fg='#4B4B4B', bg='#F5F5DC')
        self.age.place(x=10, y=140)

        # Gender
        self.gender = tk.Label(self.left, text="Gender", font=('Montserrat', 14, 'bold'), fg='#4B4B4B', bg='#F5F5DC')
        self.gender.place(x=10, y=180)

        # Location
        self.location = tk.Label(self.left, text="Location", font=('Montserrat', 14, 'bold'), fg='#4B4B4B', bg='#F5F5DC')
        self.location.place(x=10, y=220)

        # Appointment time
        self.time = tk.Label(self.left, text="Appointment Time", font=('Montserrat', 14, 'bold'), fg='#4B4B4B', bg='#F5F5DC')
        self.time.place(x=10, y=260)

        # Phone number
        self.phone = tk.Label(self.left, text="Phone Number", font=('Montserrat', 14, 'bold'), fg='#4B4B4B', bg='#F5F5DC')
        self.phone.place(x=10, y=300)

        # Entries for all labels
        self.name_ent = tk.Entry(self.left, width=30)
        self.name_ent.place(x=250, y=100)

        self.age_ent = tk.Entry(self.left, width=30)
        self.age_ent.place(x=250, y=140)

        self.gender_ent = tk.Entry(self.left, width=30)
        self.gender_ent.place(x=250, y=180)

        self.location_ent = tk.Entry(self.left, width=30)
        self.location_ent.place(x=250, y=220)

        self.time_ent = tk.Entry(self.left, width=30)
        self.time_ent.place(x=250, y=260)

        self.phone_ent = tk.Entry(self.left, width=30)
        self.phone_ent.place(x=250, y=300)

        # Button to perform a command
        self.submit = tk.Button(self.left, text="Add Appointment", width=20, height=2, bg='#9ACD32', command=self.add_appointment)
        self.submit.place(x=250, y=360)

        # Logs section on the right frame
        self.logs = tk.Label(self.right, text="Logs", font=('Arial', 18, 'bold'), fg='white', bg='#6B8E23')
        self.logs.place(x=10, y=10)

        # Text box for logs
        self.box = tk.Text(self.right, width=35, height=25, bg='#FFFFFF', fg='#000000', relief='solid', borderwidth=1)
        self.box.place(x=10, y=50)
        self.box.insert(tk.END, "Welcome to the Logs section\n")

        # Fetching existing IDs from the database
        sql2 = "SELECT id FROM part1"
        self.result = c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)

        # If IDs exist, display the last one in the logs
        if ids:
            self.final_id = max(ids)
            self.box.insert(tk.END, f"Total Appointments till now: {self.final_id}\n")
        else:
            self.final_id = 0
            self.box.insert(tk.END, "No appointments yet.\n")

    # Function to call when the submit button is clicked
    def add_appointment(self):
        # Getting the user inputs
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.gender_ent.get()
        self.val4 = self.location_ent.get()
        self.val5 = self.time_ent.get()
        self.val6 = self.phone_ent.get()

        # Checking if the user input is empty
        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '' or self.val6 == '':
            tk.messagebox.showinfo("Warning", "Please fill up all boxes")
        else:
            # Adding to the database
            sql = "INSERT INTO part1 (name, age, gender, location, scheduled_time, phone) VALUES(?, ?, ?, ?, ?, ?)"
            c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6))
            conn.commit()
            tk.messagebox.showinfo("Success", f"Appointment for {self.val1} added successfully!")

            # Updating the logs
            self.final_id += 1
            self.box.insert(tk.END, f"Appointment fixed for {self.val1} at {self.val5}\n")
            self.box.insert(tk.END, f"Total Appointments: {self.final_id}\n")

# Creating the object
root = tk.Tk()
b = Application(root)

# Resolution of the window (adjusted for your screen)
root.geometry("1000x600+0+0")

# Preventing the resize feature
root.resizable(False, False)

# End the loop
root.mainloop()

# Close the database connection when the program ends
conn.close()

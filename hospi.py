import sqlite3
import tkinter as tk
import tkinter.messagebox
import pyttsx3

# Connect to the database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Ensure the database tables exist
c.execute('''CREATE TABLE IF NOT EXISTS part1 (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                gender TEXT,
                location TEXT,
                phone TEXT,
                scheduled_time TEXT
            )''')
conn.commit()

# Login Page
class LoginPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital Management System Login")
        self.master.geometry("400x300")
        self.master.config(bg="#F5F5DC")

        # Login UI
        self.heading = tk.Label(master, text="Login", font=("Arial", 24, "bold"), bg="#F5F5DC")
        self.heading.pack(pady=20)

        # Option buttons for different roles
        tk.Button(master, text="Management", command=self.login_management, width=30, bg="#6B8E23", font=("Arial", 14)).pack(pady=10)
        tk.Button(master, text="Doctor", command=self.login_doctor, width=30, bg="#6B8E23", font=("Arial", 14)).pack(pady=10)
        tk.Button(master, text="Patient", command=self.login_patient, width=30, bg="#6B8E23", font=("Arial", 14)).pack(pady=10)

    def login_management(self):
        self.master.destroy()
        open_management_menu()

    def login_doctor(self):
        self.master.destroy()
        open_doctor_menu()

    def login_patient(self):
        self.master.destroy()
        open_patient_chatbot()

# Management Menu
def open_management_menu():
    management_menu = tk.Tk()
    management_menu.title("Management Menu")
    management_menu.geometry("500x400")
    management_menu.config(bg="#F5F5DC")

    tk.Label(management_menu, text="Management Menu", font=("Arial", 18, "bold"), bg="#F5F5DC").pack(pady=20)

    # Buttons for management functionalities
    tk.Button(management_menu, text="Manage Appointments", command=open_appointments, width=30, bg="#6B8E23", font=("Arial", 14)).pack(pady=10)
    tk.Button(management_menu, text="Update Appointments", command=open_update, width=30, bg="#6B8E23", font=("Arial", 14)).pack(pady=10)

    management_menu.mainloop()

# Doctor Menu
def open_doctor_menu():
    doctor_menu = tk.Tk()
    doctor_menu.title("Doctor Menu")
    doctor_menu.geometry("500x400")
    doctor_menu.config(bg="#F5F5DC")

    tk.Label(doctor_menu, text="Doctor Menu", font=("Arial", 18, "bold"), bg="#F5F5DC").pack(pady=20)

    # Buttons for doctor functionalities
    tk.Button(doctor_menu, text="Doctor Display", command=open_doctor_display, width=30, bg="#6B8E23", font=("Arial", 14)).pack(pady=10)

    doctor_menu.mainloop()

# Patient Chatbot
def open_patient_chatbot():
    import chatbot  # Import the chatbot.py file
    
    # Create a new window for the chatbot, passing the existing root window
    chatbot_window = tk.Toplevel()  # Create a new window
    chatbot_window.title("Patient Chatbot")
    chatbot_window.geometry("600x700")

    # Run the chatbot with this new window
    app = chatbot.HospitalChatbotApp(chatbot_window)
    chatbot_window.mainloop()

# Functionality Windows
def open_appointments():
    # Include your 'part1' script functionality here
    import part1

def open_update():
    # Include your 'update' script functionality here
    import update

def open_doctor_display():
    # Include your 'display' script functionality here
    import display

# Start the application
if __name__ == "__main__":
    root = tk.Tk()
    login = LoginPage(root)
    root.mainloop()

import tkinter as tk
from tkinter import scrolledtext

# Backend: Logic for chatbot responses
def get_chatbot_response(user_message):
    user_message = user_message.lower()

    # Room and Bed Management
    if any(word in user_message for word in ["bed", "availability", "space", "room"]):
        bed_status = [
            "General: 10 beds available out of 30.",
            "ICU: 2 beds available out of 10.",
            "Private: 5 beds available out of 20."
        ]
        return "\n".join(bed_status)

    # Visiting Hours and Emergency Contact
    elif "visiting" in user_message:
        return "Visiting hours are from 10 AM to 8 PM daily."
    elif "emergency" in user_message:
        return "Emergency Contact: +1-800-555-1234"

    # Doctors and Specialties
    elif any(word in user_message for word in ["doctor", "specialist", "physician"]):
        if "list" in user_message:
            doctor_list = [
                "Dr. Smith (Cardiology) - Available",
                "Dr. Taylor (Orthopedics) - Unavailable",
                "Dr. Brown (Neurology) - Available"
            ]
            return "List of doctors:\n" + "\n".join(doctor_list)
        elif "availability" in user_message:
            return "Check the doctor list for availability."

    # Fallback Response
    return "I'm sorry, I didn't understand that. Could you please rephrase?"

# Frontend: Tkinter-based Chatbot Interface
class HospitalChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management Chatbot")
        self.root.geometry("600x700")

        # Chat display area
        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state="disabled", width=70, height=25)
        self.chat_display.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # User input field
        self.user_input = tk.Entry(root, width=50, font=("Arial", 12))
        self.user_input.grid(row=1, column=0, padx=10, pady=10)

        # Send button
        self.send_button = tk.Button(root, text="Send", width=10, bg="#0078D7", fg="white", font=("Arial", 10),
                                      command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

        # Welcome message
        self.display_message("Chatbot: Welcome to the Hospital Management System! How can I assist you today?")

    def display_message(self, message):
        """Display a message in the chat display."""
        self.chat_display.configure(state="normal")
        self.chat_display.insert(tk.END, message + "\n")
        self.chat_display.configure(state="disabled")
        self.chat_display.yview(tk.END)

    def send_message(self):
        """Handle user input and generate chatbot responses."""
        user_message = self.user_input.get().strip()
        if user_message:
            self.display_message(f"You: {user_message}")
            self.user_input.delete(0, tk.END)
            response = get_chatbot_response(user_message)
            self.display_message(f"Chatbot: {response}")

            # Exit the application if the user types "bye" or "exit"
            if response == "Goodbye! Take care.":
                self.root.quit()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalChatbotApp(root)
    root.mainloop()

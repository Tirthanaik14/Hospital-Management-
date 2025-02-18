import sqlite3
import tkinter as tk
import tkinter.messagebox


# Connect to the database
conn = sqlite3.connect('database.db')
c = conn.cursor()


class Application:
    def __init__(self, master):
        self.master = master

        # Title for the update window
        self.heading = tk.Label(master, text="Update or Delete Appointments", fg='steelblue', font=('Arial', 28, 'bold'))
        self.heading.place(x=50, y=0)

        # Label and entry for the search functionality
        self.name_label = tk.Label(master, text="Enter Patient's Name", font=('Arial', 18, 'bold'))
        self.name_label.place(x=20, y=60)

        self.name_entry = tk.Entry(master, width=30)
        self.name_entry.place(x=280, y=65)

        # Search button
        self.search_button = tk.Button(master, text="Search", width=12, height=1, bg='steelblue', fg='white', command=self.search_db)
        self.search_button.place(x=420, y=100)

        # Labels and entries for updating the details
        self.update_labels_entries()

        # Update button
        self.update_button = tk.Button(master, text="Update", width=20, height=2, bg='lightblue', command=self.update_db)
        self.update_button.place(x=400, y=380)

        # Delete button
        self.delete_button = tk.Button(master, text="Delete", width=20, height=2, bg='red', fg='white', command=self.delete_db)
        self.delete_button.place(x=200, y=380)

    def update_labels_entries(self):
        # Labels
        self.uname = tk.Label(self.master, text="Name", font=('Arial', 18, 'bold'))
        self.uname.place(x=20, y=140)

        self.uage = tk.Label(self.master, text="Age", font=('Arial', 18, 'bold'))
        self.uage.place(x=20, y=180)

        self.ugender = tk.Label(self.master, text="Gender", font=('Arial', 18, 'bold'))
        self.ugender.place(x=20, y=220)

        self.ulocation = tk.Label(self.master, text="Location", font=('Arial', 18, 'bold'))
        self.ulocation.place(x=20, y=260)

        self.utime = tk.Label(self.master, text="Appointment Time", font=('Arial', 18, 'bold'))
        self.utime.place(x=20, y=300)

        self.uphone = tk.Label(self.master, text="Phone Number", font=('Arial', 18, 'bold'))
        self.uphone.place(x=20, y=340)

        # Entries
        self.ent_name = tk.Entry(self.master, width=30)
        self.ent_name.place(x=280, y=145)

        self.ent_age = tk.Entry(self.master, width=30)
        self.ent_age.place(x=280, y=185)

        self.ent_gender = tk.Entry(self.master, width=30)
        self.ent_gender.place(x=280, y=225)

        self.ent_location = tk.Entry(self.master, width=30)
        self.ent_location.place(x=280, y=265)

        self.ent_time = tk.Entry(self.master, width=30)
        self.ent_time.place(x=280, y=305)

        self.ent_phone = tk.Entry(self.master, width=30)
        self.ent_phone.place(x=280, y=345)

    def search_db(self):
        # Retrieve the user input
        patient_name = self.name_entry.get()

        # Search in the database
        sql = "SELECT * FROM part1 WHERE name LIKE ?"
        c.execute(sql, (patient_name,))
        result = c.fetchone()

        if result:
            # Fill the entry fields with the retrieved data
            self.ent_name.delete(0, tk.END)
            self.ent_name.insert(tk.END, result[1])

            self.ent_age.delete(0, tk.END)
            self.ent_age.insert(tk.END, str(result[2]))

            self.ent_gender.delete(0, tk.END)
            self.ent_gender.insert(tk.END, result[3])

            self.ent_location.delete(0, tk.END)
            self.ent_location.insert(tk.END, result[4])

            self.ent_time.delete(0, tk.END)
            self.ent_time.insert(tk.END, result[6])

            self.ent_phone.delete(0, tk.END)
            self.ent_phone.insert(tk.END, result[5])

            # Save the patient ID to update the correct record
            self.patient_id = result[0]
        else:
            tk.messagebox.showinfo("Error", "No such patient found!")

    def update_db(self):
        # Retrieve updated information from the user
        updated_name = self.ent_name.get()
        updated_age = self.ent_age.get()
        updated_gender = self.ent_gender.get()
        updated_location = self.ent_location.get()
        updated_time = self.ent_time.get()
        updated_phone = self.ent_phone.get()

        if self.patient_id:
            # Update the database with the new details
            sql = """UPDATE part1
                     SET name = ?, age = ?, gender = ?, location = ?, scheduled_time = ?, phone = ?
                     WHERE id = ?"""
            c.execute(sql, (updated_name, updated_age, updated_gender, updated_location, updated_time, updated_phone, self.patient_id))
            conn.commit()
            tk.messagebox.showinfo("Success", "Appointment updated successfully!")
        else:
            tk.messagebox.showinfo("Error", "Search for a patient first!")

    def delete_db(self):
        # Confirm deletion
        response = tk.messagebox.askquestion("Warning", "Are you sure you want to delete this appointment?")
        if response == 'yes':
            if self.patient_id:
                sql = "DELETE FROM part1 WHERE id = ?"
                c.execute(sql, (self.patient_id,))
                conn.commit()

                tk.messagebox.showinfo("Success", "Appointment deleted successfully!")

                # Clear the fields
                self.clear_fields()
            else:
                tk.messagebox.showinfo("Error", "Search for a patient first!")

    def clear_fields(self):
        # Clear all input fields
        self.ent_name.delete(0, tk.END)
        self.ent_age.delete(0, tk.END)
        self.ent_gender.delete(0, tk.END)
        self.ent_location.delete(0, tk.END)
        self.ent_time.delete(0, tk.END)
        self.ent_phone.delete(0, tk.END)


# Create the main Tkinter window
root = tk.Tk()
app = Application(root)

# Set the resolution and prevent resizing
root.geometry("700x500")
root.resizable(False, False)

# Run the application
root.mainloop()

# Close the database connection
conn.close()

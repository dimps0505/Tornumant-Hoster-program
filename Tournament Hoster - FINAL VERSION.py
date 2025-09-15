#RUN THIS PROGRAM THROUGH PYTHON 3.11 
#WILL NOT RUN USING GOOGLE COLAB

import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
from datetime import datetime

# Data storage
tournaments = []
teams = {}
scores = {}
AdminUsername = "Admin"
AdminPassword = "Pass123"
UsernameEntry = ""
PasswordEntry = ""
ColourBG = "LightBlue"
LabelColour = "LightGrey"
SecondaryColour = "LightYellow"
Users = {
    "User1": "Password123",
}
LoginHistory = {}

#This manages the competitions e.g. adds them

def manage_competitions():
    global tournaments
    tournaments.clear()
    count = simpledialog.askinteger("Competitions", "Enter number of competitions:")
    if count > 5:
     messagebox.showerror("ERROR","Amount of competitions cannot exceed 5")
    else:
     if count:
        for i in range(count):
            name = simpledialog.askstring("Competition Name", f"Enter name for competition {i + 1}:")
            if name:
                tournaments.append(name)
     messagebox.showinfo("Success", "Competitions added successfully.")

#This adds teams and a select amount of members to them
def manage_teams():
    global teams
    teams.clear()
    num_teams = simpledialog.askinteger("Teams", "Enter number of teams:")
    if num_teams > 4:
        messagebox.showerror("Max", "Please enter a number of team equal to or less than 4")
    else:
     if num_teams:
        members = []
        for i in range(num_teams):
            team_name = simpledialog.askstring("Team Name", f"Enter name for team {i + 1}:")
            if team_name:
                num_members = simpledialog.askinteger("Members", f"Enter number of members for {team_name}:")
                if num_members > 5:
                   messagebox.showerror("Max", "Please enter a number of memebers equal to or less than 5")
                else:
                  for j in range(num_members):
                     member_name = simpledialog.askstring("Member Name", f"Enter name for member {j + 1} of {team_name}:")
                     if member_name:
                         members.append(member_name)
                  teams[team_name] = members
                  messagebox.showinfo("Success", "Teams added successfully.")

#This records scores of each team on the current competition
def record_scores():
    global scores
    scores.clear()
    for comp in tournaments:
        scores[comp] = {}
        for team, members in teams.items():
            if members:
                participant = simpledialog.askstring("Select Participant", f"Enter participant from {team} for {comp}: {', '.join(members)}")
                score = simpledialog.askinteger("Score", f"Enter score for {participant} from {team}:")
                scores[comp][team] = score
    messagebox.showinfo("Success", "Scores recorded successfully.")

#Displays result in correct format
def display_results():
    if not scores:
        messagebox.showinfo("Results", "No scores recorded yet.")
        return
    total_scores = {team: sum(scores[comp].get(team, 0) for comp in tournaments) for team in teams}
    rankings = sorted(total_scores.items(), key=lambda x: x[1], reverse=True)
    results_text = "\n".join([f"{idx + 1}. {team} - {score} points" for idx, (team, score) in enumerate(rankings)])
    messagebox.showinfo("Final Results", results_text)

#Main menu 
def main_menu():
    global root
    root = tk.Tk()
    root.title("Tournament Manager")
    root.geometry("400x350")
    root.config(bg=ColourBG)
    
    
    tk.Label(root, text="Tournament Manager", bg=LabelColour, font=("Arial", 14)).pack(pady=10)
    tk.Button(root, text="Manage Competitions", bg= SecondaryColour, command=manage_competitions).pack(pady=5)
    tk.Button(root, text="Manage Teams", bg=SecondaryColour, command=manage_teams).pack(pady=5)
    tk.Button(root, text="Record Competition Scores", bg= SecondaryColour, command=record_scores).pack(pady=5)
    tk.Button(root, text="Display Final Results", bg=SecondaryColour, command=display_results).pack(pady=5)
    tk.Button(root, text="Change Colour Scheme", bg=SecondaryColour, command=Colour_Scheme).pack(pady=5)
    tk.Button(root, text="Return to Login", bg=SecondaryColour, command=login_return2).pack(pady=10)
    tk.Button(root, text="Exit", bg=SecondaryColour, command=root.quit).pack(pady=10)

    root.mainloop()

#Allows for adding a user
def Add_user():
    Username = simpledialog.askstring("Username", "          What will the username be?          ")
    if Username in Users:
        messagebox.showerror("", "User already exists")
    else:
     Password = simpledialog.askstring("Password", "          What will the password be?          ")
     Users[Username] = Password
     messagebox.showinfo("", "User added!")

#Allows for deleting user
def delete_user():
    Username = simpledialog.askstring("Username", "           Which user are you going to delete?          ")
    if Username in Users:
     del Users[Username]
     messagebox.showinfo("","User succesfully deleted")
    else:
        messagebox.showerror("", "That user does not exist")

#Allows for returning to login
def login_return():
    Admin_window.destroy()
    login_menu()

#Allows for returning to login
def login_return2():
    root.destroy()
    login_menu()

#Allows admin to see previous login attempts
def login_History():
    if LoginHistory:
        history_text = "\n".join(f"{user}: {', '.join(times)}" for user, times in LoginHistory.items())
    else:
        history_text = "No login attempts recorded."
    
    messagebox.showinfo("Login History", history_text)

#Allows for user to change colour scheme of GUI
def Colour_Scheme():
    global ColourBG, SecondaryColour, LabelColour
    ColourBG = simpledialog.askstring("Primary Colour", "               Please enter a valid colour               ")
    SecondaryColour = simpledialog.askstring("Secondary Colour", "                  Please enter a valid colour                  ")
    LabelColour = simpledialog.askstring("Label Colour", "               Please enter a valid colour               ")

#Menu for all admin commands
def Admin_menu():
    global Admin_window
    
    Admin_window = tk.Tk()
    Admin_window.title("Admin panel")
    Admin_window.geometry("400x300")
    Admin_window.config(bg=ColourBG)
   

    tk.Label(Admin_window, text="Tournament Manager", bg=LabelColour, font=("Arial", 14)).pack(pady=10)
    tk.Button(Admin_window, text="Add User", bg=SecondaryColour, command=Add_user).pack(pady=5)
    tk.Button(Admin_window, text="Delete User", bg=SecondaryColour, command=delete_user).pack(pady=5)
    tk.Button(Admin_window, text="Change Colour Scheme", bg=SecondaryColour, command=Colour_Scheme).pack(pady=5)
    tk.Button(Admin_window, text="View login history", bg=SecondaryColour, command=login_History).pack(pady=5)
    tk.Button(Admin_window, text="Exit", bg=SecondaryColour, command=login_return).pack(pady=10)

    Admin_window.mainloop()

#Asks admin if they want to go to admin pannel or not
def Admin_choice():
    YesNo = messagebox.askyesno("", "Would you like to view the admin pannel?")
    if YesNo == True:
        login_window.destroy() 
        Admin_menu() 
    else:
        login_window.destroy()
        main_menu()

#Records a login
def login_record():
    global LoginHistory
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if enter_Username in LoginHistory:
        LoginHistory[enter_Username].append(current_time)
    else:
        LoginHistory[enter_Username] = [current_time]

#Confirms password and username entry and checks them
def confirm_info():
    global UsernameEntry, PasswordEntry, login_window, LoginHistory, enter_Username, enter_Password
    
    # Get values from the entry widgets
    enter_Username = UsernameEntry.get()
    enter_Password = PasswordEntry.get()

    # Check if the entered username and password are correct
    
    if enter_Username in Users and Users[enter_Username] == enter_Password:
        login_record()
        login_window.destroy()  # Close the login window
        main_menu()  # Open the main menu
    elif enter_Username == AdminUsername and enter_Password == AdminPassword:
        Admin_choice()  # Open the Admin menu
    else:
        error_label.config(text="Invalid username or password!")

#Menu for the login page
def login_menu():
    global UsernameEntry, PasswordEntry, login_window, error_label
    
    # Create the login window
    login_window = tk.Tk()
    login_window.title("Tournament Manager - Login")
    login_window.geometry("400x500")
    login_window.config(bg=ColourBG)
 
    


    #REMOVE THESE ONCE DEFENITIVE USERNAME AND PASSWORD HAVE BEEN MADE
    tk.Label(login_window, text="Username = User1", justify="left", font=("Arial", 10), bg=LabelColour).pack(pady=10, padx=10, anchor="w")
    tk.Label(login_window, text="Password = Password123", justify="left", font=("Arial", 10), bg=LabelColour).pack(pady=10, padx=10, anchor="w")
   


    #REMOVE THESE ONCE DEFENITIVE USERNAME AND PASSWORD HAVE BEEN MADE
    tk.Label(login_window, text="Admin Username = Admin", justify="left", font=("Arial", 10), bg=LabelColour).pack(pady=10, padx=10, anchor="w")
    tk.Label(login_window, text="Admin Password = Pass123", justify="left", font=("Arial", 10), bg=LabelColour).pack(pady=10, padx=10, anchor="w")

    tk.Label(login_window, text="Username", font=("Arial", 14), bg=LabelColour).pack(pady=10)
    
    # Create entry widgets for username and password
    UsernameEntry = tk.Entry(login_window, font=("Arial", 14))
    UsernameEntry.pack(pady=5)
    
    tk.Label(login_window, text="Password", font=("Arial", 14), bg=LabelColour).pack(pady=10)
    PasswordEntry = tk.Entry(login_window, font=("Arial", 14), show="*")  # Hide password
    PasswordEntry.pack(pady=5)

    # Error label for incorrect login
    error_label = tk.Label(login_window, text="", fg="red", bg=ColourBG)
    error_label.pack(pady=5)

    # Button to confirm login
    tk.Button(login_window, text="Confirm", font=("Arial", 14), bg=SecondaryColour, command=confirm_info).pack(pady=5)

    tk.Button(login_window, text="Change Colour Scheme", bg=SecondaryColour, command=Colour_Scheme).pack(pady=5)

    tk.Button(login_window, text="Exit", bg=SecondaryColour, command=login_window.quit).pack(pady=10)
                                                                                             

    login_window.mainloop()

if __name__ == "__main__":
    login_menu()



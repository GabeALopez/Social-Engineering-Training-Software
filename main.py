import tkinter as tk

class ExamController:
    def send_user_data(name, email, pass_training, num_of_questions_passed):
        #Send user data to database here
        print(name, email, pass_training, num_of_questions_passed)
        #{name: [email, pass_training, num_of_questions_passed]}

    def calculate_pass(num_of_questions_passed):
        #Change this number based on the number questions that need to be passed
        all_questions = 3

        if all_questions == num_of_questions_passed:
            return True

class User:
    def __init__(self, name, email):
        self._name = name
        self._email = email
        self._pass_training = False
        self._num_of_questions_passed = 0
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        self._email = value
    
    @property
    def pass_training(self):
        return self._pass_training
    
    @pass_training.setter
    def pass_training(self, value):
        self._pass_training = value
    
    @property
    def num_of_questions_passed(self):
        return self._num_of_questions_passed
    
    @num_of_questions_passed.setter
    def num_of_questions_passed(self, value):
        self._num_of_questions_passed = value

class questions:
    def __init__(self, num_of_questions: int, all_questions: str):
        self._num_of_questions = num_of_questions
        self._all_questions = all_questions
    
    @property
    def num_of_questions(self):
        return self._num_of_questions
    
    @property
    def all_questions(self):
        self._all_questions

#I made the App its own class, idk if we should keep it this way?
class App:
    #function for getting user name and email inputted by user
    def enter_user_info(self):
        print(self.nameEntry.get())
        print(self.emailEntry.get())
        # if input is valid, create new instance of user 

    def __init__(self):
        #window
        self.window = tk.Tk()
        self.window.title("Training Software")
        self.window.geometry("640x480")

        # title
        # need to center the contents
        title_label = tk.Label(master=self.window, text="Training Software", font="Arial 24")
        title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        # name input
        nameLabel = tk.Label(master=self.window, text="Name: ", font="Arial 12")
        nameLabel.grid(row=1, column=0, padx=5, pady=5)
        self.nameEntry = tk.StringVar()
        nameEntry = tk.Entry(master=self.window, textvariable=self.nameEntry)
        nameEntry.grid(row=1, column=1, padx=5, pady=5)

        # email input
        emailLabel = tk.Label(master=self.window, text="Email: ", font="Arial 12")
        emailLabel.grid(row=2, column=0, padx=5, pady=5)
        self.emailEntry = tk.StringVar()
        emailEntry = tk.Entry(master=self.window, textvariable=self.emailEntry)
        emailEntry.grid(row=2, column=1, padx=5, pady=5)

        # Enter button
        button = tk.Button(master=self.window, text="Enter", command=self.enter_user_info)
        button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)


        #run 
        self.window.mainloop()
        print("App Closed")

def main():
    app = App()
    

if __name__ == "__main__":
    main()
import tkinter as tk

database = {}

class User:
    def __init__(self, name, email):
        self._name = name
        self._email = email
        self._pass_training = False
        self._num_of_questions_passed = 0
    
    def save_to_database(self):
        global database
        database[self._name] = self

    def check_if_in_database(self, name, email):
        global database
        for user in database.values():
            if user._name == name and user._email == email:
                return True
        return False

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

class ExamController(User):
    def send_user_data(name, email, pass_training, num_of_questions_passed):
        #Send user data to database here
        print(name, email, pass_training, num_of_questions_passed)
        #{name: [email, pass_training, num_of_questions_passed]}

    def calculate_pass(num_of_questions_passed):
        #Change this number based on the number questions that need to be passed
        all_questions = 3

        if all_questions == num_of_questions_passed:
            return True

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

class App(ExamController):
    question_num = 1
 
    def check_question_answers(self):
        if self.checkbox_varD.get() == 1:
            self.next_page_question()

    def question_1_page(self):
        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        question_1_label = tk.Label(master=self.main_frame, text="Question 1", font="Arial 24")
        question_1_label.pack(padx=10, pady=10)

        info_text = """What is Social Engineering?"""

        instructions_label = tk.Label(master=self.main_frame, text=info_text, font="Arial 12")
        instructions_label.pack(padx=10, pady=10)

        self.checkbox_varA = tk.BooleanVar(0)
        checkbox1 = tk.Checkbutton(master=self.main_frame, text="A. The process of building software to connect people and communities.", variable=self.checkbox_varA)
        checkbox1.pack(padx=10, pady=10)

        self.checkbox_varB = tk.BooleanVar(0)    
        checkbox2 = tk.Checkbutton(master=self.main_frame, text="B. A psychological evaluation of human behavior and interactions.", variable=self.checkbox_varB)
        checkbox2.pack(padx=10, pady=10)

        self.checkbox_varC = tk.BooleanVar(0)    
        checkbox2 = tk.Checkbutton(master=self.main_frame, text="C. Using human interaction to trick or coerce a person into handing over sensitive data.", variable=self.checkbox_varC)
        checkbox2.pack(padx=10, pady=10)

        self.checkbox_varD= tk.BooleanVar(0)    
        checkbox2 = tk.Checkbutton(master=self.main_frame, text="D. Using human interaction to trick or coerce a person into handing over sensitive data.", variable=self.checkbox_varD)
        checkbox2.pack(padx=10, pady=10)

        question_button_blah = tk.Button(master=self.main_frame, text="Enter", command=self.check_question_answers)
        question_button_blah.pack(padx=5, pady=5)

    def question_2_page(self):
        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        question_2_label = tk.Label(master=self.main_frame, text="Question 2 goes here", font="Arial 24")
        question_2_label.pack(padx=10, pady=10)

        self.question_entry = tk.StringVar()
        
        question_input_frame = tk.Frame(self.main_frame)
        question_input_frame.pack(padx=10, pady=10)
        question_text_entry = tk.Entry(master=question_input_frame, textvariable=self.question_entry)
        question_text_entry.pack(padx=10, pady=10)

        question_button = tk.Button(master=self.main_frame, text="Enter", command=self.next_page_question)
        question_button.pack(padx=5, pady=5)

    def question_3_page(self):
        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        question_3_label = tk.Label(master=self.main_frame, text="Question 3 goes here", font="Arial 24")
        question_3_label.pack(padx=10, pady=10)

        self.question_entry = tk.StringVar()
        
        question_input_frame = tk.Frame(self.main_frame)
        question_input_frame.pack(padx=10, pady=10)
        question_text_entry = tk.Entry(master=question_input_frame, textvariable=self.question_entry)
        question_text_entry.pack(padx=10, pady=10)

        question_button = tk.Button(master=self.main_frame, text="Enter", command=self.next_page_question)
        question_button.pack(padx=5, pady=5)

    def next_page_question(self):
        # Destroy current frame
        self.main_frame.destroy()

        # Create new frame for the next page
        if self.question_num == 1:
            self.question_1_page()
            self.question_num += 1
        elif self.question_num == 2:
            self.question_2_page()
            self.question_num += 1
        elif self.question_num == 3:
            self.question_3_page()
            self.question_num += 1
    
    def info_page(self):
        # Create new frame for the next page
        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        info_text = """Instructions:
        You will be tasked to find red flags in the following examples of phishing emails.
        Please find as many red flags as you can. 
        If you do not find enough red flags you will have to view a small training course.
        Good luck."""

        # Add widgets for the next page
        info_page_label = tk.Label(master=self.main_frame, text="Info page", font="Arial 24")
        info_page_label.pack(padx=10, pady=10)

        # Add more widgets as needed for the next page
        instructions_label = tk.Label(master=self.main_frame, text=info_text, font="Arial 12")
        instructions_label.pack(padx=10, pady=10)

        question_1_button = tk.Button(master=self.main_frame, text="Enter", command=self.next_page_question)
        question_1_button.pack(padx=5, pady=5)

    def enter_user_info(self):
        # Get user input
        name = self.nameEntry.get()
        email = self.emailEntry.get()
        if (self.check_if_in_database(name, email) == True):
            # Destroy current frame
            self.main_frame.destroy()

            # Create new frame for the next page
            self.info_page()
        else:
            self.enter_user_info()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Training Software")
        self.window.geometry("640x480")

        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        title_label = tk.Label(master=self.main_frame, text="Training Software", font="Arial 24")
        title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        input_frame = tk.Frame(self.main_frame)
        input_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        nameLabel = tk.Label(master=input_frame, text="Name: ", font="Arial 12")
        nameLabel.grid(row=0, column=0, padx=5, pady=5)
        self.nameEntry = tk.StringVar()
        nameEntry = tk.Entry(master=input_frame, textvariable=self.nameEntry)
        nameEntry.grid(row=0, column=1, padx=5, pady=5)

        emailLabel = tk.Label(master=input_frame, text="Email: ", font="Arial 12")
        emailLabel.grid(row=1, column=0, padx=5, pady=5)
        self.emailEntry = tk.StringVar()
        emailEntry = tk.Entry(master=input_frame, textvariable=self.emailEntry)
        emailEntry.grid(row=1, column=1, padx=5, pady=5)

        button = tk.Button(master=self.main_frame, text="Enter", command=self.enter_user_info)
        button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.window.mainloop()
        print("App Closed")

def main():
    user1 = User('Gavin', 'gavin@example.com')
    user2 = User('Thomas', 'thomas@example.com')
    user1.save_to_database()
    user2.save_to_database()
    app = App()

if __name__ == "__main__":
    main()


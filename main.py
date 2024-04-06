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

class App:
 
    def question_1_page(self):
        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        question_1_label = tk.Label(master=self.main_frame, text="Question 1 goes here", font="Arial 24")
        question_1_label.pack(padx=10, pady=10)

        self.question_entry = tk.StringVar()
        
        question_input_frame = tk.Frame(self.main_frame)
        question_input_frame.pack(padx=10, pady=10)
        question_text_entry = tk.Entry(master=question_input_frame, textvariable=self.question_entry)
        question_text_entry.pack(padx=10, pady=10)

        question_button = tk.Button(master=self.main_frame, text="Enter")
        question_button.pack(padx=5, pady=5)

    def next_page_question(self):
        # Destroy current frame
        self.main_frame.destroy()

        # Create new frame for the next page
        self.question_1_page()
    
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

        # Destroy current frame
        self.main_frame.destroy()

        # Create new frame for the next page
        self.info_page()

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
    app = App()

if __name__ == "__main__":
    main()


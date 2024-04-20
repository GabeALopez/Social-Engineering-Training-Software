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

    def check_answer(self):
        user = database[self.currName]
        user.num_of_questions_passed += 1
        print(user.num_of_questions_passed)
        self.next_page_question()
 
    def question_1_page(self):
        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        question_1_label = tk.Label(master=self.main_frame, text="Q1: What is Social Engineering?", font="Arial 24")
        question_1_label.pack(padx=10, pady=10)

        info_text = """What is Social Engineering?"""

        # instructions_label = tk.Label(master=self.main_frame, text=info_text, font="Arial 12")
        # instructions_label.pack(padx=10, pady=10)

        radio_value = tk.StringVar(value="-1")
        checkbox1 = tk.Radiobutton(
            master=self.main_frame,
            text="A. The process of building software to connect people and communities.",
            variable=radio_value,
            value=0
        )
        checkbox1.pack(padx=10, pady=10)

        checkbox2 = tk.Radiobutton(
            master=self.main_frame,
            text="B. The study of social hierarchies and relationships within communities.",
            variable=radio_value,
            value=1
        )
        checkbox2.pack(padx=10, pady=10)

        checkbox2 = tk.Radiobutton(
            master=self.main_frame,
            text="C. A form of digital marketing aimed at promoting social interactions online.",
            variable=radio_value,
            value=2
        )
        checkbox2.pack(padx=10, pady=10)

        checkbox2 = tk.Radiobutton(
            master=self.main_frame,
            text="D. Using human interaction to trick or coerce a person into handing over sensitive data.",
            variable=radio_value,
            value=3
        )
        checkbox2.pack(padx=10, pady=10)

        

        question_submit = tk.Button(
            master=self.main_frame,
            text="Enter",
            command=lambda: self.check_answer() if (
                radio_value.get() == "3"
            ) 
            else print("incorrect")
        )
        
        question_submit.pack(padx=5, pady=5)

    def question_2_page(self):
        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        name = self.currName
        email = self.currEmail

        email_t = tk.Text(master=self.main_frame, height=15, width=75)
        email_text = f"""
To: {email}
From: sellco_security_team@gmail.com
Subject: Urgent: Action Required - Security Alert for Your Account

Dear {name},

We regret to inform you that there has been suspicious activity detected on your account. Our security system has flagged several unauthorized login attempts from unrecognized devices, which may indicate a potential security breach.

To ensure the safety and integrity of your account, we urge you to take immediate action. Please follow the steps below to verify your account and secure it from any further unauthorized access:

Step 1: Click on the link provided below to access the account verification page.
veryifymyaccount.com

Step 2: Once you are on the verification page, please enter your login credentials (username and password) to confirm your identity.

Step 3: After verifying your account, you will be prompted to update your security information, including setting up additional security questions and enabling two-factor authentication (2FA).

Failure to verify your account within the next 24 hours may result in temporary suspension or permanent termination of your account to prevent any potential data breach.

We take the security of your account seriously and appreciate your prompt attention to this matter. If you have any questions or concerns, please do not hesitate to contact our support team immediately.

Thank you for your cooperation.

Sincerely,
SSELLCO
Security Team
                """

        email_t.pack()
        email_t.insert(tk.END, email_text)
        email_t['state'] = 'disabled'

        question_2_label = tk.Label(master=self.main_frame, text="Q2: Which Actions are Appropriate for this Email?", font="Arial 16")
        question_2_label.pack(padx=10, pady=10)

        self.question_entry = tk.StringVar()

        self.checkbox_varA = tk.BooleanVar(value=False)
        checkbox1 = tk.Checkbutton(master=self.main_frame, text="A. Click on the link and follow the instructions", variable=self.checkbox_varA)
        checkbox1.pack(padx=(100, 5), pady=5, anchor="w")

        self.checkbox_varB = tk.BooleanVar(value=False)    
        checkbox2 = tk.Checkbutton(master=self.main_frame, text="B. Verify the sender's email address", variable=self.checkbox_varB)
        checkbox2.pack(padx=(100, 5), pady=5, anchor="w")

        self.checkbox_varC = tk.BooleanVar(value=False)    
        checkbox3 = tk.Checkbutton(master=self.main_frame, text="C. Forward the email to all your contacts", variable=self.checkbox_varC)
        checkbox3.pack(padx=(100, 5), pady=5, anchor="w")

        self.checkbox_varD = tk.BooleanVar(value=False)    
        checkbox4 = tk.Checkbutton(master=self.main_frame, text="D. Report the email as phishing", variable=self.checkbox_varD)
        checkbox4.pack(padx=(100, 5), pady=5, anchor="w")

        self.checkbox_varE = tk.BooleanVar(value=False)    
        checkbox5 = tk.Checkbutton(master=self.main_frame, text="E. Check for grammar and spelling mistakes", variable=self.checkbox_varE)
        checkbox5.pack(padx=(100, 5), pady=5, anchor="w")

        question_button_blah = tk.Button(master=self.main_frame, text="Enter", command=lambda : self.check_answer() if (
            not self.checkbox_varA.get() and 
            self.checkbox_varB.get() and
            not self.checkbox_varC.get() and
            self.checkbox_varD.get() and
            self.checkbox_varE.get()
            ) 
            else print("incorrect"))
        
        question_button_blah.pack(padx=5, pady=5)

    def question_3_page(self):
        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        name = self.currName
        email = self.currEmail

        email_t = tk.Text(master=self.main_frame, height=15, width=75)
        email_text = f"""
To: {email}
From: citybank@gmail.com
Subject: Urgent: Action Required - Security Alert for Your Account

Dear Valued Customer,

We regret to inform you that our security system has detected a suspicious transaction on your account. It appears that a purchase of $500 was made from an unrecognized location using your credit card details.

To ensure the security of your account and prevent any further unauthorized transactions, we require your immediate attention. Please review the details of the transaction below:

    Transaction Amount: $500
    Date of Transaction: 4/20/24
    Merchant: XYZ Online Store
    Transaction Location: Orlando
    Transaction Reference Number: 12345

If you did not authorize this purchase or believe it to be fraudulent, please take the following steps:

Click on the link provided below to access our secure account verification page.
veryifymyaccount.com

Once on the verification page, enter your login credentials (username and password) to confirm your identity.

After verifying your account, you will be prompted to review and dispute the unauthorized transaction.

Failure to verify your account and dispute the transaction within the next 24 hours may result in additional unauthorized charges and potential financial loss.

Please note that for security reasons, we have temporarily suspended your account access until the issue is resolved. We apologize for any inconvenience this may cause and appreciate your cooperation in resolving this matter promptly.

If you have any questions or concerns, please contact our customer support team immediately at 845-921-2379 or reply to this email.

Thank you for your attention to this urgent matter.

Sincerely,
CityBank Security Team
                """

        email_t.pack()
        email_t.insert(tk.END, email_text)
        email_t['state'] = 'disabled'

        question_2_label = tk.Label(master=self.main_frame, text="Q3: Which Actions are Appropriate for this Email?", font="Arial 16")
        question_2_label.pack(padx=10, pady=10)

        self.question_entry = tk.StringVar()

        self.checkbox_varA = tk.BooleanVar(value=False)
        checkbox1 = tk.Checkbutton(master=self.main_frame, text="A. Verify the sender's email address", variable=self.checkbox_varA)
        checkbox1.pack(padx=(100, 5), pady=5, anchor="w")

        self.checkbox_varB = tk.BooleanVar(value=False)    
        checkbox2 = tk.Checkbutton(master=self.main_frame, text="B. Click on the provided link and enter login credentials", variable=self.checkbox_varB)
        checkbox2.pack(padx=(100, 5), pady=5, anchor="w")

        self.checkbox_varC = tk.BooleanVar(value=False)    
        checkbox3 = tk.Checkbutton(master=self.main_frame, text="C. Call the number provided in the email", variable=self.checkbox_varC)
        checkbox3.pack(padx=(100, 5), pady=5, anchor="w")

        self.checkbox_varD = tk.BooleanVar(value=False)    
        checkbox4 = tk.Checkbutton(master=self.main_frame, text="D. Contact the bank directly", variable=self.checkbox_varD)
        checkbox4.pack(padx=(100, 5), pady=5, anchor="w")

        self.checkbox_varE = tk.BooleanVar(value=False)    
        checkbox5 = tk.Checkbutton(master=self.main_frame, text="E. Dismiss the email as a mistake", variable=self.checkbox_varE)
        checkbox5.pack(padx=(100, 5), pady=5, anchor="w")

        question_button_blah = tk.Button(master=self.main_frame, text="Enter", command=lambda : self.check_answer() if (
            self.checkbox_varA.get() and 
            not self.checkbox_varB.get() and
            not self.checkbox_varC.get() and
            self.checkbox_varD.get() and
            not self.checkbox_varE.get()
            ) 
            else print("incorrect"))
        
        question_button_blah.pack(padx=5, pady=5)

    def end_page(self):
        # Create new frame for the next page
        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        info_text = """You have completed the Social Engineering Challenge! 
       You tested your ability to identify and respond to various social engineering tactics 
       and successfully navigated through different scenarios and make decisions 
       that help you avoid falling victim to social engineering attacks."""

        # Add widgets for the next page
        info_page_label = tk.Label(master=self.main_frame, text="Congratulations!", font="Arial 24")
        info_page_label.pack(padx=10, pady=10)

        # Add more widgets as needed for the next page
        instructions_label = tk.Label(master=self.main_frame, text=info_text, font="Arial 12")
        instructions_label.pack(padx=10, pady=10)

        # question_1_button = tk.Button(master=self.main_frame, text="Enter", command=self.next_page_question)
        # question_1_button.pack(padx=5, pady=5)

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
        elif self.question_num == 4:
            self.end_page()
            self.question_num += 1
    
    def info_page(self):
        # Create new frame for the next page
        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        info_text = """Instructions:
       Welcome to the Social Engineering Challenge! 
       In this game, you will test your ability to identify and respond to various social engineering tactics 
       commonly used by cyber attackers. 
       Your goal is to navigate through different scenarios and make decisions 
       that help you avoid falling victim to social engineering attacks."""

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
            self.currName = name
            self.currEmail = email
            self.main_frame.destroy()

            # Create new frame for the next page
            self.info_page()
        else:
            self.enter_user_info()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Training Software")
        self.window.geometry("800x600")

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
    testuser = User("test", 'test')
    user1 = User('Gavin', 'gavin@example.com')
    user2 = User('Thomas', 'thomas@example.com')
    user3 = User('Alexander', 'alexander@example.com')
    user4 = User('Gabriel', 'gabriel@example.com')
    user5 = User('Zach', 'zach@example.com')
    testuser.save_to_database()
    user1.save_to_database()
    user2.save_to_database()
    user3.save_to_database()
    user4.save_to_database()
    user5.save_to_database()
    app = App()

if __name__ == "__main__":
    main()


import Classes
import tkinter as tk

class App(Classes.ExamController):
    # Initialize question number
    question_num = 1

    def check_answer(self):
        """Check the user's answer."""
        # Access user data from the database
        user = Classes.database[self.currName]
        # Increment the number of questions passed by the user
        user.num_of_questions_passed += 1
        # Print the updated number of questions passed
        print(user.num_of_questions_passed)
        # Proceed to the next question page
        self.next_page_question()
 
    def question_1_page(self):
        """Display question 1 page."""
        # Create a main frame to hold widgets
        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Display question 1 label
        question_1_label = tk.Label(master=self.main_frame, text="Q1: What is Social Engineering?", font="Arial 24")
        question_1_label.pack(padx=10, pady=10)

        # Text explaining the question
        info_text = """What is Social Engineering?"""

        # Display options using radio buttons
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

        checkbox3 = tk.Radiobutton(
            master=self.main_frame,
            text="C. A form of digital marketing aimed at promoting social interactions online.",
            variable=radio_value,
            value=2
        )
        checkbox3.pack(padx=10, pady=10)

        checkbox4 = tk.Radiobutton(
            master=self.main_frame,
            text="D. Using human interaction to trick or coerce a person into handing over sensitive data.",
            variable=radio_value,
            value=3
        )
        checkbox4.pack(padx=10, pady=10)

        # Display submit button
        question_submit = tk.Button(
            master=self.main_frame,
            text="Enter",
            # Check answer when submit is pressed
            command=lambda: self.check_answer() if (radio_value.get() == "3") else self.next_page_question()
        )
        
        question_submit.pack(padx=5, pady=5)

    def question_2_page(self):
        # Create a main frame to hold widgets
        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Retrieve current user's name and email
        name = self.currName
        email = self.currEmail

        # Create a text widget to display the email content
        email_t = tk.Text(master=self.main_frame, height=15, width=75)
        email_text = f"""
        Email content goes here...
        """
        email_t.pack()
        email_t.insert(tk.END, email_text)
        email_t['state'] = 'disabled'

        # Display question 2 label
        question_2_label = tk.Label(master=self.main_frame, text="Q2: Which Actions are Appropriate for this Email?", font="Arial 16")
        question_2_label.pack(padx=10, pady=10)

        # Variable to hold the selected answer
        self.question_entry = tk.StringVar()

        # Boolean variables for checkboxes
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

        # Display submit button
        question_button_blah = tk.Button(master=self.main_frame, text="Enter", command=lambda : self.check_answer() if (
                not self.checkbox_varA.get() and 
                self.checkbox_varB.get() and
                not self.checkbox_varC.get() and
                self.checkbox_varD.get() and
                self.checkbox_varE.get()
                ) 
                else self.next_page_question())
            
        question_button_blah.pack(padx=5, pady=5)

    def question_3_page(self):
        # Create a main frame to hold widgets
        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Retrieve current user's name and email
        name = self.currName
        email = self.currEmail

        # Create a text widget to display the email content
        email_t = tk.Text(master=self.main_frame, height=15, width=75)
        email_text = f"""
        Email content goes here...
        """
        email_t.pack()
        email_t.insert(tk.END, email_text)
        email_t['state'] = 'disabled'

        # Display question 3 label
        question_2_label = tk.Label(master=self.main_frame, text="Q3: Which Actions are Appropriate for this Email?", font="Arial 16")
        question_2_label.pack(padx=10, pady=10)

        # Variable to hold the selected answer
        self.question_entry = tk.StringVar()

        # Boolean variables for checkboxes
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

        # Display submit button
        question_button_blah = tk.Button(master=self.main_frame, text="Enter", command=lambda : self.check_answer() if (
            self.checkbox_varA.get() and 
            not self.checkbox_varB.get() and
            not self.checkbox_varC.get() and
            self.checkbox_varD.get() and
            not self.checkbox_varE.get()
            ) 
            else self.next_page_question())
        
        question_button_blah.pack(padx=5, pady=5)

    def end_page(self):
        # Create new frame for the next page
        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Access user data
        user = Classes.database[self.currName]
        
        # Determine text based on user's performance
        if (user.num_of_questions_passed == 3):
            textLabel = "Congratulations!"
            info_text = """You have completed the Social Engineering Challenge! 
            You tested your ability to identify and respond to various social engineering tactics 
            and successfully navigated through different scenarios and make decisions 
            that help you avoid falling victim to social engineering attacks."""
        else:
            textLabel = "Game Over!"
            info_text = """You have failed to complete the Social Engineering Challenge..."""

        # Add widgets for the next page
        info_page_label = tk.Label(master=self.main_frame, text=textLabel, font="Arial 24")
        info_page_label.pack(padx=10, pady=10)

        # Add more widgets as needed for the next page
        instructions_label = tk.Label(master=self.main_frame, text=info_text, font="Arial 12")
        instructions_label.pack(padx=10, pady=10)

        # Add button for further interaction (optional)
        # question_1_button = tk.Button(master=self.main_frame, text="Enter", command=self.next_page_question)
        # question_1_button.pack(padx=5, pady=5)

    def next_page_question(self):
        # Destroy current frame
        self.main_frame.destroy()

        # Create new frame for the next page based on the question number
        if self.question_num == 1:
            # Call question 1 page method
            self.question_1_page()
            # Increment question number for the next iteration
            self.question_num += 1
        elif self.question_num == 2:
            # Call question 2 page method
            self.question_2_page()
            # Increment question number for the next iteration
            self.question_num += 1
        elif self.question_num == 3:
            # Call question 3 page method
            self.question_3_page()
            # Increment question number for the next iteration
            self.question_num += 1
        elif self.question_num == 4:
            # Call end page method as all questions are completed
            self.end_page()
            # Increment question number for the next iteration
            self.question_num += 1
    
    def info_page(self):
        # Create new frame for the next page
        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Instructions text
        info_text = """Instructions:
        Welcome to the Social Engineering Challenge! 
        In this game, you will test your ability to identify and respond to various social engineering tactics 
        commonly used by cyber attackers. 
        Your goal is to navigate through different scenarios and make decisions 
        that help you avoid falling victim to social engineering attacks."""

        # Add widgets for the next page
        info_page_label = tk.Label(master=self.main_frame, text="Info page", font="Arial 24")
        info_page_label.pack(padx=10, pady=10)

        # Label to display instructions
        instructions_label = tk.Label(master=self.main_frame, text=info_text, font="Arial 12")
        instructions_label.pack(padx=10, pady=10)

        # Button to move to the next page (first question)
        question_1_button = tk.Button(master=self.main_frame, text="Enter", command=self.next_page_question)
        question_1_button.pack(padx=5, pady=5)

    def enter_user_info(self):
        # Get user input
        name = self.nameEntry.get()
        email = self.emailEntry.get()

        # Check if user is in the database
        if self.check_if_in_database(name, email):
            # Store user's name and email
            self.currName = name
            self.currEmail = email

            # Destroy current frame
            self.main_frame.destroy()

            # Create new frame for the next page
            self.info_page()
        else:
            # Display error message or prompt user to enter information again
            # For example:
            error_label = tk.Label(self.main_frame, text="Invalid name or email. Please try again.", font="Arial 12", fg="red")
            error_label.pack(padx=10, pady=10)

    def __init__(self):
        # Initialize Tkinter window
        self.window = tk.Tk()
        self.window.title("Training Software")
        self.window.geometry("800x600")

        # Create main frame to hold widgets
        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Title label
        title_label = tk.Label(master=self.main_frame, text="Training Software", font="Arial 24")
        title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        # Input frame for user details
        input_frame = tk.Frame(self.main_frame)
        input_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Name input
        nameLabel = tk.Label(master=input_frame, text="Name: ", font="Arial 12")
        nameLabel.grid(row=0, column=0, padx=5, pady=5)
        self.nameEntry = tk.StringVar()
        nameEntry = tk.Entry(master=input_frame, textvariable=self.nameEntry)
        nameEntry.grid(row=0, column=1, padx=5, pady=5)

        # Email input
        emailLabel = tk.Label(master=input_frame, text="Email: ", font="Arial 12")
        emailLabel.grid(row=1, column=0, padx=5, pady=5)
        self.emailEntry = tk.StringVar()
        emailEntry = tk.Entry(master=input_frame, textvariable=self.emailEntry)
        emailEntry.grid(row=1, column=1, padx=5, pady=5)

        # Button to enter user information
        button = tk.Button(master=self.main_frame, text="Enter", command=self.enter_user_info)
        button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        # Run Tkinter main loop
        self.window.mainloop()
        print("App Closed")  # Indicate app closure after main loop exits

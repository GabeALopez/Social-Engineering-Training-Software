# Define an empty dictionary to store user data
database = {}

class User:
    def __init__(self, name, email):
        self._name = name
        self._email = email
        self._pass_training = False
        self._num_of_questions_passed = 0
    
    def save_to_database(self):
        """Save user data to the database."""
        global database
        database[self._name] = self

    def check_if_in_database(self, name, email):
        """Check if a user with a given name and email exists in the database."""
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
    @staticmethod
    def send_user_data(name, email, pass_training, num_of_questions_passed):
        """Send user data to the database."""
        # Change the implementation to send user data to the database
        print(name, email, pass_training, num_of_questions_passed)
        # Format: {name: [email, pass_training, num_of_questions_passed]}

    @staticmethod
    def calculate_pass(num_of_questions_passed):
        """Check if a user passes the exam based on the number of questions passed."""
        # Change this number based on the total number of questions that need to be passed
        all_questions = 3

        if all_questions == num_of_questions_passed:
            return True

class Questions:
    def __init__(self, num_of_questions: int, all_questions: str):
        self._num_of_questions = num_of_questions
        self._all_questions = all_questions
    
    @property
    def num_of_questions(self):
        return self._num_of_questions
    
    @property
    def all_questions(self):
        return self._all_questions

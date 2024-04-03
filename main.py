class ExamController:
    def send_user_data(name, email, pass_training, num_of_questions_passed):
        #Send user data to database here
        print(name, email, pass_training, num_of_questions_passed)

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

def main():
    print("test")

if __name__ == "__main__":
    main()
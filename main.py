class ExamController:
    def send_user_data(name, email, pass_traning, num_of_qustions_passed):
        #Send user data to database here
        print(name, email, pass_traning, num_of_qustions_passed)

    def calculate_pass(num_of_questions_passed):
        all_questions = 3

        if all_questions == num_of_questions_passed:
            return True

def main():
    print("test")

if __name__ == "__main__":
    main()
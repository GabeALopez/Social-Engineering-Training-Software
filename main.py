import Classes, GUI_App
import tkinter as tk

def main():
    testuser = Classes.User("test", 'test')
    user1 = Classes.User('Gavin', 'gavin@example.com')
    user2 = Classes.User('Thomas', 'thomas@example.com')
    user3 = Classes.User('Alexander', 'alexander@example.com')
    user4 = Classes.User('Gabriel', 'gabriel@example.com')
    user5 = Classes.User('Zach', 'zach@example.com')
    testuser.save_to_database()
    user1.save_to_database()
    user2.save_to_database()
    user3.save_to_database()
    user4.save_to_database()
    user5.save_to_database()
    app = GUI_App.App()

if __name__ == "__main__":
    main()


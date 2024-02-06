"""
    Class User handles all the attributes of our movie patrons
"""

import json
import ToolUser

class User:
    user_counter = 0  # Class variable!!!!! is works for all instances of the class!!!!

    aID          = ""
    aAccountName = ""
    aFirstName   = ""
    aLastName    = ""
    aBirthDate   = ""       # variable type is date
    aEmail       = ""
    aPassword    = ""       # Probably don't want it to just exist like that as plain text ...
    aPassword    = ""

    def __init__(self, aID, aAcN, aFiN, aLaN, aBiD, aEma, aPas, aPas2):
        self.aID          = aID
        self.aAccountName = aAcN
        self.aFirstName   = aFiN
        self.aLastName    = aLaN
        self.aBirthDate   = aBiD
        self.aEmail       = aEma
        self.aPassword    = aPas
        self.aPassword2   = aPas2       # Dennis: There's probably a better way to check for identical password

    # getter/setter methods
    def set_user_info(self):
        pass

    def get_user_info(self):
        pass




# ============================================= Mara's Code Starts Here =============================================




# will be using this variable to skip creating an account if it was already created

has_account = False

# creating a method that saves an instance of the user object.


def create_account():
    global has_account
    aAccountName = input("Choose your username: ")
    aFirstName = input("First Name: ")
    aLastName = input("Last Name: ")
    aBirthDate = str(ToolUser.check_date_input())        # check if it's the right format
    aEmail = ToolUser.email_checker()                    # check if it's the right format
    aPassword = ToolUser.repeat_password_check()

    has_account = True
    user = User(aAccountName, aFirstName, aLastName, aBirthDate, aEmail, aPassword, aPassword)
    user_info = user.__dict__  # convert the new user instance to a dictionary

    print("Your account was successfully created!")
    return user_info

# saves the instance in the json file


def load_save_account():
    try:
        with open("user.json", "r") as users_archive:
            try:
                data = json.load(users_archive)
                saved_users = data.get('users', [])
                User.user_counter = data.get('user_counter', 0)
            except json.decoder.JSONDecodeError:
                # in case of empty or invalid json file
                saved_users = []
    except FileNotFoundError:
        saved_users = []
    # if the users doesn't have an account it will call the create function and save it along with the retrieved info
    if not has_account:
        new_user_info = create_account()
        new_user_info['aID'] = User.user_counter
        # Combine the retrieved info with the new. important otherwise it will be overwritten
        all_users = saved_users + [new_user_info]

        with open("user.json", "w") as users_archive:
            data = {'users': all_users, 'user_counter': User.user_counter}
            json.dump(data, users_archive, indent=2)


load_save_account()


# method to log in.
# should only pe possible when an account has been created.
# user should be able to do certain actions whereas a guest user not.

# checking the status
is_logged = False


def log_in():
    global has_account
    global is_logged
    if has_account is True:
        print("Now let us get started. Let's log in!")
        entered_username = input("Please enter your username: ")
        entered_password = input("Please enter your password: ")
        with open("user.json", "r") as users_archive:         # should I move this outside the function?
            try:                                                       # I am using it in a lot of places after all
                my_json = json.load(users_archive)
            except json.decoder.JSONDecodeError:
                my_json = {'users': [], 'user_counter': 0}
        actual_password = ToolUser.search_the_password(my_json, entered_username)

        if entered_password == actual_password:
            print("You have successfully logged in!")
            is_logged = True
        else:
            print("The password or the username is incorrect, please try again")


log_in()

# function to log-out. checks the status and then 'logs out'...
# it only changes the status


def log_out():
    global is_logged
    if is_logged is True:
        print("You have successfully logged out")
        is_logged = False
    else:
        print("Don't worry, you were not logged in")


log_out()
print("here i called the log out function so is_logged should be False: ")
print("is_logged is", is_logged)


def search_and_modify(json_file):
    # prompts the user about what needs to be saved
    account_to_modify = int(input("Please enter your ID: "))
    print("What would you like to modify? ")
    print("1.Account Name\n"
          "2.First Name\n"
          "3.Last Name\n"
          "4.Birth Date\n"
          "5.Password\n"
          "6.Exit")
    thing_to_modify = int(input("Please enter you choice: "))
    new_value = str(input("Enter the new value: "))

    # searches and replaces that data
    for user in json_file.get('users', []):
        if user.get("aID") == account_to_modify:
            if thing_to_modify == 1:
                user["aAccountName"] = new_value
                print("Changes have been saved")
            elif thing_to_modify == 2:
                user["aFirstName"] = new_value
                print("Changes have been saved")
            elif thing_to_modify == 3:
                user["aLastName"] = new_value
                print("Changes have been saved")
            elif thing_to_modify == 4:
                new_value = str(ToolUser.check_date_input())
                user["aBirthDate"] = new_value
                print("Changes have been saved")
            elif thing_to_modify == 5:
                new_value = ToolUser.repeat_password_check()
                user["aPassword"] = new_value
                user["aPassword2"] = new_value
                print("Changes have been saved!")
            else:
                print("Invalid choice.")


# opening the json file, calling the modifying function and saving after

with open("user.json", "r") as users_archive:
    data = json.load(users_archive)

search_and_modify(json_file=data)

with open("user.json", "w") as users_archive:
    json.dump(data, users_archive, indent=2)

# function to delete a user


def delete_user(account_to_delete):
    try:
        with open("user.json", "r") as users_archive:
            all_users = json.load(users_archive)

        for user in all_users['users']:
            if user.get("aID") == account_to_delete:
                all_users["users"].remove(user)
                print("Your account and all the associated data has been deleted")

        with open("user.json", "w") as users_archive:
            json.dump(all_users, users_archive, indent=2)

        print("Account has been deleted!")

    except FileNotFoundError:
        print("Something went wrong.")


delete_request = int(input("Please note that the deletion is permanent and the data can't be recovered. Enter your ID: "))

delete_user(delete_request)
from assistant_bot.addressbook import *

FILE_NAME = 'address-book.bin'
BOOK = AddressBook()


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except KeyError:
            return '-Please enter a valid command.' \
                  '\n-If you want to see my feature set input: showcommands'
        except ValueError:
            return "-Enter correct data, please."
        except IndexError:
            return '-Please enter a valid name/phone number/date of birth.'

    return wrapper


@input_error
def hello(*args):
    return "-Hello. How can I help you?" \
           "\n-If you want to see my feature set input: showcommands"


@input_error
def add_record(user_data):
    global BOOK

    return BOOK.add_record(user_data)


@input_error
def remove_record(user_data):
    if len(user_data) < 1:
        raise IndexError
    name = user_data[0]

    if len(BOOK.data) == 0:
        return "-There are no contacts in the phone book." \
               "\n-If you want to add a contact, enter: add 'name' 'phone number' 'birthday'(optional parameter)."

    return BOOK.remove_record(name)


@input_error
def show_all(*args):
    if len(BOOK.data) == 0:
        return "-There are no contacts in the phone book." \
               "\n-If you want to add a contact, enter: add 'name' 'phone number' 'birthday'(optional parameter)."
    contact_list = [f"{record}" for record in BOOK.data.values()]
    return '\n'.join(contact_list)


@input_error
def add_phone(user_data):
    if len(user_data) < 2:
        raise IndexError
    name = user_data[0]
    phone = user_data[1]

    if len(BOOK) == 0:
        return "-There are no contacts in the phone book." \
               "\n-If you want to add a contact, enter: add 'name' 'phone number' 'birthday'(optional parameter)."

    return BOOK.add_phone_record(name, phone)


@input_error
def change_phone(user_data):
    if len(user_data) < 3:
        raise IndexError
    name = user_data[0]
    old_phone = user_data[1]
    new_phone = user_data[2]

    if len(BOOK) == 0:
        return "-There are no contacts in the phone book." \
               "\n-If you want to add a contact, enter: add 'name' 'phone number' 'birthday'(optional parameter)."

    return BOOK.change_phone_record(name, old_phone, new_phone)


@input_error
def remove_phone(user_data):
    if len(user_data) < 2:
        raise IndexError
    name = user_data[0]
    phone = user_data[1]

    if len(BOOK) == 0:
        return "-There are no contacts in the phone book." \
               "\n-If you want to add a contact, enter: add 'name' 'phone number' 'birthday'(optional parameter)."

    return BOOK.remove_phone_record(name, phone)


@input_error
def add_birthday(user_data):
    if len(user_data) < 2:
        raise IndexError
    name = user_data[0]
    birthday = user_data[1]

    if len(BOOK) == 0:
        return "-There are no contacts in the phone book." \
               "\n-If you want to add a contact, enter: add 'name' 'phone number' 'birthday'(optional parameter)."

    return BOOK.add_birthday_record(name, birthday)


@input_error
def change_birthday(user_data):
    if len(user_data) < 2:
        raise IndexError
    name = user_data[0]
    birthday = user_data[1]

    if len(BOOK) == 0:
        return "-There are no contacts in the phone book." \
               "\n-If you want to add a contact, enter: add 'name' 'phone number' 'birthday'(optional parameter)."

    return BOOK.change_birthday_record(name, birthday)


@input_error
def date_to_birth(user_data):
    if len(user_data) < 1:
        raise IndexError
    name = user_data[0]

    if len(BOOK) == 0:
        return "-There are no contacts in the phone book." \
               "\n-If you want to add a contact, enter: add 'name' 'phone number' 'birthday'(optional parameter)."
    if name not in BOOK.data:
        raise ValueError

    return BOOK.data[name].days_to_birthday()


@input_error
def remove_birthday(user_data):
    if len(user_data) < 1:
        raise IndexError
    name = user_data[0]

    if len(BOOK) == 0:
        return "-There are no contacts in the phone book." \
               "\n-If you want to add a contact, enter: add 'name' 'phone number' 'birthday'(optional parameter)."

    return BOOK.remove_birthday_record(name)


@input_error
def search_record(user_data):
    if len(user_data) < 1:
        raise IndexError
    user_data = user_data[0]

    if len(BOOK) == 0:
        return "-There are no contacts in the phone book." \
               "\n-If you want to add a contact, enter: add 'name' 'phone number' 'birthday'(optional parameter)."

    return BOOK.search_record(user_data)


@input_error
def advanced_search_record(user_data):
    if len(user_data) < 1:
        raise IndexError
    user_data = user_data[0]

    if len(BOOK) == 0:
        return "-There are no contacts in the phone book." \
               "\n-If you want to add a contact, enter: add 'name' 'phone number' 'birthday'(optional parameter)."

    return BOOK.advanced_search_record(user_data)


@input_error
def show_commands(*args):
    return "-I can such commands as: " \
           "\n 1. hello - Greetings message." \
           "\n 2. add 'name' 'phone' 'birthday' - Adds record the contact with {name} and {phone number} " \
           "and {birthday} (optional parameter) to the book." \
           "\n 3. remove 'name' - Removes record {name}." \
           "\n 4. showall - Show the list of all contacts in the phone book." \
           "\n 5. addphone 'name' 'phone' - Adds {phone} number to contact {name}." \
           "\n 6. changephone 'name' 'old phone' 'new phone' - Changes the {old phone} to the {new phone} " \
           "of the contact {name}." \
           "\n 7. removephone 'name' 'phone' - Removes the {phone} of the contact {name}." \
           "\n 8. addbirthday 'name' 'phone' - Adds {birthday} to contact {name}." \
           "\n 9. changebirthday 'name' 'birthday' - Changes the {old birthday} to the {new birthday} " \
           "of the contact {name}." \
           "\n 10. datetobirth {name} - Calculates the number of days until the birthday contact {name}." \
           "\n 11. removebirthday 'name' 'birthday' - Removes the {birthday} of the contact {name}." \
           "\n 12. search 'name' - Searches records by the {name}." \
           "\n 13. asearch 'name or phone or birthday or multiple characters' - Searches for a records by the " \
           r"specified criteria except special characters like .^$*+?{}[]\|()." \
           "\n 14. changephone 'name' 'old phone number' 'new phone number' - Changes the old phone number " \
           "to the new phone number {name}." \
           "\n 15. exit or close or . (dot) or goodbye or bye - Terminates program execution."


@input_error
def exit_func(*args):
    return "-Good bye!"


EXIT = (".", "good bye", "goodbye", "close", "exit", 'bye')
COMMANDS = {'hello': hello,
            'add': add_record,
            'remove': remove_record,
            'addphone': add_phone,
            'changephone': change_phone,
            'removephone': remove_phone,
            'showall': show_all,
            'search': search_record,
            'asearch': advanced_search_record,
            'addbirth': add_birthday,
            'changebirth': change_birthday,
            'datetobirth': date_to_birth,
            'removebirth': remove_birthday,
            'showcommands': show_commands}


@input_error
def handler(user_input):
    if not user_input.lower().startswith(tuple(COMMANDS.keys())):
        raise KeyError
    else:
        command = user_input.split()[0].lower()
        data = user_input.split()[1:]
        return COMMANDS[command](data)


def main():
    print("""Hello. I am CLI (Command Line Interface) or your personal bot helper.\
    \nI can work with phone book and calendar.\
    \nIf you want to see my feature set input: showcommands""")

    while True:
        user_command = input('>>> ')
        if user_command.lower().startswith(EXIT):
            print(exit_func())
            break
        print(handler(user_command))


if __name__ == "__main__":
    main()

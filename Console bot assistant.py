CONTACT_BOOK = dict()


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)

        except KeyError:
            print('\n-Please enter a valid command.'
                  '\n If you want to see my feature set input: showcommands')
        except ValueError:
            print('\n-Please enter a valid name/phone number.')
        except IndexError:
            print("-Enter correct data, please.")

    return wrapper


@input_error
def hello(*args):
    print("-Hello. How can I help you."
          "\n If you want to see my feature set input: showcommands")


@input_error
def contact_add(user_data):
    global CONTACT_BOOK
    name = user_data.split()[1]
    contact = user_data.split()[2]

    if name in CONTACT_BOOK:
        print(f"-The name '{name}' already exists in the phone book. "
              f"\n If you want to change the contact enter: change 'contact name' 'phone number'")
    else:
        if not contact.replace('-', '').replace('+', '').isdigit():
            raise ValueError
        CONTACT_BOOK[name] = contact
        print(f"-You successfully add '{name}' with phone number '{contact}' in phone book")


@input_error
def show_all(*args):
    if len(CONTACT_BOOK) == 0:
        print("-There are no contacts in the phone book. "
              "\n If you want to add a contact, enter: add 'name' 'phone number'")
    else:
        print(f"-Contact book have {len(CONTACT_BOOK)} contacts:")
        [print('- ', name, contact) for name, contact in CONTACT_BOOK.items()]


@input_error
def change_contact(user_data):
    name = user_data.split()[1]
    contact = user_data.split()[2]

    if len(CONTACT_BOOK) == 0:
        print("-There are no contacts in the phone book. "
              "\n If you want to add a contact, enter: add 'name' 'phone number'")
    elif name in CONTACT_BOOK:
        old_num = CONTACT_BOOK[name]
        CONTACT_BOOK[name] = contact
        print(f"-You have successfully changed contact {name} with phone number '{old_num}' at '{contact}'")
    else:
        raise ValueError


@input_error
def show_phone(user_data):
    name = user_data.split()[1]

    if len(CONTACT_BOOK) == 0:
        print("-There are no contacts in the phone book. "
              "\n If you want to add a contact, enter: add 'name' 'phone number'")
    elif name in CONTACT_BOOK:
        print(name, CONTACT_BOOK[name])
    else:
        raise ValueError


@input_error
def show_commands(*args):
    print("-I can such commands as:"
          "\n add 'name' 'phone' - Adds a contact {name} and {phone number} to a book"
          "\n showall - Show a list of all contacts in the phone book"
          "\n phone 'name' - Show a contact with name {name}"
          "\n change 'name' 'phone number' - Changes phone number {name}")


@input_error
def exit_func(*args):
    print("-Good bye!")


EXIT = (".", "good bye", "goodbye", "close", "exit", 'bye')
COMMANDS = {'hello': hello,
            'add': contact_add,
            'showall': show_all,
            'phone': show_phone,
            'change': change_contact,
            'showcommands': show_commands}


@input_error
def handler(user_input):

    if not user_input.startswith(tuple(COMMANDS.keys())):
        raise KeyError
    else:
        command = user_input.split()[0]
        data = user_input
        return COMMANDS[command](data)


def main():
    print("""Hello. I am CLI (Command Line Interface) or your personal bot helper.\
    \nI can work with phone book and calendar.\
    \nIf you want to see my feature set input: showcommands""")

    while True:
        user_command = input('>>> ').lower()
        if user_command.startswith(EXIT):
            exit_func()
            break
        handler(user_command)

if __name__ == "__main__":
    main()

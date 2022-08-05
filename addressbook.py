import re
from pathlib import Path
from re import findall
from collections import UserDict
from datetime import datetime


class Field:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @value.deleter
    def value(self):
        del self.__value


class Name(Field):
    pass


class Phone(Field):

    @staticmethod
    def verify_phone(value):
        clean_phone = value.replace('38', '', 1) if value.startswith('38') else value.replace('+38', '', 1)

        if len(value) > 13 or len(value) < 10:
            raise ValueError("-Invalid phone number length. Please enter a valid phone in the range 10-13 numbers.")

        if not clean_phone.isdigit():
            raise ValueError(
                "-Phone must be only a number. Please enter the correct phone (e.g. +380937890123 or 0934567890).")

        if len(clean_phone) != 10:
            raise ValueError("-Invalid lenght phone number. Please enter the correct phone.")

        if not clean_phone.startswith('0'):
            raise ValueError("-Phone number must start with '0' or '+380'. Please enter the correct phone.")

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.verify_phone(value)
        self.__value = value


class Birthday(Field):

    @staticmethod
    def verify_birthday(value):
        clean_birth = value.replace('.', '')
        if not clean_birth.isdigit():
            raise ValueError("-Invalid date format. Date must be only a number.")

        if len(clean_birth) < 6 or len(clean_birth) > 8:
            raise ValueError("-Invalid date format. Please enter date in the format: DD.MM.YYYY or D.M.YYYY")

        if len(value.split('.')) != 3 or '' in value.split('.'):
            raise ValueError(
                "-Invalid date format. Please enter date in the format: DD.MM.YYYY or D.M.YYYY, with separator as dot.")

        date = int(value.split('.')[0])
        month = int(value.split('.')[1])
        year = int(value.split('.')[2])

        if len(str(year)) != 4:
            raise ValueError("-Invalid year format. Year must be four-digit number (e.g. 1995).")

        if month < 1 or month > 12:
            raise ValueError("-Invalid month format. Month must be in 1-12 (e.g. 8 or 08).")

        if date < 1 or date > 31 and month in [1, 3, 5, 7, 8, 10, 12]:
            raise ValueError(
                f"-Invalid date fomat. In {datetime(1900, month, 12).strftime('%B')} no more than 31 days (e.g. 7 or 07).")

        if date < 1 or date > 30 and month in [4, 6, 9, 11]:
            raise ValueError(
                f"-Invalid date fomat. In {datetime(1900, month, 12).strftime('%B')} no more than 30 days (e.g. 8 or 08).")

        if year % 4 == 0 and month == 2 and 1 > date > 29:
            raise ValueError("-Invalid date format. February of a leap year cannot have more than 29 days.")

        if year % 4 and month == 2 and 1 > date > 28:
            raise ValueError("-Invalid date format. February cannot have more than 28 days.")

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.verify_birthday(value)
        self.__value = datetime.strptime(value, "%d.%m.%Y").date()


class Record:

    def __init__(self, name, phone=None, birthday=None):
        self.name = name if isinstance(name, Name) else Name(name)
        self.phones = list()
        self.birthday = None

        if phone:
            self.phones.append(phone if isinstance(phone, Phone) else Phone(phone))

        if birthday:
            self.birthday = birthday if isinstance(birthday, Birthday) else Birthday(birthday)

    def __str__(self):
        return f"{self.name} {self.phones} {self.birthday}"

    def __repr__(self):
        return f"{self.name} {self.phones} {self.birthday}"

    def add_phone(self, phone):
        if isinstance(phone, Phone):
            return self.phones.append(phone)

        self.phones.append(Phone(phone))
        return "-You successfully add new phone number to contact."

    def change_phone(self, old_phone, new_phone):
        if not isinstance(old_phone, Phone):
            old_phone = Phone(old_phone)

        if not isinstance(new_phone, Phone):
            new_phone = Phone(new_phone)

        for phone in self.phones:
            if old_phone.value == phone.value:
                self.phones.remove(phone)
                self.phones.append(new_phone)
                return f"-You have successfully changed your phone number to {new_phone}."
        else:
            return "-Old phone number not found."

    def remove_phone(self, phone):
        if not isinstance(phone, Phone):
            phone = Phone(phone)

        for phone_number in self.phones:
            if phone_number.value == phone.value:
                self.phones.remove(phone_number)
                return f"-Phone number removed."
        return "-Phone number not found."

    def add_birthday(self, birthday):
        if self.birthday:
            return "-Field 'birthday' already exist. \n-If you want to change the date of birth " \
                   "please enter the command: changebirth 'contact name' 'new date to birth.'"
        self.birthday = Birthday(birthday)
        return "-You successfully add date to birth."

    def change_birthday(self, birthday):
        self.birthday = Birthday(birthday)
        return f"-You have successfully changed birthday to {birthday}."

    def remove_birthday(self):
        self.birthday = None
        return "-Field birthday deleted."

    def days_to_birthday(self):
        today = datetime.today().date()

        if self.birthday:
            birthday = self.birthday.value.replace(year=today.year)
            if birthday > today:
                day_to_birth = (birthday - today).days
            else:
                day_to_birth = (birthday.replace(birthday.year + 1) - today).days

            return f"There are {day_to_birth} days left until the birthday."

        return """-The number of days cannot be counted. Field "Birthday" is empty."""


class AddressBook(UserDict):

    def __getstate__(self):
        state = self.__dict__.copy()
        return state

    def __setstate__(self, state):
        self.__dict__ = state

    def __str__(self):
        return f"{self.data}"

    def __repr__(self):
        return f"{self.data}"

    def add_record(self, record):
        if not isinstance(record, Record):
            record = Record(*record)

        if record.name.value not in self.data:
            self.data.update({record.name.value: record})
            return f"-You successfully add contact {record} in address book."
        else:
            return f"""-Name '{record.name.value}' already exist in address book."""

    def add_phone_record(self, name, phone):
        if name not in self.data:
            return f"-Record '{name}' not found."

        return self.data[name].add_phone(phone)

    def change_phone_record(self, name, old_phone, new_phone):
        if name not in self.data:
            return f"-Record '{name}' not found."

        return self.data[name].change_phone(old_phone, new_phone)

    def remove_phone_record(self, name, number):
        if name not in self.data:
            return f"-Record '{name}' not found."

        return self.data[name].remove_phone(number)

    def add_birthday_record(self, name, birthday):
        if name not in self.data:
            return f"-Record '{name}' not found."

        return self.data[name].add_birthday(birthday)

    def change_birthday_record(self, name, birthday):
        if name not in self.data:
            return f"-Record '{name}' not found."

        return self.data[name].change_birthday(birthday)

    def remove_birthday_record(self, name):
        if name not in self.data:
            return f"-Record '{name}' not found."

        if not self.data[name].birthday:
            return f"-Field {name}'s contact 'birthday' is empty."

        return self.data[name].remove_birthday()

    @staticmethod
    def verify_number(n):
        if not isinstance(n, int):
            raise ValueError("-The number of output pages must be number.")

        if n <= 0:
            raise ValueError("-The number of output pages must not be less than or equal to 0.")

    def iterator(self, n=0):
        self.verify_number(n)
        records = list(self.data.items())

        if not n or len(records) <= n:
            book = '\n'.join([f"{record[0]}: {record[1]}" for record in records])
            yield book
        else:
            while records:
                result = '\n'.join([f'{record[0]}: {record[1]}' for record in records[:n]])
                records = records[n:]
                yield result

        raise StopIteration("-StopIterationError. The whole book is on screen.")

    def search_record(self, value):
        matches = [str(self.data[record]) for record in self.data if value == record]

        return "-Record not found." if not matches else "\n".join(matches)

    def advanced_search_record(self, value):
        matches = list()

        if [symb for symb in value if symb in r'.^$*+?{}[]\|()']:
            raise ValueError('-Incorrect search {value}.')
        for record in self.data.values():
            if findall(str(value), str(record), flags=re.IGNORECASE):
                matches.append(str(record))

        return "-Record not found." if not matches else "\n".join(matches)

    def remove_record(self, name):
        if name not in self.data:
            return f"-Record '{name}' not found."

        del self.data[name]
        return f"-Record {name} deleted."

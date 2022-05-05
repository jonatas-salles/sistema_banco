import re

class Client():

    @property
    def name(self):
        return self.__name
    
    @property
    def cpf(self):
        return self.__cpf

    @property
    def birthdate(self):
        return self.__birthdate

    @property
    def email(self):
        return self.__email

    @name.setter
    def name(self, client_name):
        if type(client_name) == type(str()):
            self.__name = client_name
        else:
            print("Name must be a string")

    @cpf.setter
    def cpf(self, client_cpf):
        if validateCPF(client_cpf):
            self.__cpf = client_cpf
        else:
            print("CPF not found")

    @email.setter
    def email(self, client_email):
        if not re.match(r'^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$', client_email):
            print('Email not in the correct pattern. Correct pattern: username@company.domain')
        else:
            self.__email = client_email

    @birthdate.setter
    def birthdate(self, client_birthdate):
        if not re.match(r'[0-9]{1,4}[\_|\-|\/|\|][0-9]{1,2}[\_|\-|\/|\|][0-9]{1,4}', client_birthdate):
            print('Birthdate is not in the correct pattern. Correct pattern: dd/mm/yyyy')
        else:
            self.__birthdate = client_birthdate

    def create_Account():
        client = Client()
        client.name = input("Name: ")
        client.cpf = input("CPF: ")
        client.birthdate = input("Nascimento: ")
        client.email = input("Email: ")

def validateCPF(cpf):
    if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
        print('CPF is not in the correct pattern. Correct pattern: xxx.xxx.xxx-xx')
    else:	
        numbers = [int(digit) for digit in cpf if digit.isdigit()]
        first_validation = sum(a * b for a, b in zip(numbers[0:9], range(10, 1, -1)))
        expected = (first_validation * 10 % 11) % 10
        if numbers[9] != expected:
            return False

        second_validation = sum(a * b for a, b in zip(numbers[0:10], range(11, 1, -1)))
        expected = (second_validation * 10 % 11) % 10
        if numbers[10] != expected:
            return False
        return True



def menu():
    print(f''' {'='*10} Salles Bank {'='*10}
    [1] Access your account
    [2] Create new account
    [0] Exit
    ''')
    option = input("Type in your option: ")
    while option != "0":
        match option.split():
            case["1"]:
                print("Still working")
                menu()
            case["2"]:
                Client.create_Account()
                menu()
            case["0"]:
                print("Thanks for using our system")
                break
            case _:
                print("Select a valid option")
                menu()
        option = input("Type in your option: ")

menu()
import re
import pandas as pd
from excelData import *

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
        def validateName(name):
            if re.match(r'[^a-zA-Z]', name):
                print()
                print("Name must be only letters")
                name = input('''Try Again.

[0] Menu
Name: ''')
                if name == "0":
                    menu()
                else:	
                    validateName(name)
            self.__name = name
            return True

        if validateName(client_name):
            pass

    @cpf.setter
    def cpf(self, client_cpf):
        def validateCPF(cpf):
            if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
                print()
                print('CPF is not in the correct pattern. Correct pattern: xxx.xxx.xxx-xx')
                cpf = input('''Try again. 

[0] Menu                
CPF: ''')
                if cpf == "0":
                    menu()
                else:	
                    validateCPF(cpf)
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
            self.__cpf = cpf
            return True

        if validateCPF(client_cpf):
            pass
        else:
            print("CPF not found, stoping register")
            menu()

    @birthdate.setter
    def birthdate(self, client_birthdate):
        def validateBirthdate(birthdate):
            if not re.match(r'[0-9]{1,4}[\_|\-|\/|\|][0-9]{1,2}[\_|\-|\/|\|][0-9]{4}', birthdate):
                print()
                print('Birthdate is not in the correct pattern. Correct pattern: dd/mm/yyyy')
                birthdate = input('''Try again. 
                    
[0] Menu
Birthdate: ''')
                if birthdate == "0":
                    menu()
                else:
                    validateBirthdate(birthdate)
            self.__birthdate = birthdate
            return True

        if validateBirthdate(client_birthdate):
            pass

    @email.setter
    def email(self, client_email):
        def validateEmail(email):
            if not re.match(r'^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$', email):
                print()
                print('Email not in the correct pattern. Correct pattern: username@company.domain')
                email = input('''Try again. 

[0] Menu
Email: ''')
                if email == "0":
                    menu()
                else:
                    validateEmail(email)
            self.__email = email
            return True
        
        if validateEmail(client_email):
            pass

    def create_Account():
        client = Client()
        client.name = input("Name: ")
        client.cpf = input("CPF: ")
        client.birthdate = input("Nascimento: ")
        client.email = input("Email: ")
        client.balance = 100

        print(f''' {'='*10} Client Data {'='*10}

    Name: {client.name}
    CPF: {client.cpf}
    Birthdate: {client.birthdate}
    Email: {client.email}
    ''')

        df = pd.DataFrame({f'Name': [client.name],
                            'Cpf': [client.cpf],
                            'Birthdate': [client.birthdate],
                            'Email': [client.email],
                            'balance': [client.balance]})

        readExcel(df)

class Account(Client):
    def __init__(self):
        super().__init__()


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
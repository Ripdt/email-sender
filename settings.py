import os
import json
import sys

from os.path import exists

jsonFile = "settings.json"

def changeSettings():
    option = ''
    account = readSettings()
    while (option != 'c'):
        os.system("cls")
        printMenu(account)
        option = input("opção: ")
        processOption(option, account)

    json_object = json.dumps(account, indent=4)

    with open("settings.json", "w") as outfile:
        outfile.write(json_object)


def readSettings():
    if (exists(jsonFile)):
        return json.load(open(jsonFile))
    return {
        "email": "",
        "senha": "",
        "app-password": "gbsr xapy yeoq vsou",
        "server": "smtp.gmail.com",
        "porta": 465
    }
        
def printMenu(account):
    print('CONFIGURAÇÕES\n')
    printEmailInformation(account)
    printOptionsFromMenu()

def printEmailInformation(account):
    print('ESTES SÃO SEUS DADOS:')
    print("email........." + account["email"])
    print("senha........." + account["senha"])
    print("app-password.." + account["app-password"])
    print("server........" + account["server"])
    print("porta........." + str(account["porta"]))

def printOptionsFromMenu():
    print("\nQUAL DESEJA ALTERAR?\n")
    print("insira 'e' para 'email'")
    print("insira 's' para 'senha'")
    print("insira 'a' para 'app-password'")
    print("insira 'S' para 'server'")
    print("insira 'p' para 'porta'")
    print("\ninsira 'c' para cancelar configuração\n")

def processOption(option, account):
    if (option == 'e'):
        account['email'] = input('email: ')
    elif (option == 's'):
        account["senha"] = input('senha: ')
    elif (option == 'a'):
        account["app-password"] = input('app-password')
    elif (option == 'S'):
        account["server"] = input('server: ')
    elif (option == 'p'):
        account["porta"] = input('porta: ')

if __name__ == "__main__":
    globals()[sys.argv[1]]()
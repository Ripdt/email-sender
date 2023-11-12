import os
import json
import sys

from os.path import exists

jsonFile = "settings.json"

def changeSettings():
    option = ''
    emailJSON = readSettings()
    while (option != 'c'):
        printMenu(emailJSON)
        option = input('opção: ')
        processOption(option, emailJSON)

    json_object = json.dumps(emailJSON, indent=4)

    with open("settings.json", "w") as outfile:
        outfile.write(json_object)


def readSettings():
    if (exists(jsonFile)):
        return json.load(open(jsonFile))
    return {
        "email": "",
        "senha": "",
        "app-password": "gbsr xapy yeoq vsou"
    }
        
def printMenu(emailJSON):
    print('CONFIGURAÇÕES')
    print('')
    printEmailInformation(emailJSON)
    printOptionsFromMenu()

def printEmailInformation(emailJSON):
    print('ESTES SÃO SEUS DADOS:')
    print("email........." + emailJSON["email"])
    print("senha........." + emailJSON["senha"])
    print("app-password.." + emailJSON["app-password"])

def printOptionsFromMenu():
    print('')
    print('QUAL DESEJA ALTERAR?')
    print('')
    print('insira "e" para "email"')
    print('insira "s" para "senha"')
    print('insira "a" para "app-password"')
    print('')
    print('insira "c" para cancelar configuração')
    print('')

def processOption(option, emailJSON):
    if (option == 'e'):
        emailJSON['email'] = input('email: ')
    elif (option == 's'):
        emailJSON["password"] = input('senha: ')
    elif (option == 'a'):
        emailJSON["app-password"] = input('app-password')

if __name__ == '__main__':
    globals()[sys.argv[1]]()
from email import message
import ssl
import smtplib
import sys

import json

from os import system

def getBody():
    print("Insira o corpo do e-mail. Ctrl + D ou Ctrl + Z ( Windows ) para finalizar.\n")
    body = ''
    while True:
        try:
            line = input()
        except EOFError:
            break
        body += line + "\n"
    return body

def printEmail(email):
    print("\n--------------- EMAIL ----------------\n")
    print("De: " + email["From"])
    print("Para: " + email["To"])
    print("Assunto: " + email["Subject"])
    print("\n" + email.get_content())
    print("\n------------ FIM DO EMAIL ------------\n")


def sendEmail(accountStr):
    account = json.loads(str(accountStr).replace("'", '"'))
    email = message.EmailMessage()
    email["From"] = account["email"]
    email["To"] = input("Para quem deseja enviar o e-mail? ")
    email["Subject"] = input("Qual o assunto do e-mail? ")
    email.set_content(getBody())
    printEmail(email)
    if (input('Deseja continuar? (s ou n) ') == 's'):
        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL(account["server"], account["porta"], context=context) as smtp:
                smtp.login(account["email"], account["senha"])
                smtp.sendmail(email["From"], email["To"], email.as_string())

                print('\nE-mail enviado com sucesso')
        except smtplib.SMTPAuthenticationError:
            print('Erro de autenticação. Verifique suas configurações')
        # except smtplib.SSLERROR:
        #     print('a')
    system('pause')

import settings
if __name__ == "__main__" and sys.argv.count(sys.argv) > 0:
    globals()[sys.argv[1]](sys.argv[2])
else:
    sendEmail(settings.readSettings().__str__())
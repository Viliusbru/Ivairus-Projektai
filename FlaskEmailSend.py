from flask import Flask, render_template, request
from calendar import isleap
import smtplib
from email.message import EmailMessage
from os import environ
from string import Template

password = environ.get('slaptazodis')

def funkcija(emailas, subject, zinute):
        
    email = EmailMessage()
    email['from'] = 'Python'
    email['to'] = emailas
    email['subject'] = subject
    email.set_content(zinute)


    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo() # žiūrėkite, kaip į pasisveikinimą su serveriu
        smtp.starttls() # inicijuojame šifruotą kanalą
        smtp.login('bandymas147852@gmail.com', password) # nurodome prisijungimo duomenis
        smtp.send_message(email) # išsiunčiame žinutę


funkcija('viliusbru@gmail.com','asdasd','asdasdasdasd')
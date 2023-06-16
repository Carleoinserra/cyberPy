#!/usr/bin/env python3
import cgi

# Ottenere i dati dal form HTML
form = cgi.FieldStorage()
username = form.getvalue("username")
password = form.getvalue("password")

# Stampare i dati in console
print("Username:", username)
print("Password:", password)

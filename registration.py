#!/usr/bin/env python3

import cgi
import cgitb

cgitb.enable()

# Get the form data
form = cgi.FieldStorage()
name = form.getvalue('name')
email = form.getvalue('email')
password = form.getvalue('password')
confirm_password = form.getvalue('confirm_password')
gender = form.getvalue('gender')
country = form.getvalue('country')

# Check if passwords match
if password != confirm_password:
    print('Content-type: text/html')
    print()
    print('<h1>Passwords do not match!</h1>')
else:
    # Save the user's data to a database or file
    # ...

    print('Content-type: text/html')
    print()
    print('<h1>User registered successfully!</h1>')
    print(f'<p>Name: {name}</p>')
    print(f'<p>Email: {email}</p>')
    print(f'<p>Gender: {gender}</p>')
    print(f'<p>Country: {country}</p>')

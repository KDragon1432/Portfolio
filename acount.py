#!/usr/bin/python
import cgi
import csv
f = open("accounts.csv")
data = f.read()
accounts = data.split('\n')
def htmlTop():
	print'''Content-type:text/html\n\n
	<!DOCTYPE html>
	<html>
		<head>
			<meta charaset="utf-8"/>
			<title> </title>
		</head>
		<body>'''
def htmlTail():
	print '''</body>
	</html>'''
def main():
	formData = cgi.FieldStorage()
	htmlTop()
	username = formData.getvalue("username")
	email = formData.getvalue("email")
	password = formData.getvalue("password")
	password2 = formData.getvalue("password2")
	
	
	
	htmlTail()
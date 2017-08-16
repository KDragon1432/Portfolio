#!/user/bin/env python
import cgi
import cgitb
cgitb.enable()
htmlTop = """Content-Type:text/html\n\n
<!DOCTYPE html>
<html>
        <head>
                <metacharaset="utf-8"/>
                <title> My Account Confirmation </title>
        </head>
        <body>
	"""
htmlTail = """
        </body>
</html>"""
def main():
	formData = cgi.FieldStorage()
	print(htmlTop)
	print("<p> username: {} </p>".format(formData.getvalue("username")))
	print("<p> email: {} </p>".format(formData.getvalue("email")))
	print("<p> password: {} </p>".format(formData.getvalue("password")))
	print(htmlTail)

	
	
main()

<form action="account.py" method="POST">
		username: <br> <input name="username"> <br>
		e-mail: <br> <input name="email"/> <br>
		password: <br> <input name="password"/> <br>
		password again: <br> <input name="password2"/> <br>
		<input type="submit" value="Submit">
		</form>

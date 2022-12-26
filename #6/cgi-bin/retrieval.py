import cgi, cgitb

cgitb.enable()

form = cgi.FieldStorage()

first = form.getvalue('user')
last = form.getvalue('pass')

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head><title>User entered</title></head>")
print("<body>")
print("<h1>User has entered</h1>")
print("<b>Firstname : </b>" + first + "<br>")
print("<br><b>Lastname : </b>" + last + "<br>")
print("")
print("</div>")
print("</body>")
print("</html>")
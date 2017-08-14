var account_list = []
document.getElementById("accounts").innerHTML = account_list
function createAccount() {
	username = document.getElementById("username").value;
	email = documnet.getElementById("email").value;
	password = document.getElementById("password").value;
	password2 = document.getElementById("password2").value;
	var a;
	a = "[" + username + ", " + email + ", " + password + "]";
	account_list.push(a);
	document.getElementById("accounts").innerHTML = "works"
	}
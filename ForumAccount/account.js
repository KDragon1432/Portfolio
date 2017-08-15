var LoggedIn = false;

function LogIn() {
	LoggedIn = true;
	}
function LogOut() {
	LoggedIn = false;
	}

var account_list = [
{"username":"arck2k17", "email":"arck2k17@gmail.com", "password":"girlswhocode"}
];

function createAccount() {
	document.getElementById("accounts").innerHTML = "your account was created";
	username = document.getElementById("usernameCA").value;
	email = document.getElementById("emailCA").value;
	password = document.getElementById("passwordCA").value;
	var new_user;
	new_user = ["username":username, "email":email, "password":password] 
	account_list.push(new_user);
	}
	
function SignIn() {
	username = document.getElementById("usernameLI").value;
	email = document.getElementById("emailLI").value;
	password = document.getElementById("passwordLI").value;
	i = account_list.length
	while (i > 0) {
		if ((username === account_list[i].username) and (password === account_list[i].password)) {
			LogIn()
			}
		i = i - 1;
		}
	}
	
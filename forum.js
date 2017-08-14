function pPost(){
	var new_post = document.getElementById("nPost").value;
	document.getElementById("posts").innerHTML = new_post;
	}
	
function account_error() {
	A_E = document.getElementById("account_error")
	A_E.innerHTML = "your passwords do not match. please try again"
	}
	
	
	

//<p id="posts"> </p>
//<textarea id="nPost" rows="5" cols="80">Post Area</textarea>
//<br> <br>
//<button id="pSubmit" onclick="pPost()"> POST </button>
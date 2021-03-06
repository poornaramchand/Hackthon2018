<?php
session_start ();
function loginForm() {
    echo '
    <div id="loginform">
    <form action="index.php" method="post">
        <p>Please enter your name to continue:</p>
        <label for="name">Name:</label>
        <input type="text" name="name" id="name" autofocus />
        <input type="submit" name="enter" id="enter" value="Enter" />
    </form>
    </div>
    ';
}

if (isset ( $_POST ['enter'] )) {
    if ($_POST ['name'] != "") {
        $_SESSION ['name'] = stripslashes ( htmlspecialchars ( $_POST ['name'] ) );
        $fp = fopen ( "log.html", 'a' );
        fwrite ( $fp, "<b> <div class='msgln' style= 'background-color: #efefef' ><i>User " . $_SESSION ['name'] . " has joined the chat session.</i><br></div></b>" );
        fwrite ( $fp, "<b> <div class='msgln' style= 'background-color: #A5D175'><i> Alpha has joined the chat session.</i><br></div></b>" );
        fwrite ( $fp, "<div class='msglnuser'> <b>Alpha</b> :<i> Hello ! This is Alpha. How may i assist  you .</i> <br >
<style>
.msglnuser{  color: black;
    background-color: #A5D175;
     margin-right: 100px;
    margin-top: 10px;
    margin-left: 15px;
   
display:block;
padding-top: 10px;
    padding-right: 10px;
    padding-bottom: 10px;
    padding-left: 10px;
    border-radius: 15px;
   
</style>
</div>" );
       
        fclose ( $fp );
    } else {
        echo '<span class="error">Please type in a name</span>';
    }
}

if (isset ( $_GET ['logout'] )) {
    
    // Simple exit message
    $fp = fopen ( "log.html", 'a' );
    fwrite ( $fp, "<div class='msgln'><i>User " . $_SESSION ['name'] . " has left the chat session.</i><br></div>" );
    fclose ( $fp );
    unlink('log.html');
   # unlink('db.sqlite3');
    session_destroy ();
    header ( "Location: index.php" ); // Redirect the user
}

?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<style>
body {
	font: 12px arial;
	color: #222;
	text-align:Center ;
	padding: 35px;
}

form,p,span {
	margin: 0;
	padding: 0;
}

input {
	font: 12px arial;
}

a {
	color: #0000FF;
	text-decoration: none;
}

a:hover {
	text-decoration: underline;
}

#wrapper,#loginform {
	margin: 0 auto;
	padding-bottom: 25px;
	background: white;
	width: 504px;
	border: 1px solid #ACD8F0;
}

#loginform {
	padding-top: 18px;
}

#loginform p {
	margin: 5px;
}

#chatbox {
	text-align: left;
	margin: 0 auto;
	margin-bottom: 25px;
	padding: 10px;
	background: #fff;
	height: 270px;
	width: 430px;
	border: 1px solid #ACD8F0;
	overflow: auto;
}

#usermsg {
	width: 395px;
	border: 1px solid #ACD8F0;
}

#submit {
	width: 60px;
}

.error {
	color: #ff0000;
}

#menu {
	padding: 12.5px 25px 12.5px 25px;
}

.welcome {
    font-size: 20px;
	float: left;
}


.logout {
	float: right;
}

.msgln {
	margin: 0 0 2px 0;
}
</style>
<title>CDK Customer Support</title>
</head>
<body>
	<?php
	if (! isset ( $_SESSION ['name'] )) {
		loginForm ();
	} else {
		?>
<div id="wrapper">
		<div id="menu">
			<p class="welcome">
			<img src="cdk logo.png" alt="cdk" style="width:450px;height:50px;">
			<b> Welcome, <?php echo $_SESSION['name']; ?> </b>
			</p>
			<p class="logout">
				<a id="exit" href="#">Exit Chat</a>
			</p>
			<div style="clear: both"></div>
		</div>
		<div id="chatbox"><?php
		if (file_exists ( "log.html" ) && filesize ( "log.html" ) > 0) {
			$handle = fopen ( "log.html", "r" );
			$contents = fread ( $handle, filesize ( "log.html" ) );
			fclose ( $handle );
			
			echo $contents;
		}
		?></div>

		<form name="message" action="">
			<input name="usermsg" type="text" id="usermsg" size="63" autofocus/> <input
				name="submitmsg" type="submit" id="submitmsg" value="Send" />
		</form>
	</div>
	<script type="text/javascript"
		src="http://ajax.googleapis.com/ajax/libs/jquery/1.3/jquery.min.js"></script>
	<script type="text/javascript">
// jQuery Document
$(document).ready(function(){
});

//jQuery Document
$(document).ready(function(){
	//If user wants to end session
	$("#exit").click(function(){
		var exit = confirm("Are you sure you want to end the session?");
		if(exit==true){window.location = 'index.php?logout=true';}		
	});
});

//If user submits the form
$("#submitmsg").click(function(){
		var clientmsg = $("#usermsg").val();
		$.post("post.php", {text: clientmsg, name:' <?php echo $_SESSION['name']?>'});
		getResponse(clientmsg);				
		$("#usermsg").attr("value", "");
		loadLog;
	return false;
});

function getResponse(clientmsg){		
	
	$.ajax({
		url: "http://localhost:5002/chat" ,
		cache: false,
		data:{
			text:clientmsg
		},
		method:'GET',
		contentType:'application/json',
		dataType:'json',
		success: function(data){
			$.post("post.php", {text: data.response, name:'Alpha'});
	  	},
	});
}


function loadLog(){		
	var oldscrollHeight = $("#chatbox").attr("scrollHeight") - 20; //Scroll height before the request
	$.ajax({
		url: "log.html",
		cache: false,
		success: function(html){		
			$("#chatbox").html(html); //Insert chat log into the #chatbox div	
			
			//Auto-scroll			
			var newscrollHeight = $("#chatbox").attr("scrollHeight") - 20; //Scroll height after the request
			if(newscrollHeight > oldscrollHeight){
				$("#chatbox").animate({ scrollTop: newscrollHeight }, 'normal'); //Autoscroll to bottom of div
			}				
	  	},
	});
}

setInterval (loadLog, 2500);
</script>
<?php
	}
	?>
	<script type="text/javascript"
		src="http://ajax.googleapis.com/ajax/libs/jquery/1.3/jquery.min.js"></script>
	<script type="text/javascript">
</script>
</body>
</html>


def signup_nyu_marketplace():
	return"""
<!DOCTYPE html>
<html  >
<head>
  <!-- Site made with Mobirise Website Builder v5.5.2, https://mobirise.com -->
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="generator" content="Mobirise v5.5.2, mobirise.com">
  <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1">
  <link rel="shortcut icon" href="assets/images/nyu.png" type="image/x-icon">
  <meta name="description" content="">
  
  
  <title>signin</title>
  <link rel="stylesheet" href="https://nyu-marketplace.s3.amazonaws.com/assets/bootstrap/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://nyu-marketplace.s3.amazonaws.com/assets/bootstrap/css/bootstrap-grid.min.css">
  <link rel="stylesheet" href="https://nyu-marketplace.s3.amazonaws.com/assets/bootstrap/css/bootstrap-reboot.min.css">
  <link rel="stylesheet" href="https://nyu-marketplace.s3.amazonaws.com/assets/dropdown/css/style.css">
  <link rel="stylesheet" href="https://nyu-marketplace.s3.amazonaws.com/assets/socicon/css/styles.css">
  <link rel="stylesheet" href="https://nyu-marketplace.s3.amazonaws.com/assets/theme/css/style.css">
  <link rel="preload" href="https://fonts.googleapis.com/css?family=Jost:100,200,300,400,500,600,700,800,900,100i,200i,300i,400i,500i,600i,700i,800i,900i&display=swap" as="style" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Jost:100,200,300,400,500,600,700,800,900,100i,200i,300i,400i,500i,600i,700i,800i,900i&display=swap"></noscript>
  <link rel="preload" as="style" href="https://nyu-marketplace.s3.amazonaws.com/assets/mobirise/css/mbr-additional.css"><link rel="stylesheet" href="https://nyu-marketplace.s3.amazonaws.com/assets/mobirise/css/mbr-additional.css" type="text/css">
  <link rel="stylesheet" href="https://nyu-marketplace.s3.amazonaws.com/style_signin.css">
  
  
  
</head>

<body onload="disableSubmit()">
  
  <section data-bs-version="5.1" class="menu menu1 cid-sQbwwgSO5L" once="menu" id="menu1-m">
    

    <nav class="navbar navbar-dropdown navbar-fixed-top navbar-expand-lg">
        <div class="container-fluid">
            <div class="navbar-brand">
                <span class="navbar-logo">
                    
                        <img src="https://nyu-marketplace.s3.amazonaws.com/assets/images/nyu.png" alt="Mobirise" style="height: 3rem;">
                    
                </span>
                <span class="navbar-caption-wrap"><a class="navbar-caption text-white display-7">NEW YORK UNIVERSITY</a></span>
            </div>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-bs-toggle="collapse" data-target="#navbarSupportedContent" data-bs-target="#navbarSupportedContent" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                <div class="hamburger">
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav nav-dropdown nav-right" data-app-modern-menu="true"><li class="nav-item"><a class="nav-link link text-white display-7" >SIGN IN</a>
                    </li></ul>
                
            </div>
        </div>
    </nav>
   
</section>

<section>
    <div style = "margin-top:90px" class="container-fluid" id = "c1">
        <div class="row justify-content-center">
            <div class="title col-md-12 col-lg-10">
                <h3 class="mbr-section-title mbr-fonts-style align-center mb-4 display-2"><strong>Welcome to the NYU MARKETPLACE</strong></h3>
                
            </div>
        </div>
    </div>
<div id = "formm"><div class="wrapper">
        <div class="title-text">
           <div class="title login">
               LOGIN
           </div>
           <div class="title signup">
              SIGN UP
           </div>
        </div>
        <div class="form-container">
           <div class="slide-controls">
              <input type="radio" name="slide" id="login" checked>
              <input type="radio" name="slide" id="signup">
              <label for="login" class="slide login">Login</label>
              <label for="signup" class="slide signup">Signup</label>
              <div class="slider-tab"></div>
           </div>
           <div class="form-inner">
           
              <form id="signinform" action="#" class="login">
                 <div class="field">
                    <input type="text" name="SignInEmail" placeholder="Email Address" required>
                 </div>
                 <div class="field">
                    <input type="password" name="SignInPassword" placeholder="Password" required>
                 </div>
                 
                 <div class="field btn">
                    <div class="btn-layer"></div>
                    <input type="submit" value="Login">
                 </div>
                 <div class="signup-link">
                    Not a member? <a >Signup now</a>
                 </div>
              </form>
              
              <form id="signupform" action="#" class="signup">
                 <div class="field">
                    <label id  = "name" for="name_ip" ></label>
                    <input type="text" id="name_ip" name="Name" placeholder="Enter your Name" required>
                 </div>
                 <div class="field">
                    <label id  = "email"for="email_ip"></label>
                    <input type="email" id="email_ip" name="Email" placeholder="Enter your Email Address" required>
                 </div>
                  <div class="field">
                     <label id  = "phone"for="phone_ip"></label>
                     <input type="tel" id="phone_ip" name="phoneNumber_1" placeholder="Enter your Phone Number 123-456-7890" pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" required>
                  </div>
                 <div class="field">
                    <label id  = "password"for="password_ip"></label>
                    <input type="password" id="password_ip" name="Password" placeholder="Enter your Password" required>
                 </div>
                 <input style = "margin-top: 50px;" type="checkbox" name="terms" id="terms" onchange="activateButton(this)" required> I agree to the Terms & Conditions
            
                 <div class="field btn">
                    <div class="btn-layer"></div>
                    <input id = "submit" type="submit" value="Signup">
                 </div>
              </form>
           </div>
        </div>
 
</section>
<section><a href="https://mobirise.site/s" style="flex: 1 1; height: 3rem; padding-left: 1rem;"></a><p style="flex: 0 0 auto; margin:0; padding-right:1rem;"></section><script src="https://nyu-marketplace.s3.amazonaws.com/assets/bootstrap/js/bootstrap.bundle.min.js"></script>  <script src="https://nyu-marketplace.s3.amazonaws.com/assets/smoothscroll/smooth-scroll.js"></script>  <script src="https://nyu-marketplace.s3.amazonaws.com/assets/ytplayer/index.js"></script>  <script src="https://nyu-marketplace.s3.amazonaws.com/assets/dropdown/js/navbar-dropdown.js"></script>  <script src="https://nyu-marketplace.s3.amazonaws.com/assets/theme/js/script.js"></script>  

<script src="https://code.jquery.com/jquery-3.5.1.min.js" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>

<script>
	$(document).ready(function() {
	    $("#signupform").attr('action', '/signup');
	    $("#signinform").attr('action', '/signin');
	});
	
	
    function disableSubmit() {
     document.getElementById("submit").disabled = true;
    }
   
     function activateButton(element) {
   
         if(element.checked) {
           document.getElementById("submit").disabled = false;
          }
          else  {
           document.getElementById("submit").disabled = true;
         }
   
     }
        /*document.getElementById("submit").onclick = function () {
            location.href = "home.html";
        };*/
        
  
  
    $("#signupform").submit(function(e) {
			console.log('The form will now be submitted.')
			e.preventDefault(); // avoid to execute the actual submit of the form.
			var form = $(this);
			var url = form.attr('action');
			$.ajax({
				type: "POST", url: url,
				data: form.serialize(), //serializes the form's elements.
				success: function(data) {
					console.log(data);
            		alert("User Created!");
            		location.reload();
        		},
				error: function (data) {
					console.log(data);
					alert("Oops! Something went wrong, please try again.");
				},
        	});
		});
		
		
	$("#signinform").submit(function(e) {
			console.log('The form will now be submitted.')
			e.preventDefault(); // avoid to execute the actual submit of the form.
			var form = $(this);
			var url = form.attr('action');
			$.ajax({
				type: "POST", url: url,
				data: form.serialize(), //serializes the form's elements.
				success: function(data) {
				    window.sessionStorage.setItem('session_mail',document.forms["signinform"]["SignInEmail"].value);
					console.log(data);
					if(data.toUpperCase() == "LOGIN SUCCESSFUL") {
					    location.replace("https://xj343strre.execute-api.us-east-1.amazonaws.com/home");
					} else {
					    alert(data);
					}
            		//location.reload();
        		},
				error: function (data) {
					console.log(data);
					alert("Oops! Something went wrong, please try again.");
				},
        	});
		});

   </script>
   <script>
    const loginText = document.querySelector(".title-text .login");
    const loginForm = document.querySelector("form.login");
    const loginBtn = document.querySelector("label.login");
    const signupBtn = document.querySelector("label.signup");
    const signupLink = document.querySelector("form .signup-link a");
    signupBtn.onclick = (()=>{
      loginForm.style.marginLeft = "-50%";
      loginText.style.marginLeft = "-50%";
    });
    loginBtn.onclick = (()=>{
      loginForm.style.marginLeft = "0%";
      loginText.style.marginLeft = "0%";
    });
    signupLink.onclick = (()=>{
      signupBtn.click();
      return false;
    });
 </script>
</body>
</html>
"""


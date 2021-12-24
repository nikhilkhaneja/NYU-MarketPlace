def payment():
	return"""
<!DOCTYPE html>
<html  >
<head>
  <!-- Site made with Mobirise Website Builder v5.5.2, https://mobirise.com -->
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="generator" content="Mobirise v5.5.2, mobirise.com">
  <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1">
  <link rel="shortcut icon" href="https://nyu-marketplace.s3.amazonaws.com/assets/images/nyu.png" type="image/x-icon">
  <meta name="description" content="">
  
  
  <title>Payment Gateway</title>
  <link rel="stylesheet" href="https://nyu-marketplace.s3.amazonaws.com/assets/bootstrap/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://nyu-marketplace.s3.amazonaws.com/assets/bootstrap/css/bootstrap-grid.min.css">
  <link rel="stylesheet" href="https://nyu-marketplace.s3.amazonaws.com/assets/bootstrap/css/bootstrap-reboot.min.css">
  <link rel="stylesheet" href="https://nyu-marketplace.s3.amazonaws.com/assets/dropdown/css/style.css">
  <link rel="stylesheet" href="https://nyu-marketplace.s3.amazonaws.com/assets/socicon/css/styles.css">
  <link rel="stylesheet" href="https://nyu-marketplace.s3.amazonaws.com/assets/theme/css/style.css">
  <link rel="preload" href="https://fonts.googleapis.com/css?family=Jost:100,200,300,400,500,600,700,800,900,100i,200i,300i,400i,500i,600i,700i,800i,900i&display=swap" as="style" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Jost:100,200,300,400,500,600,700,800,900,100i,200i,300i,400i,500i,600i,700i,800i,900i&display=swap"></noscript>
  <link rel="preload" as="style" href="https://nyu-marketplace.s3.amazonaws.com/assets/mobirise/css/mbr-additional.css"><link rel="stylesheet" href="https://nyu-marketplace.s3.amazonaws.com/assets/mobirise/css/mbr-additional.css" type="text/css">
  <link rel="stylesheet" href="https://nyu-marketplace.s3.amazonaws.com/payment_style.css">
  
  
  
</head>

<body onload="disableSubmit()">
  
  <section data-bs-version="5.1" class="menu menu1 cid-sQbwwgSO5L" once="menu" id="menu1-m">
    

    <nav class="navbar navbar-dropdown navbar-fixed-top navbar-expand-lg">
        <div class="container-fluid">
            <div class="navbar-brand">
                <span class="navbar-logo">
                    
                        <img src="https://nyu-marketplace.s3.amazonaws.com/assets/images/nyu.png" alt="Mobirise" style="height: 3rem;">
                    
                </span>
                <span class="navbar-caption-wrap"><a class="navbar-caption text-white display-7" href="https://xj343strre.execute-api.us-east-1.amazonaws.com/home" >NEW YORK UNIVERSITY</a></span>
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
                <ul class="navbar-nav nav-dropdown nav-right" data-app-modern-menu="true"><li class="nav-item"><a class="nav-link link text-white display-7" >PAYMENT GATEWAY</a>
                    </li></ul>
                
            </div>
        </div>
    </nav>
   
</section>

<section>
    <div style = "margin-top:90px" class="container-fluid" id = "c1">
        <div class="row justify-content-center">
            <div class="title col-md-12 col-lg-10">
                <h3 class="mbr-section-title mbr-fonts-style align-center mb-4 display-2"><strong>NYU Marketplace Payment Gateway</strong></h3>
                
            </div>
        </div>
    </div>
<div id = "formm"><div class="wrapper">
        
        <div class="form-container">
         
           <div class="form-inner">
           
              <form id="paymentform" action="#" class="signup">
                 <div class="field">
                    <label id  = "name" for="name_ip" ></label>
                    <input type="text" id="name_ip" name="firstname" placeholder="Enter your Name">
                 </div>
                 <div class="field">
                    <label id  = "card"for="card_no"></label>
                    <input type="number" id="card_no" name="lastname" placeholder="Enter your Card Number" onkeypress="limitKeypress(event,this.value,16)">
                 </div>
                  <div class="field">
                     <label id  = "phone"for="phone_ip"></label>
                     <input type="tel" id="phone_ip" name="phoneNumber_1" placeholder="Enter your Phone Number 123-456-7890" pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" required>
                  </div>
                 <div class="field">
                    <label id  = "month"for="month_ip"></label>
                    <input type="date" id="month_ip" name="lastname" placeholder="Enter your Expiry Date (MM/YYYY)" >
                 </div>
                 <div class="field">
                    <label id  = "cvv"for="cvv_ip"></label>
                    <input type="password" id="cvv_ip" name="lastname" placeholder="Enter your CVV" onkeypress="limitKeypress(event,this.value,4)">
                 </div>
                 <div class="field">
                    <label id  = "address"for="addr"></label>
                    <input type="text" id="addr" name="lastname" placeholder="Enter your Address">
                 </div>
                 <div class="field">
                    <label id  = "phone"for="phone_ip"></label>
                    <input type="text" id="phone_ip" name="lastname" placeholder="Enter your City">
                 </div>
                 <div class="field">
                    <label id  = "month"for="zip_ip"></label>
                    <input type="number" id="zip_ip" name="lastname" placeholder="Enter your Zip Code" onkeypress="limitKeypress(event,this.value,5)">
                 </div>
                <input style = "margin-top: 50px;" type="checkbox" name="terms" id="terms" onchange="activateButton(this)" required>  I agree to the Terms & Conditions
                
                 
                 <div class="field btn">
                    <div class="btn-layer"></div>
                    <input id = "submit" type="submit" value="Confirm and Pay">
                 </div>
              </form>
           </div>
        </div>
 
    </section>
    <section><a href="https://mobirise.site/s" style="flex: 1 1; height: 3rem; padding-left: 1rem;"></a><p style="flex: 0 0 auto; margin:0; padding-right:1rem;"></section><script src="https://nyu-marketplace.s3.amazonaws.com/assets/bootstrap/js/bootstrap.bundle.min.js"></script>  <script src="https://nyu-marketplace.s3.amazonaws.com/assets/smoothscroll/smooth-scroll.js"></script>  <script src="https://nyu-marketplace.s3.amazonaws.com/assets/ytplayer/index.js"></script>  <script src="https://nyu-marketplace.s3.amazonaws.com/assets/dropdown/js/navbar-dropdown.js"></script>  <script src="https://nyu-marketplace.s3.amazonaws.com/assets/theme/js/script.js"></script>  
    <script src="https://code.jquery.com/jquery-3.5.1.min.js" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>
<script>
	$(document).ready(function() {
		var user_session = sessionStorage.getItem('session_mail');
		var pid = sessionStorage.getItem('session_pid');
		var pname = sessionStorage.getItem('session_pname');
		var pprice = sessionStorage.getItem('session_pprice');
		var pdesc = sessionStorage.getItem('session_pdesc');
		
	    $("#paymentform").attr('action', '/payment?pid=' + pid + "&pname=" + pname + "&pprice=" + pprice + "&pdesc=" + pdesc + "&userEmail=" + user_session);
	});
	
	$("#paymentform").submit(function(e) {
			console.log('The form will now be submitted.')
			e.preventDefault(); // avoid to execute the actual submit of the form.
			var form = $(this);
			var url = form.attr('action');
			$.ajax({
				type: "POST", url: url,
				data: form.serialize(), //serializes the form's elements.
				success: function(data) {
					console.log(data);
            		alert("Thank you for your purchase. We have sent you an email which has the product information.");
            		location.replace("https://xj343strre.execute-api.us-east-1.amazonaws.com/buysideui");
        		},
				error: function (data) {
					console.log(data);
					alert("Oops! Something went wrong, please try again.");
				},
        	});
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
   </script>
   <script>
  
   function limitKeypress(event, value, maxLength) {
        if (value != undefined && value.toString().length >= maxLength) {
            event.preventDefault();
        }
    }
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

def bid():
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
  <link rel="stylesheet" href="https://nyu-marketplace.s3.amazonaws.com/bid_style.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  
  
</head>

<body onload="disableSubmit()">
  
  <section data-bs-version="5.1" class="menu menu1 cid-sQbwwgSO5L" once="menu" id="menu1-m">
    

    <nav class="navbar navbar-dropdown navbar-fixed-top navbar-expand-lg">
        <div class="container-fluid">
            <div class="navbar-brand">
                <span class="navbar-logo">
                    
                        <img src="https://nyu-marketplace.s3.amazonaws.com/assets/images/nyu.png" alt="Mobirise" style="height: 3rem;">
                    
                </span>
                <span class="navbar-caption-wrap"><a class="navbar-caption text-white display-7" href="https://xj343strre.execute-api.us-east-1.amazonaws.com/home">NEW YORK UNIVERSITY</a></span>
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
                <ul class="navbar-nav nav-dropdown nav-right" data-app-modern-menu="true"><li class="nav-item"><a class="nav-link link text-white display-7" >BIDING GATEWAY</a>
                    </li></ul>
                
            </div>
        </div>
    </nav>
   
</section>

<section>
    <div style = "margin-top:90px" class="container-fluid" id = "c1">
        <div class="row justify-content-center">
            <div class="title col-md-12 col-lg-10">
                <h3 class="mbr-section-title mbr-fonts-style align-center mb-4 display-2"><strong>NYU Marketplace Biding Gateway</strong></h3>
                
            </div>
        </div>
    </div>
<div id = "formm"><div class="wrapper">
        
        <div class="form-container">
         
           <div class="form-inner">
           
              <form action="#" id="bid" class="signup">
                 <div class="field">
                    <label id  = "name" for="name" ></label>
                    <input type="text" id="name" name="name" placeholder="Enter your Name">
                 </div>
               
                  <div class="field">
                     <label id  = "phone_l"for="phone"></label>
                     <input type="tel" id="phone" name="phone" placeholder="Enter your Phone Number 123-456-7890" pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" required>
                  </div>
                
                 <div class="field">
                    <label id = "bid_ippp" for="bid"></label>
                    <input type="number" id="bid" name="bidprice" placeholder="Enter your Bid">
                 </div>
                <div class="field">
                    <label id  = "mail"for="mail_ip"></label>
                    <input type="email" id="mail_ip" name="email" placeholder="Enter yor e-mail ID" >
                 </div>

                     <input style = "margin-top: 50px;"type="checkbox" name="terms" id="terms" onchange="activateButton(this)" required>  I Agree to the Terms & Conditions
                 
                 <div class="field btn">
                    <div class="btn-layer"></div>
                    <input id = "submit" type="submit" value="Confirm and Place Your Bid">
                 </div>
              </form>
           </div>
        </div>
 
    </section>
    <section><a href="https://mobirise.site/s" style="flex: 1 1; height: 3rem; padding-left: 1rem;"></a><p style="flex: 0 0 auto; margin:0; padding-right:1rem;"></section><script src="https://nyu-marketplace.s3.amazonaws.com/assets/bootstrap/js/bootstrap.bundle.min.js"></script>  <script src="https://nyu-marketplace.s3.amazonaws.com/assets/smoothscroll/smooth-scroll.js"></script>  <script src="https://nyu-marketplace.s3.amazonaws.com/assets/ytplayer/index.js"></script>  <script src="https://nyu-marketplace.s3.amazonaws.com/assets/dropdown/js/navbar-dropdown.js"></script>  <script src="https://nyu-marketplace.s3.amazonaws.com/assets/theme/js/script.js"></script>  
<script>
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
   </script>
   <script>
        $(document).ready(function() {
                var price = sessionStorage.session_pid
                $("#bid").attr('action', '/updateBid?p=' + price);
            });
        
         $("#bid").submit(function(e) {
              console.log('The form will now be submitted.')
              e.preventDefault(); 
              var form = $(this);
              var url = form.attr('action');
              $.ajax({
                 type: "POST", url: url,
                 data: form.serialize(), 
                 success: function(data) {
                    console.log(data);
                       alert("Bid Updated");
                       //location.reload();
                   },
                 error: function (data) {
                    console.log(data);
                    alert("Oops! Something went wrong, please try again.");
                 },
                });
           });
   </script
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
 <script type="text/javascript">
    /*
    function minmax(value) 
    {
        var min = 16;
        if(parseInt(value) < min){
            alert('Your Bid is being changed to the Minimum Bid which is ' + (min+1))
            return min+1; 
        }
        else return value;
    }
    */
    </script>
</body>
</html>
"""
def sellside():
    return """
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
  
  
  <title>SELL PRODUCTS</title>
  <link rel="stylesheet" href="https://nyu-marketplace.s3.amazonaws.com/assets/web/assets/mobirise-icons2/mobirise2.css">
  <link rel="stylesheet" href="https://nyu-marketplace.s3.amazonaws.com/assets/bootstrap/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://nyu-marketplace.s3.amazonaws.com/assets/bootstrap/css/bootstrap-grid.min.css">
  <link rel="stylesheet" href="https://nyu-marketplace.s3.amazonaws.com/assets/bootstrap/css/bootstrap-reboot.min.css">
  <link rel="stylesheet" href="https://nyu-marketplace.s3.amazonaws.com/assets/dropdown/css/style.css">
  <link rel="stylesheet" href="https://nyu-marketplace.s3.amazonaws.com/assets/socicon/css/styles.css">
  <link rel="stylesheet" href="https://nyu-marketplace.s3.amazonaws.com/assets/theme/css/style.css">
  <link rel="preload" href="https://fonts.googleapis.com/css?family=Jost:100,200,300,400,500,600,700,800,900,100i,200i,300i,400i,500i,600i,700i,800i,900i&display=swap" as="style" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Jost:100,200,300,400,500,600,700,800,900,100i,200i,300i,400i,500i,600i,700i,800i,900i&display=swap"></noscript>
  <link rel="preload" as="style" href="https://nyu-marketplace.s3.amazonaws.com/assets/mobirise/css/mbr-additional.css"><link rel="stylesheet" href="https://nyu-marketplace.s3.amazonaws.com/assets/mobirise/css/mbr-additional.css" type="text/css">
  <link rel="stylesheet" href="https://nyu-marketplace.s3.amazonaws.com/sell_style.css">
  
  
  
</head>
<style>
   h1 {
       color: green;
   }
    
   select {
       -webkit-appearance: none;
       -moz-appearance: none;
       -ms-appearance: none;
       appearance: none;
       outline: 0;
       color : #222222;
       background: white;
       background-image: none;
       border: 1px solid black;
   }
    
   .select {
       position: relative;
       display: block;
       width: 100%;;
       height: 3em;
       line-height: 3;
       background: white;
       overflow: hidden;
       border-radius: .25em;
   }
    
   select {
       width: 100%;
       height: 100%;
       margin: 0;
       padding: 0 0 0 .5em;
       color: #222222;
       cursor: pointer;
   }
    
   select::-ms-expand {
       display: none;
   }
    
   .select::after {
       content: 'V';
       
       position: absolute;
       top: 0;
       right: 0;
       color : white;
       bottom: 0;
       padding: 0 1em;
       background: #410369;
       pointer-events: none;
   }
    
   .select:hover::after {
       color: white;
   }

   </style>
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
                <ul class="navbar-nav nav-dropdown nav-right" data-app-modern-menu="true"><li class="nav-item"><a class="nav-link link text-white display-7">SELL PRODUCTS</a>
                    </li></ul>
                
            </div>
        </div>
    </nav>
   
</section>
      <section>
         <div style = "margin-top:90px" class="container-fluid" id = "c1">
             <div class="row justify-content-center">
                 <div class="title col-md-12 col-lg-10">
                     <h3 class="mbr-section-title mbr-fonts-style align-center mb-4 display-2"><strong>NYU MARKETPLACE Sell Products   </strong></h3>
                     
                 </div>
             </div>
         </div>
      <div class="wrapper">
       <div class="title-text">
            <div class="title login">
                Place Product for Bidding
            </div>
            <div class="title signup">
               Don't Place Product for Bid
            </div>
         </div>
         <div class="form-container">
            <div class="slide-controls">
               <input type="radio" name="slide" id="login" checked>
               <input type="radio" name="slide" id="signup">
               <label for="login" class="slide login">Place Product for Bidding</label>
               <label for="signup" class="slide signup">Don't Place Product for Bid</label>
               <div class="slider-tab"></div>
            </div>
            <div class="form-inner">
               <form action="#" class="login" id = "signinform">
                  <div class="field">
                     <label id  = "name" for="name_ip_1" ></label>
                     <input type="text" id="name_ip_1" name="name_1" placeholder="Enter the Product Name">
                  </div>
                  <div class="field">
                     <label id  = "info"for="info_ip_1"></label>
                     <input type="textfeild" id="info_ip_1" name="desc_1" placeholder="Enter the Product Information (Max 300 Characters)">
                  </div>
                 <div class="field">
                  <label for="prod_type_1" style = "margin-top: 5px;;color:#410369">Choose the product type:</label>
                  <div class="select">
                     
                     <select name="slct" id="prod_type_1">
                         <option value = "table">Table</option>
                         <option value="chair">Chair</option>
                         <option value="bedframe">Bedframe</option>
                         <option value="mattress">Mattress</option>
                         <option value="fan">Fan</option>
                         <option value="others">Others</option>
                     </select>
                 </div>
                 </div>
                  <div class="field">
                     <label id  = "mail"for="mail_ip_1"></label>
                     <input type="email" id="mail_ip_1" name="email_1" placeholder="Enter your e-mail ID" >
                  </div>
                  <div class="field">
                     <label id  = "phone"for="phone_ip_1"></label>
                     <input type="tel" id="phone_ip_1" name="phoneNumber_1" placeholder="Enter your Phone Number 123-456-7890" pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" required>
                  </div>
                  <div class="field">
                   <label id  = "bid_type"for="bid_type_ip_1"></label>
                   <input type="text" id="bid_type_ip_1" name="yes_1" placeholder="Bid Type" value = 'Yes' disabled>
                  </div>
                  <div class="field">
                     <label id  = "bid_date"for="bid_date_ip_1"></label>
                     <input type="date" id="bid_date_ip_1" name="date_1" placeholder="Enter Bid By Date (DD/MM/YYYY)" >
                  </div>
                  <div class="field">
                     <label id  = "bid_rate"for="bid_rate_ip_1"></label>
                     <input type="number" id="bid_rate_ip_1" name="price_1" placeholder="Enter the Starting Bid Price" >
                  </div>
                  <div class="field">
                     <label id  = "file"for="file_ip_1"></label>
                     <input type="file" id="file_ip_1" name="image_1" placeholder="Upload the product Image" accept="image/*">
                  </div>
               
                <input style = "margin-top: 50px;" type="checkbox" name="terms" id="terms" onchange="activateButton(this)" required>  I agree to the Terms & Conditions
                  
                  <div class="field btn">
                     <div class="btn-layer"></div>
                     <input id = "submit" type="submit" onclick=getImageLink(); value="Place the Product Up for Bidding">
                  </div>
               </form>
               <form action="#" class="signup" id = "signupform">
                  <div class="field">
                    <label id  = "name" for="name_ip_2" ></label>
                    <input type="text" id="name_ip_2" name="name_2" placeholder="Enter the Product Name">
                 </div>
                 <div class="field">
                    <label id  = "info"for="info_ip_2"></label>
                    <input type="textfeild" id="info_ip_2" name="description_2" placeholder="Enter the Product Information (Max 300 Characters)">
                 </div>
                <div class="field">
                  <label for="prod_type_2" style = "margin-top: 5px;;color:#410369">Choose the product type:</label>
                  <div class="select">
                     
                     <select name="slct" id="prod_type_2">
                         <option value = "table">Table</option>
                         <option value="chair">Chair</option>
                         <option value="bedframe">Bedframe</option>
                         <option value="mattress">Mattress</option>
                         <option value="fan">Fan</option>
                         <option value="others">Others</option>
                     </select>
                 </div>
                 </div>
                 <div class="field">
                    <label id  = "mail"for="mail_ip_2"></label>
                    <input type="email" id="mail_ip_2" name="email_2" placeholder="Enter your e-mail ID" >
                 </div>
                 <div class="field">
                    <label id  = "phone"for="phone_ip_2"></label>
                    <input type="tel" id="phone_ip_2" name="phoneNumber_2" placeholder="Enter your Phone Number123-456-7890" pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" required >
                 </div>
                 <div class="field">
                  <label id  = "bid_type"for="bid_type_ip_2"></label>
                  <input type="text" id="bid_type_ip_2" name="no_2" placeholder="Bid Type" value = 'No' disabled>
                 </div>
                <div class="field">
                    <label id  = "buy_rate"for="buy_rate_ip_2"></label>
                    <input type="number" id="buy_rate_ip_2" name="price_2" placeholder="Enter the Sale Price" >
                 </div>
                 <div class="field">
                    <label id  = "file"for="file_ip_2"></label>
                    <input type="file" id="file_ip_2" name="image_2" placeholder="Upload the product Image" accept="image/*">
                 </div>
              
               <input style = "margin-top: 50px;" type="checkbox" name="terms" id="terms" onchange="activateButton(this)" required> I agree to the Terms & Conditions
            
                 <div class="field btn">
                    <div class="btn-layer"></div>
                    <input id = "submit" type="submit" onclick=getImageLinkNB(); value="Place the Product Up for Sale">
                 </div>
               </form>
            </div>
         </div>
      </div>
       </section>
      <section style="background-color: #fff; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif; color:#aaa; font-size:12px; padding: 0; align-items: center; display: flex;"><a href="https://mobirise.site/p" style="flex: 1 1; height: 3rem; padding-left: 1rem;"></a><p style="flex: 0 0 auto; margin:0; padding-right:1rem;"></section><script src="https://nyu-marketplace.s3.amazonaws.com/assets/bootstrap/js/bootstrap.bundle.min.js"></script>  <script src="https://nyu-marketplace.s3.amazonaws.com/assets/smoothscroll/smooth-scroll.js"></script>  <script src="https://nyu-marketplace.s3.amazonaws.com/assets/ytplayer/index.js"></script>  <script src="https://nyu-marketplace.s3.amazonaws.com/assets/dropdown/js/navbar-dropdown.js"></script>  <script src="https://nyu-marketplace.s3.amazonaws.com/assets/embla/embla.min.js"></script>  <script src="https://nyu-marketplace.s3.amazonaws.com/assets/embla/script.js"></script>  <script src="https://nyu-marketplace.s3.amazonaws.com/assets/theme/js/script.js"></script>  
      <script src="https://code.jquery.com/jquery-3.5.1.min.js" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/aws-sdk/2.49.0/aws-sdk.min.js"></script>
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
            $("#signinform").attr('action', '/postProductData');
            $("#signupform").attr('action', '/postProductData');
        });
        
        function getImageLink() {
        
            var bucketRegion = 'us-east-1';
            var IdentityPoolId = 'us-east-1:d686fe8e-8958-40fa-9af7-effa30d33bab';
            
            AWS.config.update({
                region: bucketRegion,
                credentials: new AWS.CognitoIdentityCredentials({
                IdentityPoolId: IdentityPoolId,
                }),
            });
            
            var s3 = new AWS.S3({
                apiVersion: '2006-03-01',
                params: { Bucket: 'nyu-items-store' },
            });
            
            var upload = new AWS.S3.ManagedUpload({
                params: {
                    Bucket: 'nyu-items-store',
                    Key: document.getElementById('file_ip_1').files[0].name,
                    ContentType: 'image/jpeg',
                    Body: document.getElementById('file_ip_1').files[0],
                    ContentDisposition: 'inline',
                },
            });

            var promise = upload.promise();

            promise.then(
                function (data) {
                    alert('Successfully uploaded photo.');
                },
            function (err) {
                return alert('There was an error uploading your photo: ', err.message);
            });
            
            var imageURL = "https://nyu-items-store.s3.amazonaws.com/"+document.getElementById('file_ip_1').files[0].name;
            console.log(imageURL);
            $("#signinform").attr('action', '/postProductData?url=' + imageURL);
        }
        
        function getImageLinkNB() {
            
            var bucketRegion = 'us-east-1';
            var IdentityPoolId = 'us-east-1:d686fe8e-8958-40fa-9af7-effa30d33bab';
            
            AWS.config.update({
                region: bucketRegion,
                credentials: new AWS.CognitoIdentityCredentials({
                IdentityPoolId: IdentityPoolId,
                }),
            });
            
            var s3 = new AWS.S3({
                apiVersion: '2006-03-01',
                params: { Bucket: 'nyu-items-store' },
            });
            
            var upload = new AWS.S3.ManagedUpload({
                params: {
                    Bucket: 'nyu-items-store',
                    Key: document.getElementById('file_ip_2').files[0].name,
                    ContentType: 'image/jpeg',
                    Body: document.getElementById('file_ip_2').files[0],
                    ContentDisposition: 'inline',
                },
            });

            var promise = upload.promise();

            promise.then(
                function (data) {
                    alert('Successfully uploaded photo.');
                },
            function (err) {
                return alert('There was an error uploading your photo: ', err.message);
            });
        
            var imageURL = "https://nyu-items-store.s3.amazonaws.com/"+document.getElementById('file_ip_2').files[0].name;
            $("#signupform").attr('action', '/postProductData?url=' + imageURL);
        }
        
         $("#signinform").submit(function(e) {
              console.log('The form will now be submitted.')
              e.preventDefault(); 
              var form = $(this);
              var url = form.attr('action');
              $.ajax({
                 type: "POST", url: url,
                 data: form.serialize(), 
                 success: function(data) {
                    console.log(data);
                       alert("Product Saved");
                       //location.reload();
                   },
                 error: function (data) {
                    console.log(data);
                    alert("Oops! Something went wrong, please try again.");
                 },
                });
           });
           
           $("#signupform").submit(function(e) {
              console.log('The form will now be submitted.')
              e.preventDefault(); 
              var form = $(this);
              var url = form.attr('action');
              $.ajax({
                 type: "POST", url: url,
                 data: form.serialize(), 
                 success: function(data) {
                    console.log(data);
                       alert("Product Saved");
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
         
         signupBtn.onclick = (()=>{
           loginForm.style.marginLeft = "-50%";
           loginText.style.marginLeft = "-50%";
         });
         loginBtn.onclick = (()=>{
           loginForm.style.marginLeft = "0%";
           loginText.style.marginLeft = "0%";
         });
        
      </script>
   </body>
</html>
"""
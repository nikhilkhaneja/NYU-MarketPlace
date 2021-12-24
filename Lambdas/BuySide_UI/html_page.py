def buyside():
	return"""
<!DOCTYPE html>
<html  >
<head>
  <!-- Site made with Mobirise Website Builder v5.5.2, https://mobirise.com -->
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="generator" content="Mobirise v5.5.2, mobirise.com">
  <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1">
  <link rel="shortcut icon" href="http://nyu-marketplace.s3.amazonaws.com/assets/images/nyu.png" type="image/x-icon">
  <meta name="description" content="">
  <meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests">
  
  
  <title>NYU Marketplace</title>
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

</head>
<style>
    .button {
      background-color: #410369;
      border: none;
      color: white;
      padding: 16px 32px;
      text-align: center;
      font-size: 20px;
      margin-top:30px;
      margin-left:5px;
      opacity: 0.75;
      transition: 0.3s;
      display: inline-block;
      text-decoration: none;
      cursor: pointer;
      width: 230px;
    }
    
    .button:hover {opacity: 1}
    </style>
<body>
  
  <section data-bs-version="5.1" class="menu menu1 cid-sQbwwgSO5L" once="menu" id="menu1-z">
    

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
                <ul class="navbar-nav nav-dropdown nav-right" data-app-modern-menu="true"><li class="nav-item"><a class="nav-link link text-white display-7">LISTINGS</a>
                    </li></ul>
            </div>
        </div>
    </nav>
</section>

<section data-bs-version="5.1" class="slider4 mbr-embla cid-sQbOB8VK8w" id="slider4-10">
    
    <div class="mbr-section-head">
        <h4 class="mbr-section-title mbr-fonts-style align-center mb-0 display-2">
            <strong>Buy at NYU Marketplace</strong></h4>
        <h5 class="mbr-section-subtitle mbr-fonts-style align-center mb-0 mt-2 display-5">View all the items or select a category</h5>
    
    </div>
        <input class = "button" type="button" id="table" onclick="filterElements(this)" value="Table" />
        <input class = "button" type="button" id="chair" onclick="filterElements(this)" value="Chair" />
        <input class = "button" type="button" id="fan" onclick="filterElements(this)" value="Fan" />
        <input class = "button" type="button" id="bedframe" onclick="filterElements(this)" value="BedFrame" />
        <input class = "button" type="button" id="mattress" onclick="filterElements(this)" value="Mattress" />
        <input class = "button" type="button" id="others" onclick="filterElements(this)" value="Others" />

    <div id = "abba" ></div>
</section>
<section style="background-color: #fff; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif; color:#aaa; font-size:12px; padding: 0; align-items: center; display: flex;"><a href="https://mobirise.site/p" style="flex: 1 1; height: 3rem; padding-left: 1rem;"></a><p style="flex: 0 0 auto; margin:0; padding-right:1rem;"></section><script src="https://nyu-marketplace.s3.amazonaws.com/assets/bootstrap/js/bootstrap.bundle.min.js"></script>  <script src="https://nyu-marketplace.s3.amazonaws.com/assets/smoothscroll/smooth-scroll.js"></script>  <script src="https://nyu-marketplace.s3.amazonaws.com/assets/ytplayer/index.js"></script>  <script src="https://nyu-marketplace.s3.amazonaws.com/assets/dropdown/js/navbar-dropdown.js"></script>  <script src="https://nyu-marketplace.s3.amazonaws.com/assets/embla/embla.min.js"></script>  <script src="https://nyu-marketplace.s3.amazonaws.com/assets/embla/script.js"></script>  <script src="https://nyu-marketplace.s3.amazonaws.com/assets/theme/js/script.js"></script>  
<script src="https://code.jquery.com/jquery-3.5.1.min.js" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>
<script>
var json_data;
var count;
var count_table;
var count_chair;
var count_fan;
var count_mattress;
var count_bedframe;
var count_others;
var k = 0;
let table_arr = []
let chair_arr = []
let mattress_arr = []
let bedframe_arr = []
let fan_arr = []
let others_arr = []



$(document).ready(function() {

var k = 0;
product_arr = [];
product_count = 0;
var url = "/getProductData";
				$.ajax({
					url: url,
					type: "GET", 
					datatype:"json" , 
					success: function(data) {
						$("#get_quiz_listing tr").remove(); 
						json_data = JSON.parse(data);
						console.log(json_data)
						count = Object.keys(json_data.Items).length;
                        console.log(count)
for (let i= 0; i < count; i++)
{
    product_arr.push(json_data.Items[i])
    product_count = product_arr.length;
}                     

document.getElementById('abba').innerHTML = " ";

for (let i = 0; i < product_count/3; i++) {
    
diviiiii=document.createElement('div')
diviiiii.id = 'containeriiiii'+i;
diviiiii.className = 'position-relative text-center';
document.getElementById('abba').appendChild(diviiiii);    

divj=document.createElement('div')
divj.id = 'containerj'+i;
divj.className = 'embla mt-4';
document.getElementById('containeriiiii'+i).appendChild(divj);

divk=document.createElement('div')
divk.id = 'containerk'+i;
divk.className = 'embla__viewport container-fluid';
document.getElementById('containerj'+i).appendChild(divk);  

divl = document.createElement('div');
divl.id = 'containerl'+i;
divl.className = 'embla__container';
document.getElementById('containerk'+i).appendChild(divl);

for (let j = 0;j<3;j++){
    div = document.createElement('div');
    div.id = 'container'+j;
    div.className = 'embla__slide slider-image item';
    div.style = 'margin-left: 1rem; margin-right: 1rem;'
    document.getElementById('containerl'+i).appendChild(div);

    divi = document.createElement('div');
    divi.id = 'containeri'+j;
    divi.className = 'slide-content';
    document.getElementById('container'+j).appendChild(divi);

    divii = document.createElement('div');
    divii.id = 'containerii'+j;
    divii.className = 'item-wrapper';
    document.getElementById('containeri'+j).appendChild(divii);

    diviii = document.createElement('div');
    diviii.id = 'containeriii'+j;
    diviii.className = 'item-img';
    document.getElementById('containerii'+j).appendChild(diviii);

    var elem = document.createElement("img");
    if(product_arr[k] != undefined) {
        elem.setAttribute("src", product_arr[k].product_url);
        elem.setAttribute("height", "350");
        elem.setAttribute("width", "300");
        document.getElementById('containeriii'+j).appendChild(elem);
    
        diviiii= document.createElement('div');
        diviiii.id = 'containeriiii'+j;
        diviiii.className = 'item-content';
        let str = ""
        if(product_arr[k].bid_rate == "None") {
            str = "PRODUCT ID : " + product_arr[k].product_id + "<br>PRODUCT NAME : " + product_arr[k].product_name + "<br>PRODUCT PRICE : " + product_arr[k].product_price + "<br>PRODUCT TYPE : " + product_arr[k].product_type + "<br>CANNOT BID THIS PRODUCT";
        } else {
            str = "PRODUCT ID : " + product_arr[k].product_id + "<br>PRODUCT NAME : " + product_arr[k].product_name + "<br>ORIGINAL PRICE : " + product_arr[k].bid_rate + "<br>LATEST PRICE : " + product_arr[k].bidder_price + "<br>PRODUCT TYPE : " + product_arr[k].product_type + "<br>";
        }
        
        const prod_id = product_arr[k].product_id;
        const prod_name = product_arr[k].product_name;
        const prod_price = product_arr[k].product_price;
        const bid_price = product_arr[k].bidder_price;
        const prod_desc = product_arr[k].product_desc;
        
        diviiii.innerHTML = str
        document.getElementById('containeri'+j).appendChild(diviii);
        document.getElementById('containeri'+j).appendChild(diviiii);
    
        if(product_arr[k].bid_type.toLowerCase() === 'yes'){
            var button = document.createElement('button');
            button.type = 'button';
            button.innerHTML = 'Bid Now';
            button.className = 'btn-primary';
            button.style.marginBottom = '30px';
            button.onclick = function() {
                window.sessionStorage.setItem('session_pid', prod_id);
                window.sessionStorage.setItem('session_pname', prod_name);
                window.sessionStorage.setItem('session_pprice', bid_price);
                window.sessionStorage.setItem('session_pdesc', prod_desc);
                location.replace("https://xj343strre.execute-api.us-east-1.amazonaws.com/bid");
            };
            document.getElementById('containeri'+j).appendChild(button);
        }
        else
        {
            var button = document.createElement('button');
            button.type = 'button';
            button.innerHTML = 'Buy Now';
            button.style.color= 'white';
            button.style.background = '#410369';
            button.style.marginBottom = '30px';
            button.onclick = function() {
                window.sessionStorage.setItem('session_pid', prod_id);
                window.sessionStorage.setItem('session_pname', prod_name);
                window.sessionStorage.setItem('session_pprice', prod_price);
                window.sessionStorage.setItem('session_pdesc', prod_desc);
                location.replace("https://xj343strre.execute-api.us-east-1.amazonaws.com/paymentui");
            };
            document.getElementById('containeri'+j).appendChild(button);
        }
        k = k+1;
    }
   } 
}
					},
					error: function (data) {
						console.log(data);
						alert("Oops! Something went wrong, please try again.");
					},
				});

var user_session = sessionStorage.getItem('session_mail');
x = 0;
k = 0;
});

function filterElements(clicked_id) {
var k = 0;
let table_arr = []
let chair_arr = []
let mattress_arr = []
let bedframe_arr = []
let fan_arr = []
let others_arr = []

var url = "/getProductData";
				$.ajax({
					url: url,
					type: "GET", 
					datatype:"json" , 
					success: function(data) {
						$("#get_quiz_listing tr").remove(); 
						json_data = JSON.parse(data);
						console.log(json_data)
						count = Object.keys(json_data.Items).length;
                        console.log(count)
for (let i= 0; i < count; i++)
{
    if (json_data.Items[i].product_type.toLowerCase() == 'chair') {
        chair_arr.push(json_data.Items[i])
        count_chair = chair_arr.length;
    }
    
    if (json_data.Items[i].product_type.toLowerCase() == 'fan') {
        fan_arr.push(json_data.Items[i])
        count_fan = fan_arr.length;
    }
    
    if (json_data.Items[i].product_type.toLowerCase() == 'mattress') {
        mattress_arr.push(json_data.Items[i])
        count_mattress = mattress_arr.length;
    }
    
    if (json_data.Items[i].product_type.toLowerCase() == 'bedframe') {
        mattress_arr.push(json_data.Items[i])
        count_mattress = mattress_arr.length;
    }
    
    if (json_data.Items[i].product_type.toLowerCase() == 'table') {
        mattress_arr.push(json_data.Items[i])
        count_mattress = mattress_arr.length;
    }
    
    if (json_data.Items[i].product_type.toLowerCase() == 'others') {
        others_arr.push(json_data.Items[i])
        count_others = others_arr.length;
    }

}                     

var x = 0;
var y = [];
var q = $(clicked_id).attr("id");

if(q == 'chair') {
    x = count_chair;
    y = chair_arr;
}

if(q == 'fan') {
    x = count_fan;
    y = fan_arr;
}

if(q == 'mattress') {
    x = count_mattress;
    y = mattress_arr;
}

if(q == 'bedframe') {
    x = count_bedframe;
    y = bedframe_arr
}

if(q == 'table') {
    x = count_table;
    y = table_arr;
}

if(q == 'others') {
    x = count_others;
    y = others_arr;
}


document.getElementById('abba').innerHTML = " ";

for (let i = 0; i < x/3; i++) {
    
diviiiii=document.createElement('div')
diviiiii.id = 'containeriiiii'+i;
diviiiii.className = 'position-relative text-center';
document.getElementById('abba').appendChild(diviiiii);    

divj=document.createElement('div')
divj.id = 'containerj'+i;
divj.className = 'embla mt-4';
document.getElementById('containeriiiii'+i).appendChild(divj);

divk=document.createElement('div')
divk.id = 'containerk'+i;
divk.className = 'embla__viewport container-fluid';
document.getElementById('containerj'+i).appendChild(divk);  

divl = document.createElement('div');
divl.id = 'containerl'+i;
divl.className = 'embla__container';
document.getElementById('containerk'+i).appendChild(divl);

for (let j = 0;j<3;j++){
    div = document.createElement('div');
    div.id = 'container'+j;
    div.className = 'embla__slide slider-image item';
    div.style = 'margin-left: 1rem; margin-right: 1rem;'
    document.getElementById('containerl'+i).appendChild(div);

    divi = document.createElement('div');
    divi.id = 'containeri'+j;
    divi.className = 'slide-content';
    document.getElementById('container'+j).appendChild(divi);

    divii = document.createElement('div');
    divii.id = 'containerii'+j;
    divii.className = 'item-wrapper';
    document.getElementById('containeri'+j).appendChild(divii);

    diviii = document.createElement('div');
    diviii.id = 'containeriii'+j;
    diviii.className = 'item-img';
    document.getElementById('containerii'+j).appendChild(diviii);

    var elem = document.createElement("img");
    if(y[k] != undefined) {
        elem.setAttribute("src", y[k].product_url);
        elem.setAttribute("height", "300");
        elem.setAttribute("width", "300");
        document.getElementById('containeriii'+j).appendChild(elem);
    
        diviiii= document.createElement('div');
        diviiii.id = 'containeriiii'+j;
        diviiii.className = 'item-content';
        let str = ""
        if(y[k].bid_rate == "None") {
            str = "PRODUCT ID : " + y[k].product_id + "<br>PRODUCT NAME : " + y[k].product_name + "<br>PRODUCT PRICE : " + y[k].product_price + "<br>PRODUCT TYPE : " + y[k].product_type + "<br>CANNOT BID THIS PRODUCT";
        } else {
            str = "PRODUCT ID : " + y[k].product_id + "<br>PRODUCT NAME : " + y[k].product_name + "<br>ORIGINAL PRICE : " + y[k].bid_rate + "<br>LATEST PRICE : " + y[k].bidder_price + "<br>PRODUCT TYPE : " + y[k].product_type + "<br>";
        }
        
        const prod_id = y[k].product_id;
        const prod_name = y[k].product_name;
        const prod_price = y[k].product_price;
        const bid_price = y[k].bidder_price;
        const prod_desc = y[k].product_desc;
        
        diviiii.innerHTML = str
        document.getElementById('containeri'+j).appendChild(diviii);
        document.getElementById('containeri'+j).appendChild(diviiii);
    
        if(y[k].bid_type.toLowerCase() === 'yes'){
            var button = document.createElement('button');
            button.type = 'button';
            button.innerHTML = 'Bid Now';
            button.className = 'btn-primary';
            button.style.marginBottom = '30px';
            button.onclick = function() {
                window.sessionStorage.setItem('session_pid', prod_id);
                window.sessionStorage.setItem('session_pname', prod_name);
                window.sessionStorage.setItem('session_pprice', bid_price);
                window.sessionStorage.setItem('session_pdesc', prod_desc);
                location.replace("https://xj343strre.execute-api.us-east-1.amazonaws.com/bid");
            };
            document.getElementById('containeri'+j).appendChild(button);
        }
        else
        {
            var button = document.createElement('button');
            button.type = 'button';
            button.innerHTML = 'Buy Now';
            button.style.color= 'white';
            button.style.background = '#410369';
            button.style.marginBottom = '30px';
            button.onclick = function() {
                window.sessionStorage.setItem('session_pid', prod_id);
                window.sessionStorage.setItem('session_pname', prod_name);
                window.sessionStorage.setItem('session_pprice', prod_price);
                window.sessionStorage.setItem('session_pdesc', prod_desc);
                location.replace("https://xj343strre.execute-api.us-east-1.amazonaws.com/paymentui");
            };
            document.getElementById('containeri'+j).appendChild(button);
        }
        k = k+1;
    }
   } 
}
					},
					error: function (data) {
						console.log(data);
						alert("Oops! Something went wrong, please try again.");
					},
				});

var user_session = sessionStorage.getItem('session_mail');
x = 0;
k = 0;
}

</script>
</body>
</html>

"""


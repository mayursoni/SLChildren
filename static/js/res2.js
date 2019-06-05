function checkPass()
{
    //Store the password field objects into variables ...
    var pass1 = document.getElementById('pass1');
    var pass2 = document.getElementById('pass2');
    //Store the Confimation Message Object ...
    var message = document.getElementById('confirmMessage');
    //Set the colors we will be using ...
    var goodColor = "#66cc66";
    var badColor = "#ff6666";
    //Compare the values in the password field 
    //and the confirmation field
    if(pass1.value == pass2.value){
        //The passwords match. 
        //Set the color to the good color and inform
        //the user that they have entered the correct password 
        pass2.style.backgroundColor = goodColor;
        message.style.color = goodColor;
        message.innerHTML = "Passwords Match"
    }else{
        //The passwords do not match.
        //Set the color to the bad color and
        //notify the user.
        pass2.style.backgroundColor = badColor;
        message.style.color = badColor;
        message.innerHTML = "Passwords Do Not Match!"
    }
} 
function validatephone(phone) 
{
    var maintainplus = '';
    var numval = phone.value
    if ( numval.charAt(0)=='+' )
    {
        var maintainplus = '';
    }
    curphonevar = numval.replace(/[\\A-Za-z!"£$%^&\,*+_={};:'@#~,.Š\/<>?|`¬\]\[]/g,'');
    phone.value = maintainplus + curphonevar;
    var maintainplus = '';
    if ( phone.value.length<10)
    {
      document.getElementById("statusP").innerHTML  = "<span class='warning'>Phone number is invalid!</span>";  
    }
    else
    {
        document.getElementById("statusP").innerHTML  = "<span class='valid'>Phone number is valid!</span>";
    }
    phone.focus;
}
function validateadhar(adhar) 
{
    var maintainplus = '';
    var numval = adhar.value
    
    if ( numval.charAt(0)=='+' )
    {
        var maintainplus = '';
    }
    curadharvar = numval.replace(/[\\A-Za-z!"£$%^&\,*+_={};:'@#~,.Š\/<>?|`¬\]\[]/g,'');
    adhar.value = maintainplus + curadharvar;
    var maintainplus = '';
    if ( adhar.value.length<12)
    {
      document.getElementById("statusA").innerHTML  = "<span class='warning'>Adhar card number is invalid!</span>";  
    }
    else
    {
        document.getElementById("statusA").innerHTML  = "<span class='valid'>Adhar card number is valid!</span>";
    }

    adhar.focus;
}
// validates text only
function Validate(txt) {
    txt.value = txt.value.replace(/[^a-zA-Z-'\n\r.]+/g, '');
}
// validate email
function email_validate(email)
{
var regMail = /^([_a-zA-Z0-9-]+)(\.[_a-zA-Z0-9-]+)*@([a-zA-Z0-9-]+\.)+([a-zA-Z]{2,3})$/;

    if(regMail.test(email) == false)
    {
    document.getElementById("status").innerHTML    = "<span class='warning'>Email address is not valid yet.</span>";
    }
    else
    {
    document.getElementById("status").innerHTML	= "<span class='valid'>Thanks, you have entered a valid Email address!</span>";	
    }
}
// validate date of birth
function dob_validate(dob)
{
var regDOB = /^(\d{1,2})[-\/](\d{1,2})[-\/](\d{4})$/;

    if(regDOB.test(dob) == false)
    {
    document.getElementById("statusDOB").innerHTML	= "<span class='warning'>DOB is only used to verify your age.</span>";
    }
    else
    {
    document.getElementById("statusDOB").innerHTML	= "<span class='valid'>Thanks, you have entered a valid DOB!</span>";	
    }
}
function gendervalidate() 
{
    var x = document.getElementById("radios-0").checked;
    var y = document.getElementById("radios-1").checked;
    var z = document.getElementById("radios-2").checked;
    if(x||y||z)
    {
        document.getElementById("statusGender").innerHTML  = "<span class='valid'>Gender Selected successfully!</span>";
    }
    else
    {
    document.getElementById("statusGender").innerHTML  = "<span class='warning'>Select appropriate gender!</span>";   
    }   
}
//validate rating
function ratingvalidate1() 
{
    var x = document.getElementById("radios-0").checked;
    var y = document.getElementById("radios-1").checked;
    var z = document.getElementById("radios-2").checked;
    if(x||y||z)
    {
        document.getElementById("statusRating1").innerHTML  = "<span class='valid'>Rating Selected successfully!</span>";
    }
    else
    {
    document.getElementById("statusRating1").innerHTML  = "<span class='warning'>Select appropriate Rating!</span>";   
    }


    
}



// validate address
function add_validate(address)
{
/*var regAdd = /^(?=.*\d)[a-zA-Z\s\d\/]+$/;
  
    if(regAdd.test(address) == false)
    {
    document.getElementById("statusAdd").innerHTML	= "<span class='warning'>Address is not valid yet.</span>";
    }
    else
    {
    document.getElementById("statusAdd").innerHTML	= "<span class='valid'>Thanks, Address looks valid!</span>";	
    }*/
    var regAdd = document.getElementById('address');
    var letters=/^[0-9A-Za-z/,_ ]+$/;
    var add_len=regAdd.value.length;
    if(!regAdd.value.match(letters)||add_len<20)
    {
        document.getElementById("statusAdd").innerHTML  = "<span class='warning'>Address is not valid yet.</span>";
    }
    else
    {
        document.getElementById("statusAdd").innerHTML  = "<span class='valid'>Thanks, Address looks valid!</span>";
        
        address.focus();
    
    }
}

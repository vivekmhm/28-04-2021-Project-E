import os
from django.http import HttpResponse


file_path= os.path.abspath(__file__)
pro_dir=os.path.dirname(file_path)


def sample(request):
    return HttpResponse("Django Project ") 


def htmlsample1(request):
    return HttpResponse("<h1> Django project - HTML Sample Function with HTML Tags </h1> ") 


def register(request):
    data = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register Page</title>
</head>
<body bgcolor="Grey">  
        <br>  
        <br>  
        <form>  
          
        <label> Firstname </label>         
        <input type="text" name="firstname" size="15"/> <br> <br>  
        <label> Middlename: </label>     
        <input type="text" name="middlename" size="15"/> <br> <br>  
        <label> Lastname: </label>         
        <input type="text" name="lastname" size="15"/> <br> <br>  
          
        <label>   
        Course :  
        </label>   
        <select>  
        <option value="Course">Course</option>  
        <option value="BCA">BCA</option>  
        <option value="BBA">BBA</option>  
        <option value="B.Tech">B.Tech</option>  
        <option value="MBA">MBA</option>  
        <option value="MCA">MCA</option>  
        <option value="M.Tech">M.Tech</option>  
        </select>  
          
        <br>  
        <br>  
        <label>   
        Gender :  
        </label><br>  
        <input type="radio" name="male"/> Male <br>  
        <input type="radio" name="female"/> Female <br>  
        <input type="radio" name="other"/> Other  
        <br>  
        <br>  
          
        <label>   
        Phone :  
        </label>  
        <input type="text" name="country code"  value="+91" size="2"/>   
        <input type="text" name="phone" size="10"/> <br> <br>  
        Address  
        <br>  
        <textarea cols="80" rows="5" value="address">  
        </textarea>  
        <br> <br>  
        Email:  
        <input type="email" id="email" name="email"/> <br>    
        <br> <br>  
        Password:  
        <input type="Password" id="pass" name="pass"> <br>   
        <br> <br>  
        Re-type password:  
        <input type="Password" id="repass" name="repass"> <br> <br>  
        <input type="button" value="Submit"/>  
        </form>  
</body>
</html>
    """
    return HttpResponse(data) 


def home(request):
    file_addr=os.path.join(pro_dir,'home.html')
    fp = open(file_addr,'r')
    data1=fp.read()
    return HttpResponse(data1)
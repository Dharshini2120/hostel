<<<<<<< HEAD
#!C:/Users/Dell/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgitb, pymysql,cgi
from datetime import datetime
cgitb.enable()
a = pymysql.connect(host="localhost", user="root", password="", database="hostel")
b = a.cursor()
print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Dashboard</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">
  <script src="https://cdn.jsdelivr.net/npm/jquery@3.7.1/dist/jquery.slim.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.3/css/all.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <style>
     .navbar {
            background: linear-gradient(45deg, #007bff, #00d4ff);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        }
        .navbar-brand {
            font-weight: 700;
            font-size: 1.8rem;
            text-transform: uppercase;
            letter-spacing: 1.5px;
        }
    .ml-auto {
      margin-right: 100px;
    }
    #a {
      color: white;
      font-size: 20px;
      font-family: 'Times New Roman', Times, serif;
    }
    #a a {
      text-decoration: none;
      color: black;
      font-size: 18px;
    }

    #x a{
        text-decoration: none;
        color: black;
    }
    #t{
       background: linear-gradient(180deg, #1e3c72, #2a5298);
  color:#ECF0F1;
        font-size: 21px;
  width: 20%;
  height: 920px;
    }
#s{
  display: none;
 }
 ul:hover #s{
  display: block;
 }

#b a{
  color: white;
  text-decoration: none;
 }
  #t a{
  color:black;
  text-decoration: none;
 }
 #b #s a{
  color:white;
  text-decoration: none;
 }
 #t #w a{
  color:white;
  text-decoration: none;
 }
 #t #w{
  color:white;
  text-decoration: none;
 }
  body {
            background-color: #f4f7f6;
        }
          .card {
    max-width: 600px;
    background: linear-gradient(135deg, #ffafbd, #ffc3a0);
    padding: 30px;
  
    border-radius: 10px;
    box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.2);
    color: #4f4f4f;
    font-weight: 500;
}
        .card h2 {
            margin-bottom: 30px;
            font-family: 'Helvetica', sans-serif;
            font-weight: bold;
            font-size: 36px;
            color: #333;
            text-align: center;
            letter-spacing: 1px;
            text-transform: uppercase;
            position: relative;
        }
        .card h2:after {
            content: '';
            position: absolute;
            width: 50px;
            height: 3px;
            background: #007bff;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
        }
        .card h5{
        color:white;
        font-weight:600;}
        body {
            background: linear-gradient(to right, #f8f9fa, #e9ecef);
            font-family: Arial, sans-serif;
        }
        .container {
            margin-top: 50px;
        }
        .card {
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        .btn-custom {
            background-color: #007bff;
            color: white;
            border-radius: 20px;
            transition: 0.3s;
        }
        .btn-custom:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
<nav class="navbar navbar-expand-lg-none navbar-dark bg-dark fixed-top">
    <a class="navbar-brand" href="#">Dormitory Haven</a>
        <button type="button" class="navbar-toggler d-sm-block d-lg-none" data-toggle="collapse" data-target="#b">
          <span class="navbar-toggler-icon"></span>
      </button> 
      <div class="collapse navbar-collapse " id="b">
    <ul class="dropdown">Warden      <span class="dropdown-toggle"></span>
      <li  class="dropdown-item" id="s"> <a href="adwnew.py">New</a></li>
       <li  class="dropdown-item" id="s"> <a href="adwex.py">Existing</a></li>
   </ul> 
  <ul class="dropdown"> Student <span class="dropdown-toggle"></span>
        <li  class="dropdown-item" id="s"> <a href="adrb.py">New</a></li>
           <li  class="dropdown-item" id="s"> <a href="adrpp.py">Payment Processing</a></li>
            <li  class="dropdown-item" id="s"> <a href="adral.py">Allocated</a></li>
   </ul> 
      <ul class="dropdown" >Request Orders <span class="dropdown-toggle"></span>
         <li  class="dropdown-item" id="s"> <a href="adreqorder.py">New</a></li>
           <li  class="dropdown-item" id="s"> <a href="adreqorderex.py">Existing</a></li>
       </ul>
   <ul class="dropdown" >Menus <span class="dropdown-toggle"></span>
      <li  class="dropdown-item" id="s"> <a href="admenunew.py">New</a></li>
       <li  class="dropdown-item" id="s"> <a href="admenuex.py">Existing</a></li>
   </ul>
   <ul class="dropdown" >Requested Menu <span class="dropdown-toggle"></span>
      <li  class="dropdown-item" id="s"> <a href="adreqm.py">New</a></li>
       <li  class="dropdown-item" id="s"> <a href="adreex.py">Existing</a></li>
   </ul>

    <ul class="dropdown" >Rooms <span class="dropdown-toggle"></span>
         <li  class="dropdown-item" id="s"> <a href="adrnew.py">New</a></li>
           <li  class="dropdown-item" id="s"> <a href="adrex.py">Existing</a></li>
       </ul>
       <ul class="dropdown" >Scheduling Time <span class="dropdown-toggle"></span>
      <li  class="dropdown-item" id="s"> <a href="adsctnew.py">New</a></li>
       <li  class="dropdown-item" id="s"> <a href="adsctex.py">Existing</a></li>
   </ul>
    <ul class="dropdown" >Feedback <span class="dropdown-toggle"></span>
      <li  class="dropdown-item" id="s"> <a href="adfefood.py">Food</a></li>
       <li  class="dropdown-item" id="s"> <a href="adfemain.py">Maintenance</a></li>
   </ul>
    <ul> <a href="vacation.py" style="text-decoration:none; color:black;">Vacation</a> </ul>
      <hr>
      <ul id="w" ><span class="fa fa-hand-o-left"></span> <a href="home.py" style="color:black;" >Logout</a></ul>
    </nav><br><br>
    <div class="row">
     <nav id="t" class="d-xl-block d-lg-block d-none" style="margin-top:20px;">
      <br> 
<ul class="dropdown">Warden      <span class="dropdown-toggle"></span>
      <li  class="dropdown-item" id="s"> <a href="adwnew.py">New</a></li>
       <li  class="dropdown-item" id="s"> <a href="adwex.py">Existing</a></li>
   </ul> 
  <ul class="dropdown"> Student <span class="dropdown-toggle"></span>
        <li  class="dropdown-item" id="s"> <a href="adrb.py">New</a></li>
           <li  class="dropdown-item" id="s"> <a href="adrpp.py">Payment Processing</a></li>
            <li  class="dropdown-item" id="s"> <a href="adral.py">Allocated</a></li>
   </ul> 
      <ul class="dropdown" >Request Orders <span class="dropdown-toggle"></span>
         <li  class="dropdown-item" id="s"> <a href="adreqorder.py">New</a></li>
           <li  class="dropdown-item" id="s"> <a href="adreqorderex.py">Existing</a></li>
       </ul>
   <ul class="dropdown" >Menus <span class="dropdown-toggle"></span>
      <li  class="dropdown-item" id="s"> <a href="admenunew.py">New</a></li>
       <li  class="dropdown-item" id="s"> <a href="admenuex.py">Existing</a></li>
   </ul>
   <ul class="dropdown" >Requested Menu <span class="dropdown-toggle"></span>
      <li  class="dropdown-item" id="s"> <a href="adreqm.py">New</a></li>
       <li  class="dropdown-item" id="s"> <a href="adreex.py">Existing</a></li>
   </ul>

    <ul class="dropdown" >Rooms <span class="dropdown-toggle"></span>
         <li  class="dropdown-item" id="s"> <a href="adrnew.py">New</a></li>
           <li  class="dropdown-item" id="s"> <a href="adrex.py">Existing</a></li>
       </ul>
       <ul class="dropdown" >Scheduling Time <span class="dropdown-toggle"></span>
      <li  class="dropdown-item" id="s"> <a href="adsctnew.py">New</a></li>
       <li  class="dropdown-item" id="s"> <a href="adsctex.py">Existing</a></li>
   </ul>
    <ul class="dropdown" >Feedback <span class="dropdown-toggle"></span>
      <li  class="dropdown-item" id="s"> <a href="adfefood.py">Food</a></li>
       <li  class="dropdown-item" id="s"> <a href="adfemain.py">Maintenance</a></li>
   </ul>
    <ul> <a href="vacation.py" style="text-decoration:none; color:white;">Vacation</a> </ul>

  <hr>
  <ul  id="w"><span class="fa fa-hand-o-left"></span> <a href="home.py">Logout</a></ul></nav>
  <div class="col-lg-1"></div>
<div  class="col-lg-7 mx-auto">
    <div class="container">
        <form  method="post">
            <div class="card p-4">
            <h2 class="text-center mb-4">Timing Scheduler</h2>
                <h5>Breakfast Time</h5>
                 <div class="row">
                <div class="col-6">
                <div class="form-group">
                    <label for="breakfast_from_time">From</label>
                    <input type="time" class="form-control" id="breakfast_from_time" name="breakfast_from_time" required>
                </div></div>
                    <div class="col-6">
                <div class="form-group">
                    <label for="breakfast_to_time">To</label>
                    <input type="time" class="form-control" id="breakfast_to_time" name="breakfast_to_time" required>
                </div></div></div>

                <h5>Lunch Time</h5>
                <div class="row">
                <div class="col-6">
                <div class="form-group">
                    <label for="lunch_from_time">From</label>
                    <input type="time" class="form-control" id="lunch_from_time" name="lunch_from_time" required>
                </div></div>
                <div class="col-6">
                <div class="form-group">
                    <label for="lunch_to_time">To</label>
                    <input type="time" class="form-control" id="lunch_to_time" name="lunch_to_time" required>
                </div></div></div>

                <h5>Snacks Time</h5>
                <div class="row">
                <div class="col-6">
                <div class="form-group">
                    <label for="snacks_from_time">From</label>
                    <input type="time" class="form-control" id="snacks_from_time" name="snacks_from_time" required>
                </div></div>
                <div class="col-6">
                <div class="form-group">
                    <label for="snacks_to_time">To</label>
                    <input type="time" class="form-control" id="snacks_to_time" name="snacks_to_time" required>
                </div></div></div>

                <h5>Dinner Time</h5>
                <div class="row">
                <div class="col-6">
                <div class="form-group">
                    <label for="dinner_from_time">From</label>
                    <input type="time" class="form-control" id="dinner_from_time" name="dinner_from_time" required>
                </div></div>
                
                <div class="col-6">
                <div class="form-group">
                    <label for="dinner_to_time">To</label>
                    <input type="time" class="form-control" id="dinner_to_time" name="dinner_to_time" required>
                </div></div></div>

                <h5>Study Time</h5>
                <div class="row">
                <div class="col-6">
                <div class="form-group">
                    <label for="study_from_time">From</label>
                    <input type="time" class="form-control" id="study_from_time" name="study_from_time" required>
                </div></div>
                <div class="col-6">
                <div class="form-group">
                    <label for="study_to_time">To</label>
                    <input type="time" class="form-control" id="study_to_time" name="study_to_time" required>
                </div></div></div>
                <input type="submit" class="btn btn-custom btn-block" value="Submit" name="sub">
            </div>
        </form>
    </div>
</body>
</html>

""")
form = cgi.FieldStorage()
sub=form.getvalue("sub")
breakfast_from_time = form.getvalue('breakfast_from_time')
breakfast_to_time = form.getvalue('breakfast_to_time')
lunch_from_time = form.getvalue('lunch_from_time')
lunch_to_time = form.getvalue('lunch_to_time')
snacks_from_time = form.getvalue('snacks_from_time')
snacks_to_time = form.getvalue('snacks_to_time')
dinner_from_time = form.getvalue('dinner_from_time')
dinner_to_time = form.getvalue('dinner_to_time')
study_from_time = form.getvalue('study_from_time')
study_to_time = form.getvalue('study_to_time')
# Function to convert 24-hour to 12-hour with AM/PM
def convert_to_12hr(time_str):
    if time_str:  # Check if the value is not None or empty
        in_time = datetime.strptime(time_str, "%H:%M")
        return in_time.strftime("%I:%M %p")
breakfast_from_time = convert_to_12hr(breakfast_from_time)
breakfast_to_time = convert_to_12hr(breakfast_to_time)
lunch_from_time = convert_to_12hr(lunch_from_time)
lunch_to_time = convert_to_12hr(lunch_to_time)
snacks_from_time = convert_to_12hr(snacks_from_time)
snacks_to_time = convert_to_12hr(snacks_to_time)
dinner_from_time = convert_to_12hr(dinner_from_time)
dinner_to_time = convert_to_12hr(dinner_to_time)
study_from_time = convert_to_12hr(study_from_time)
study_to_time = convert_to_12hr(study_to_time)

if sub!=None:
    query = """INSERT INTO schedule_timing 
    ( breakfast_from_time, breakfast_to_time, lunch_from_time, 
    lunch_to_time, snacks_from_time, snacks_to_time, dinner_from_time, dinner_to_time, 
    study_from_time, study_to_time,Status) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','New')"""%(breakfast_from_time, breakfast_to_time,
              lunch_from_time, lunch_to_time, snacks_from_time, snacks_to_time,
              dinner_from_time, dinner_to_time, study_from_time, study_to_time)
    b.execute(query)
    a.commit()
    print("""<script>alert('Timings Scheduled Successfully');
     location.href="adsctnew.py";</script>""")

=======
#!C:/Users/Dell/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgitb, pymysql,cgi
from datetime import datetime
cgitb.enable()
a = pymysql.connect(host="localhost", user="root", password="", database="hostel")
b = a.cursor()
print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Dashboard</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">
  <script src="https://cdn.jsdelivr.net/npm/jquery@3.7.1/dist/jquery.slim.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.3/css/all.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <style>
     .navbar {
            background: linear-gradient(45deg, #007bff, #00d4ff);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        }
        .navbar-brand {
            font-weight: 700;
            font-size: 1.8rem;
            text-transform: uppercase;
            letter-spacing: 1.5px;
        }
    .ml-auto {
      margin-right: 100px;
    }
    #a {
      color: white;
      font-size: 20px;
      font-family: 'Times New Roman', Times, serif;
    }
    #a a {
      text-decoration: none;
      color: black;
      font-size: 18px;
    }

    #x a{
        text-decoration: none;
        color: black;
    }
    #t{
       background: linear-gradient(180deg, #1e3c72, #2a5298);
  color:#ECF0F1;
        font-size: 21px;
  width: 20%;
  height: 920px;
    }
#s{
  display: none;
 }
 ul:hover #s{
  display: block;
 }

#b a{
  color: white;
  text-decoration: none;
 }
  #t a{
  color:black;
  text-decoration: none;
 }
 #b #s a{
  color:white;
  text-decoration: none;
 }
 #t #w a{
  color:white;
  text-decoration: none;
 }
 #t #w{
  color:white;
  text-decoration: none;
 }
  body {
            background-color: #f4f7f6;
        }
          .card {
    max-width: 600px;
    background: linear-gradient(135deg, #ffafbd, #ffc3a0);
    padding: 30px;
  
    border-radius: 10px;
    box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.2);
    color: #4f4f4f;
    font-weight: 500;
}
        .card h2 {
            margin-bottom: 30px;
            font-family: 'Helvetica', sans-serif;
            font-weight: bold;
            font-size: 36px;
            color: #333;
            text-align: center;
            letter-spacing: 1px;
            text-transform: uppercase;
            position: relative;
        }
        .card h2:after {
            content: '';
            position: absolute;
            width: 50px;
            height: 3px;
            background: #007bff;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
        }
        .card h5{
        color:white;
        font-weight:600;}
        body {
            background: linear-gradient(to right, #f8f9fa, #e9ecef);
            font-family: Arial, sans-serif;
        }
        .container {
            margin-top: 50px;
        }
        .card {
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        .btn-custom {
            background-color: #007bff;
            color: white;
            border-radius: 20px;
            transition: 0.3s;
        }
        .btn-custom:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
<nav class="navbar navbar-expand-lg-none navbar-dark bg-dark fixed-top">
    <a class="navbar-brand" href="#">Dormitory Haven</a>
        <button type="button" class="navbar-toggler d-sm-block d-lg-none" data-toggle="collapse" data-target="#b">
          <span class="navbar-toggler-icon"></span>
      </button> 
      <div class="collapse navbar-collapse " id="b">
    <ul class="dropdown">Warden      <span class="dropdown-toggle"></span>
      <li  class="dropdown-item" id="s"> <a href="adwnew.py">New</a></li>
       <li  class="dropdown-item" id="s"> <a href="adwex.py">Existing</a></li>
   </ul> 
  <ul class="dropdown"> Student <span class="dropdown-toggle"></span>
        <li  class="dropdown-item" id="s"> <a href="adrb.py">New</a></li>
           <li  class="dropdown-item" id="s"> <a href="adrpp.py">Payment Processing</a></li>
            <li  class="dropdown-item" id="s"> <a href="adral.py">Allocated</a></li>
   </ul> 
      <ul class="dropdown" >Request Orders <span class="dropdown-toggle"></span>
         <li  class="dropdown-item" id="s"> <a href="adreqorder.py">New</a></li>
           <li  class="dropdown-item" id="s"> <a href="adreqorderex.py">Existing</a></li>
       </ul>
   <ul class="dropdown" >Menus <span class="dropdown-toggle"></span>
      <li  class="dropdown-item" id="s"> <a href="admenunew.py">New</a></li>
       <li  class="dropdown-item" id="s"> <a href="admenuex.py">Existing</a></li>
   </ul>
   <ul class="dropdown" >Requested Menu <span class="dropdown-toggle"></span>
      <li  class="dropdown-item" id="s"> <a href="adreqm.py">New</a></li>
       <li  class="dropdown-item" id="s"> <a href="adreex.py">Existing</a></li>
   </ul>

    <ul class="dropdown" >Rooms <span class="dropdown-toggle"></span>
         <li  class="dropdown-item" id="s"> <a href="adrnew.py">New</a></li>
           <li  class="dropdown-item" id="s"> <a href="adrex.py">Existing</a></li>
       </ul>
       <ul class="dropdown" >Scheduling Time <span class="dropdown-toggle"></span>
      <li  class="dropdown-item" id="s"> <a href="adsctnew.py">New</a></li>
       <li  class="dropdown-item" id="s"> <a href="adsctex.py">Existing</a></li>
   </ul>
    <ul class="dropdown" >Feedback <span class="dropdown-toggle"></span>
      <li  class="dropdown-item" id="s"> <a href="adfefood.py">Food</a></li>
       <li  class="dropdown-item" id="s"> <a href="adfemain.py">Maintenance</a></li>
   </ul>
    <ul> <a href="vacation.py" style="text-decoration:none; color:black;">Vacation</a> </ul>
      <hr>
      <ul id="w" ><span class="fa fa-hand-o-left"></span> <a href="home.py" style="color:black;" >Logout</a></ul>
    </nav><br><br>
    <div class="row">
     <nav id="t" class="d-xl-block d-lg-block d-none" style="margin-top:20px;">
      <br> 
<ul class="dropdown">Warden      <span class="dropdown-toggle"></span>
      <li  class="dropdown-item" id="s"> <a href="adwnew.py">New</a></li>
       <li  class="dropdown-item" id="s"> <a href="adwex.py">Existing</a></li>
   </ul> 
  <ul class="dropdown"> Student <span class="dropdown-toggle"></span>
        <li  class="dropdown-item" id="s"> <a href="adrb.py">New</a></li>
           <li  class="dropdown-item" id="s"> <a href="adrpp.py">Payment Processing</a></li>
            <li  class="dropdown-item" id="s"> <a href="adral.py">Allocated</a></li>
   </ul> 
      <ul class="dropdown" >Request Orders <span class="dropdown-toggle"></span>
         <li  class="dropdown-item" id="s"> <a href="adreqorder.py">New</a></li>
           <li  class="dropdown-item" id="s"> <a href="adreqorderex.py">Existing</a></li>
       </ul>
   <ul class="dropdown" >Menus <span class="dropdown-toggle"></span>
      <li  class="dropdown-item" id="s"> <a href="admenunew.py">New</a></li>
       <li  class="dropdown-item" id="s"> <a href="admenuex.py">Existing</a></li>
   </ul>
   <ul class="dropdown" >Requested Menu <span class="dropdown-toggle"></span>
      <li  class="dropdown-item" id="s"> <a href="adreqm.py">New</a></li>
       <li  class="dropdown-item" id="s"> <a href="adreex.py">Existing</a></li>
   </ul>

    <ul class="dropdown" >Rooms <span class="dropdown-toggle"></span>
         <li  class="dropdown-item" id="s"> <a href="adrnew.py">New</a></li>
           <li  class="dropdown-item" id="s"> <a href="adrex.py">Existing</a></li>
       </ul>
       <ul class="dropdown" >Scheduling Time <span class="dropdown-toggle"></span>
      <li  class="dropdown-item" id="s"> <a href="adsctnew.py">New</a></li>
       <li  class="dropdown-item" id="s"> <a href="adsctex.py">Existing</a></li>
   </ul>
    <ul class="dropdown" >Feedback <span class="dropdown-toggle"></span>
      <li  class="dropdown-item" id="s"> <a href="adfefood.py">Food</a></li>
       <li  class="dropdown-item" id="s"> <a href="adfemain.py">Maintenance</a></li>
   </ul>
    <ul> <a href="vacation.py" style="text-decoration:none; color:white;">Vacation</a> </ul>

  <hr>
  <ul  id="w"><span class="fa fa-hand-o-left"></span> <a href="home.py">Logout</a></ul></nav>
  <div class="col-lg-1"></div>
<div  class="col-lg-7 mx-auto">
    <div class="container">
        <form  method="post">
            <div class="card p-4">
            <h2 class="text-center mb-4">Timing Scheduler</h2>
                <h5>Breakfast Time</h5>
                 <div class="row">
                <div class="col-6">
                <div class="form-group">
                    <label for="breakfast_from_time">From</label>
                    <input type="time" class="form-control" id="breakfast_from_time" name="breakfast_from_time" required>
                </div></div>
                    <div class="col-6">
                <div class="form-group">
                    <label for="breakfast_to_time">To</label>
                    <input type="time" class="form-control" id="breakfast_to_time" name="breakfast_to_time" required>
                </div></div></div>

                <h5>Lunch Time</h5>
                <div class="row">
                <div class="col-6">
                <div class="form-group">
                    <label for="lunch_from_time">From</label>
                    <input type="time" class="form-control" id="lunch_from_time" name="lunch_from_time" required>
                </div></div>
                <div class="col-6">
                <div class="form-group">
                    <label for="lunch_to_time">To</label>
                    <input type="time" class="form-control" id="lunch_to_time" name="lunch_to_time" required>
                </div></div></div>

                <h5>Snacks Time</h5>
                <div class="row">
                <div class="col-6">
                <div class="form-group">
                    <label for="snacks_from_time">From</label>
                    <input type="time" class="form-control" id="snacks_from_time" name="snacks_from_time" required>
                </div></div>
                <div class="col-6">
                <div class="form-group">
                    <label for="snacks_to_time">To</label>
                    <input type="time" class="form-control" id="snacks_to_time" name="snacks_to_time" required>
                </div></div></div>

                <h5>Dinner Time</h5>
                <div class="row">
                <div class="col-6">
                <div class="form-group">
                    <label for="dinner_from_time">From</label>
                    <input type="time" class="form-control" id="dinner_from_time" name="dinner_from_time" required>
                </div></div>
                
                <div class="col-6">
                <div class="form-group">
                    <label for="dinner_to_time">To</label>
                    <input type="time" class="form-control" id="dinner_to_time" name="dinner_to_time" required>
                </div></div></div>

                <h5>Study Time</h5>
                <div class="row">
                <div class="col-6">
                <div class="form-group">
                    <label for="study_from_time">From</label>
                    <input type="time" class="form-control" id="study_from_time" name="study_from_time" required>
                </div></div>
                <div class="col-6">
                <div class="form-group">
                    <label for="study_to_time">To</label>
                    <input type="time" class="form-control" id="study_to_time" name="study_to_time" required>
                </div></div></div>
                <input type="submit" class="btn btn-custom btn-block" value="Submit" name="sub">
            </div>
        </form>
    </div>
</body>
</html>

""")
form = cgi.FieldStorage()
sub=form.getvalue("sub")
breakfast_from_time = form.getvalue('breakfast_from_time')
breakfast_to_time = form.getvalue('breakfast_to_time')
lunch_from_time = form.getvalue('lunch_from_time')
lunch_to_time = form.getvalue('lunch_to_time')
snacks_from_time = form.getvalue('snacks_from_time')
snacks_to_time = form.getvalue('snacks_to_time')
dinner_from_time = form.getvalue('dinner_from_time')
dinner_to_time = form.getvalue('dinner_to_time')
study_from_time = form.getvalue('study_from_time')
study_to_time = form.getvalue('study_to_time')
# Function to convert 24-hour to 12-hour with AM/PM
def convert_to_12hr(time_str):
    if time_str:  # Check if the value is not None or empty
        in_time = datetime.strptime(time_str, "%H:%M")
        return in_time.strftime("%I:%M %p")
breakfast_from_time = convert_to_12hr(breakfast_from_time)
breakfast_to_time = convert_to_12hr(breakfast_to_time)
lunch_from_time = convert_to_12hr(lunch_from_time)
lunch_to_time = convert_to_12hr(lunch_to_time)
snacks_from_time = convert_to_12hr(snacks_from_time)
snacks_to_time = convert_to_12hr(snacks_to_time)
dinner_from_time = convert_to_12hr(dinner_from_time)
dinner_to_time = convert_to_12hr(dinner_to_time)
study_from_time = convert_to_12hr(study_from_time)
study_to_time = convert_to_12hr(study_to_time)

if sub!=None:
    query = """INSERT INTO schedule_timing 
    ( breakfast_from_time, breakfast_to_time, lunch_from_time, 
    lunch_to_time, snacks_from_time, snacks_to_time, dinner_from_time, dinner_to_time, 
    study_from_time, study_to_time,Status) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','New')"""%(breakfast_from_time, breakfast_to_time,
              lunch_from_time, lunch_to_time, snacks_from_time, snacks_to_time,
              dinner_from_time, dinner_to_time, study_from_time, study_to_time)
    b.execute(query)
    a.commit()
    print("""<script>alert('Timings Scheduled Successfully');
     location.href="adsctnew.py";</script>""")

>>>>>>> c403f4a19814397122cdcefd156ae16b6abcd48e

<<<<<<< HEAD
#!C:/Users/Dell/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql
from datetime import datetime
cgitb.enable()
a = pymysql.connect(host="localhost", user="root", password="", database="hostel")
b = a.cursor()
print("""
<!DOCTYPE html>
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
  height: 530px;
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
          .container {
    max-width: 600px;
    background: linear-gradient(135deg, #ffafbd, #ffc3a0);
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.2);
    color: #4f4f4f;
    font-weight: 500;
}
        .container h2 {
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
        .container h2:after {
            content: '';
            position: absolute;
            width: 50px;
            height: 3px;
            background: #007bff;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
        }
        .form-group label {
            color: white;
        }
        .form-control {
            background-color: #ffffff;
            color: #495057;
            border-radius: 5px;
            border: 1px solid #ced4da;
        }
        .form-control:focus {
            border-color: #007bff;
            box-shadow: 0 0 5px rgba(0, 123, 255, 0.25);
        }
        .btn-register {
            background-color: #007bff;
            border-color: #007bff;
            color: white;
            font-size: 16px;
            font-weight: 600;
            border-radius: 5px;
        }
        .btn-register:hover {
            border-color: #004085;
        }
        .btn-link {
            background-color: red;
            border-color: red;
            color: white;
            font-size: 16px;
            font-weight: 600;
            border-radius: 5px;
        }
        .btn-link:hover {
           text-decoration: none;
           color: black;
           border-color: #4e555b;
        }
        #con h3 {
            font-family: 'Lora', serif;
            font-size: 36px;
            font-weight: 700;
            color: black;
            text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3);
            margin-bottom: 25px;
            letter-spacing: 1px;
        }
        #con p {
            font-family: 'Roboto', sans-serif;
            font-size: 18px;
            color: black;
            line-height: 1.8;
            text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
        } 

</style>
</head>
<body >
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
    <div class="container mt-5" style="height:460px;">
        <h2 class="text-center">Room Registration Form</h2>
        <form id="roomForm" method="post">
            <div class="form-group">
                <label for="room_number">Room Number</label>
                <input type="text" class="form-control" id="room_number" name="Room_Number" required>
            </div>
            <div class="form-group">
                <label for="occupancy">Occupancy</label>
                <input type="number" class="form-control" id="occupancy" name="Occupancy" required>
            </div>
            <div class="form-group">
                <label for="total_capacity">Total Capacity</label>
                <input type="number" class="form-control" id="total_capacity" name="Total_Capacity" required>
            </div>
            <input type="submit" name="sub" class="btn btn-primary" value="Register Room" style="float:right;">
        </form>
    </div>

</body>
</html>


    """)
form = cgi.FieldStorage()
if len(form) != 0:
    submit = form.getvalue("sub")
    if submit != None:
        current_date = datetime.today().strftime("%d-%m-%Y")
        room_number = form.getvalue('Room_Number')
        occupancy = form.getvalue('Occupancy')
        total_capacity = form.getvalue('Total_Capacity')
        query = """INSERT INTO rooms (Room_Number, Occupancy, Total_Capacity,Date,Status) VALUES ('%s', '%s', '%s','%s','Deleted')"""%(room_number, occupancy, total_capacity,current_date)
        b.execute(query)
        a.commit()
        print("""<script>alert('Room registered successfully!');
=======
#!C:/Users/Dell/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql
from datetime import datetime
cgitb.enable()
a = pymysql.connect(host="localhost", user="root", password="", database="hostel")
b = a.cursor()
print("""
<!DOCTYPE html>
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
  height: 530px;
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
          .container {
    max-width: 600px;
    background: linear-gradient(135deg, #ffafbd, #ffc3a0);
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.2);
    color: #4f4f4f;
    font-weight: 500;
}
        .container h2 {
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
        .container h2:after {
            content: '';
            position: absolute;
            width: 50px;
            height: 3px;
            background: #007bff;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
        }
        .form-group label {
            color: white;
        }
        .form-control {
            background-color: #ffffff;
            color: #495057;
            border-radius: 5px;
            border: 1px solid #ced4da;
        }
        .form-control:focus {
            border-color: #007bff;
            box-shadow: 0 0 5px rgba(0, 123, 255, 0.25);
        }
        .btn-register {
            background-color: #007bff;
            border-color: #007bff;
            color: white;
            font-size: 16px;
            font-weight: 600;
            border-radius: 5px;
        }
        .btn-register:hover {
            border-color: #004085;
        }
        .btn-link {
            background-color: red;
            border-color: red;
            color: white;
            font-size: 16px;
            font-weight: 600;
            border-radius: 5px;
        }
        .btn-link:hover {
           text-decoration: none;
           color: black;
           border-color: #4e555b;
        }
        #con h3 {
            font-family: 'Lora', serif;
            font-size: 36px;
            font-weight: 700;
            color: black;
            text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3);
            margin-bottom: 25px;
            letter-spacing: 1px;
        }
        #con p {
            font-family: 'Roboto', sans-serif;
            font-size: 18px;
            color: black;
            line-height: 1.8;
            text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
        } 

</style>
</head>
<body >
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
    <div class="container mt-5" style="height:460px;">
        <h2 class="text-center">Room Registration Form</h2>
        <form id="roomForm" method="post">
            <div class="form-group">
                <label for="room_number">Room Number</label>
                <input type="text" class="form-control" id="room_number" name="Room_Number" required>
            </div>
            <div class="form-group">
                <label for="occupancy">Occupancy</label>
                <input type="number" class="form-control" id="occupancy" name="Occupancy" required>
            </div>
            <div class="form-group">
                <label for="total_capacity">Total Capacity</label>
                <input type="number" class="form-control" id="total_capacity" name="Total_Capacity" required>
            </div>
            <input type="submit" name="sub" class="btn btn-primary" value="Register Room" style="float:right;">
        </form>
    </div>

</body>
</html>


    """)
form = cgi.FieldStorage()
if len(form) != 0:
    submit = form.getvalue("sub")
    if submit != None:
        current_date = datetime.today().strftime("%d-%m-%Y")
        room_number = form.getvalue('Room_Number')
        occupancy = form.getvalue('Occupancy')
        total_capacity = form.getvalue('Total_Capacity')
        query = """INSERT INTO rooms (Room_Number, Occupancy, Total_Capacity,Date,Status) VALUES ('%s', '%s', '%s','%s','Deleted')"""%(room_number, occupancy, total_capacity,current_date)
        b.execute(query)
        a.commit()
        print("""<script>alert('Room registered successfully!');
>>>>>>> c403f4a19814397122cdcefd156ae16b6abcd48e
              location.href="adrnew.py" </script>""")
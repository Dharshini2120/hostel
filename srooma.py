<<<<<<< HEAD
#!C:/Users/Dell/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgitb, pymysql, cgi
from datetime import datetime
cgitb.enable()
a = pymysql.connect(host="localhost", user="root", password="", database="hostel")
b = a.cursor()
form = cgi.FieldStorage()
id=form.getvalue("id")
v="""select * from student where id='%s' """%(id)
b.execute(v)
r=b.fetchall()
status =""
query = "SELECT * FROM rooms"
b.execute(query)
room = b.fetchall()

name=""
email=""
Degree=""
Year=""
Depart=""
Roll=""
for i in r:
   name=i[2]
   email=i[3]
   Degree=i[9]
   Year=i[10]
   Depart=i[11]
   Roll=i[12]

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Dashboard</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.7.1/dist/jquery.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"></script>
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
  height: 563px;
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
        .search-box {
            width: 100%;
            max-width: 500px;
            margin: 0 auto;
        }
        
    </style>
</head>""")
print("""
<body >
<nav class="navbar navbar-expand-lg-none navbar-dark bg-dark fixed-top">
    <a class="navbar-brand" href="#">Dormitory Haven</a>
        <button type="button" class="navbar-toggler d-sm-block d-lg-none" data-toggle="collapse" data-target="#b">
          <span class="navbar-toggler-icon"></span>
      </button> 
      <div class="collapse navbar-collapse " id="b">
     <ul> <a href="sprofile.py?id=%s" style="color:black;">Profile</a></ul>
    <ul class="dropdown">Rooms <span class="dropdown-toggle"></span>
      <li  class="dropdown-item" id="s"> <a href="srooma.py?id=%s">Available</a></li>
       <li  class="dropdown-item" id="s"> <a href="sroomb.py?id=%s">Booking</a></li>
          <li  class="dropdown-item" id="s"> <a href="sroomal.py?id=%s">Allocated</a></li>
   </ul> 

   <ul class="dropdown" >Menus <span class="dropdown-toggle"></span>
          <li  class="dropdown-item" id="s"> <a href="smenu.py?id=%s">New</a></li>
           <li  class="dropdown-item" id="s"> <a href="smenuex.py?id=%s">Existing</a></li>
       </ul>
  <ul> <a href="sst.py?id=%s" style="color:black;">Schedule Timing</a></ul>


        <ul class="dropdown" >Feedback <span class="dropdown-toggle"></span>
          <li  class="dropdown-item" id="s"> <a href="sfnew.py?id=%s">New</a></li>
           <li  class="dropdown-item" id="s"> <a href="sfex.py?id=%s">Existing</a></li>
       </ul>
       <ul class="dropdown" >Vacation <span class="dropdown-toggle"></span>
          <li  class="dropdown-item" id="s"> <a href="vactionnew.py?id=%s">New</a></li>
           <li  class="dropdown-item" id="s"> <a href="vactionex.py?id=%s">Existing</a></li>
       </ul>
     
  <hr>
  <ul  id="w"><span class="fa fa-hand-o-left"></span> <a href="home.py" style="color:black;">Logout</a></ul></nav>  <br> <br>""" % (
id, id, id, id, id, id, id, id,id,id,id))
print("""
    <div class="row">
     <nav id="t" class="d-xl-block d-lg-block d-none" style="margin-top:20px;">
      <br> 
     <ul> <a href="sprofile.py?id=%s" style="color:white;">Profile</a></ul>
      <ul class="dropdown">Rooms <span class="dropdown-toggle"></span>
      <li  class="dropdown-item" id="s"> <a href="srooma.py?id=%s">Available</a></li>
       <li  class="dropdown-item" id="s"> <a href="sroomb.py?id=%s">Booking</a></li>
          <li  class="dropdown-item" id="s"> <a href="sroomal.py?id=%s">Allocated</a></li>
   </ul> 

    <ul class="dropdown" >Menus <span class="dropdown-toggle"></span>
          <li  class="dropdown-item" id="s"> <a href="smenu.py?id=%s">New</a></li>
           <li  class="dropdown-item" id="s"> <a href="smenuex.py?id=%s">Existing</a></li>
       </ul>
  <ul> <a href="sst.py?id=%s" style="color:white;">Schedule Timing</a></ul>


        <ul class="dropdown" >Feedback <span class="dropdown-toggle"></span>
          <li  class="dropdown-item" id="s"> <a href="sfnew.py?id=%s">New</a></li>
           <li  class="dropdown-item" id="s"> <a href="sfex.py?id=%s">Existing</a></li>
       </ul>
       <ul class="dropdown" >Vacation <span class="dropdown-toggle"></span>
          <li  class="dropdown-item" id="s"> <a href="vactionnew.py?id=%s">New</a></li>
           <li  class="dropdown-item" id="s"> <a href="vactionex.py?id=%s">Existing</a></li>
       </ul>
       
  <hr>
  <ul  id="w"><span class="fa fa-hand-o-left"></span> <a href="home.py">Logout</a></ul></nav>
 """ % (id, id, id, id, id, id, id, id,id,id,id))
print("""<div class="col-lg-9"><br><br><br>
<div class="container text-center">
    <img src="./media/ro.jpg" height="300px" width="500px" class="mx-auto d-block">
    <h1 class="text-center">Rooms</h1>

""")
print("""<section class="container my-5">
    <div class="row">
""")

for j in room:
    roo = j[2]
    if j[3] < j[4]:
        status = "Available"
        card_class = "border-success shadow-lg"
    else:
        status = "Room is already booked"
        card_class = "border-danger shadow-lg"

    print(f"""
          <div class="col-lg-4 col-md-6 col-12 mb-4">
            <div class="card {card_class}" style="background: linear-gradient(135deg, #f8f9fa, #e9ecef); border-radius: 15px;">
                <div class="card-body">
                    <h3 class="card-subtitle mb-2 " style="font-family: 'Lora', serif; font-size: 36px; font-weight: 700; color:purple;
    text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3); margin-bottom: 25px; letter-spacing: 1px;" > Room Number: {j[2]}</h3>
                    
                <p class="card-text">
                    <strong>Status: </strong> <span class="{'text-success' if status == 'Available' else 'text-danger'}">{status}</span><br>
                    <strong>Occupancy: </strong> {j[3]} / {j[4]}
                </p>
                """)
    if status == "Available":
        print(f"""
           <form method="post">
               <input type="hidden" value="{name}" name="na">
               <input type="hidden" value="{email}" name="em">
               <input type="hidden" value="{Degree}" name="deg">
               <input type="hidden" value="{Year}" name="yr">
               <input type="hidden" value="{Depart}" name="dep">
               <input type="hidden" value="{Roll}" name="rol">
               <input type="hidden" value="{j[2]}" name="roomno">
               <input  type="submit" class="btn btn-primary" name="sub" value="Book Now"></form>
               """)
    print("""
                </div>
            </div></div>
            
""")


print("""
</div>
</body>
</html>
""")
sub=form.getvalue("sub")
na=form.getvalue("na")
em=form.getvalue("em")
deg=form.getvalue("deg")
yr=form.getvalue("yr")
dep=form.getvalue("dep")
rol=form.getvalue("rol")
roomno=form.getvalue("roomno")
bdate= datetime.now().strftime('%d-%m-%Y')
if sub!=None:
        v="""insert into book (Book_Date,room_no,Student_Name,Email,Degree,Year,Department,Roll_Number,Status) values ('%s','%s','%s','%s','%s','%s','%s','%s','Booked')"""%(bdate,roomno,na,em,deg,yr,dep,rol)
        b.execute(v)
        a.commit()
        print("""<script>alert('You have been Booked Room Successfully');</script>""")
=======
#!C:/Users/Dell/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgitb, pymysql, cgi
from datetime import datetime
cgitb.enable()
a = pymysql.connect(host="localhost", user="root", password="", database="hostel")
b = a.cursor()
form = cgi.FieldStorage()
id=form.getvalue("id")
v="""select * from student where id='%s' """%(id)
b.execute(v)
r=b.fetchall()
status =""
query = "SELECT * FROM rooms"
b.execute(query)
room = b.fetchall()

name=""
email=""
Degree=""
Year=""
Depart=""
Roll=""
for i in r:
   name=i[2]
   email=i[3]
   Degree=i[9]
   Year=i[10]
   Depart=i[11]
   Roll=i[12]

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Dashboard</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.7.1/dist/jquery.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"></script>
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
  height: 563px;
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
        .search-box {
            width: 100%;
            max-width: 500px;
            margin: 0 auto;
        }
        
    </style>
</head>""")
print("""
<body >
<nav class="navbar navbar-expand-lg-none navbar-dark bg-dark fixed-top">
    <a class="navbar-brand" href="#">Dormitory Haven</a>
        <button type="button" class="navbar-toggler d-sm-block d-lg-none" data-toggle="collapse" data-target="#b">
          <span class="navbar-toggler-icon"></span>
      </button> 
      <div class="collapse navbar-collapse " id="b">
     <ul> <a href="sprofile.py?id=%s" style="color:black;">Profile</a></ul>
    <ul class="dropdown">Rooms <span class="dropdown-toggle"></span>
      <li  class="dropdown-item" id="s"> <a href="srooma.py?id=%s">Available</a></li>
       <li  class="dropdown-item" id="s"> <a href="sroomb.py?id=%s">Booking</a></li>
          <li  class="dropdown-item" id="s"> <a href="sroomal.py?id=%s">Allocated</a></li>
   </ul> 

   <ul class="dropdown" >Menus <span class="dropdown-toggle"></span>
          <li  class="dropdown-item" id="s"> <a href="smenu.py?id=%s">New</a></li>
           <li  class="dropdown-item" id="s"> <a href="smenuex.py?id=%s">Existing</a></li>
       </ul>
  <ul> <a href="sst.py?id=%s" style="color:black;">Schedule Timing</a></ul>


        <ul class="dropdown" >Feedback <span class="dropdown-toggle"></span>
          <li  class="dropdown-item" id="s"> <a href="sfnew.py?id=%s">New</a></li>
           <li  class="dropdown-item" id="s"> <a href="sfex.py?id=%s">Existing</a></li>
       </ul>
       <ul class="dropdown" >Vacation <span class="dropdown-toggle"></span>
          <li  class="dropdown-item" id="s"> <a href="vactionnew.py?id=%s">New</a></li>
           <li  class="dropdown-item" id="s"> <a href="vactionex.py?id=%s">Existing</a></li>
       </ul>
     
  <hr>
  <ul  id="w"><span class="fa fa-hand-o-left"></span> <a href="home.py" style="color:black;">Logout</a></ul></nav>  <br> <br>""" % (
id, id, id, id, id, id, id, id,id,id,id))
print("""
    <div class="row">
     <nav id="t" class="d-xl-block d-lg-block d-none" style="margin-top:20px;">
      <br> 
     <ul> <a href="sprofile.py?id=%s" style="color:white;">Profile</a></ul>
      <ul class="dropdown">Rooms <span class="dropdown-toggle"></span>
      <li  class="dropdown-item" id="s"> <a href="srooma.py?id=%s">Available</a></li>
       <li  class="dropdown-item" id="s"> <a href="sroomb.py?id=%s">Booking</a></li>
          <li  class="dropdown-item" id="s"> <a href="sroomal.py?id=%s">Allocated</a></li>
   </ul> 

    <ul class="dropdown" >Menus <span class="dropdown-toggle"></span>
          <li  class="dropdown-item" id="s"> <a href="smenu.py?id=%s">New</a></li>
           <li  class="dropdown-item" id="s"> <a href="smenuex.py?id=%s">Existing</a></li>
       </ul>
  <ul> <a href="sst.py?id=%s" style="color:white;">Schedule Timing</a></ul>


        <ul class="dropdown" >Feedback <span class="dropdown-toggle"></span>
          <li  class="dropdown-item" id="s"> <a href="sfnew.py?id=%s">New</a></li>
           <li  class="dropdown-item" id="s"> <a href="sfex.py?id=%s">Existing</a></li>
       </ul>
       <ul class="dropdown" >Vacation <span class="dropdown-toggle"></span>
          <li  class="dropdown-item" id="s"> <a href="vactionnew.py?id=%s">New</a></li>
           <li  class="dropdown-item" id="s"> <a href="vactionex.py?id=%s">Existing</a></li>
       </ul>
       
  <hr>
  <ul  id="w"><span class="fa fa-hand-o-left"></span> <a href="home.py">Logout</a></ul></nav>
 """ % (id, id, id, id, id, id, id, id,id,id,id))
print("""<div class="col-lg-9"><br><br><br>
<div class="container text-center">
    <img src="./media/ro.jpg" height="300px" width="500px" class="mx-auto d-block">
    <h1 class="text-center">Rooms</h1>

""")
print("""<section class="container my-5">
    <div class="row">
""")

for j in room:
    roo = j[2]
    if j[3] < j[4]:
        status = "Available"
        card_class = "border-success shadow-lg"
    else:
        status = "Room is already booked"
        card_class = "border-danger shadow-lg"

    print(f"""
          <div class="col-lg-4 col-md-6 col-12 mb-4">
            <div class="card {card_class}" style="background: linear-gradient(135deg, #f8f9fa, #e9ecef); border-radius: 15px;">
                <div class="card-body">
                    <h3 class="card-subtitle mb-2 " style="font-family: 'Lora', serif; font-size: 36px; font-weight: 700; color:purple;
    text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3); margin-bottom: 25px; letter-spacing: 1px;" > Room Number: {j[2]}</h3>
                    
                <p class="card-text">
                    <strong>Status: </strong> <span class="{'text-success' if status == 'Available' else 'text-danger'}">{status}</span><br>
                    <strong>Occupancy: </strong> {j[3]} / {j[4]}
                </p>
                """)
    if status == "Available":
        print(f"""
           <form method="post">
               <input type="hidden" value="{name}" name="na">
               <input type="hidden" value="{email}" name="em">
               <input type="hidden" value="{Degree}" name="deg">
               <input type="hidden" value="{Year}" name="yr">
               <input type="hidden" value="{Depart}" name="dep">
               <input type="hidden" value="{Roll}" name="rol">
               <input type="hidden" value="{j[2]}" name="roomno">
               <input  type="submit" class="btn btn-primary" name="sub" value="Book Now"></form>
               """)
    print("""
                </div>
            </div></div>
            
""")


print("""
</div>
</body>
</html>
""")
sub=form.getvalue("sub")
na=form.getvalue("na")
em=form.getvalue("em")
deg=form.getvalue("deg")
yr=form.getvalue("yr")
dep=form.getvalue("dep")
rol=form.getvalue("rol")
roomno=form.getvalue("roomno")
bdate= datetime.now().strftime('%d-%m-%Y')
if sub!=None:
        v="""insert into book (Book_Date,room_no,Student_Name,Email,Degree,Year,Department,Roll_Number,Status) values ('%s','%s','%s','%s','%s','%s','%s','%s','Booked')"""%(bdate,roomno,na,em,deg,yr,dep,rol)
        b.execute(v)
        a.commit()
        print("""<script>alert('You have been Booked Room Successfully');</script>""")
>>>>>>> c403f4a19814397122cdcefd156ae16b6abcd48e

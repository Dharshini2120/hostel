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
s=""
for kk in r:
    s=kk[2]
query = "SELECT * FROM rooms"
b.execute(query)
room = b.fetchall()
roo=""
for k in room:
    roo=k[2]
student_query = """ 
    SELECT s.Name, b.Year, b.room_no 
    FROM book b
    INNER JOIN student s ON b.Student_Name = s.Name
    WHERE s.Name = %s AND b.Status = 'Paid' 
"""

b.execute(student_query, (s,))
students = b.fetchall()

rn = ""
for ll in students:
    rn = ll[2]



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
        </style></head>""")
print("""
<body >
<nav class="navbar navbar-expand-lg-none navbar-dark bg-dark fixed-top">
    <a class="navbar-brand" href="#">Dormitory Haven</a>
        <button type="button" class="navbar-toggler d-sm-block d-lg-none" data-toggle="collapse" data-target="#b">
          <span class="navbar-toggler-icon"></span>
      </button> 
      <div class="collapse navbar-collapse " id="b">
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
      <ul id="w" ><span class="fa fa-hand-o-left"></span> <a href="home.py" style="color:black;" >Logout</a></ul>
    </nav>  <br> <br>""" % ( id, id, id, id, id, id, id, id, id, id, id))
print("""
    <div class="row">
     <nav id="t" class="d-xl-block d-lg-block d-none">
      <br> <br>
     
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
  """ % (id, id, id, id, id, id, id, id, id, id, id))
for i in r:
    print("""<div class="col-lg-9">
    <div class="container mt-5">
        <h2 class="text-center">Hostel Vacation Leave Request Form</h2>
        <form method="post">
            <div class="form-group">
                <label for="studentName">Student Name</label>
                <input type="text" class="form-control" name="st" value="%s"  readonly>
            </div>
                <input type="hidden" class="form-control" name="roll" value="%s"  required>
                <input type="hidden" class="form-control" name="rn"  value="%s" required>
                <input type="hidden" class="form-control"  name="de" value="%s" required>
                <input type="hidden" class="form-control"  name="yr" value="%s" required>
                   <input type="hidden" class="form-control"  name="dep" value="%s" required>
            <div class="form-group">
                <label for="leave">Leaving Date</label>
                <input type="date" class="form-control" name="leave" required>
            </div>
            <div class="form-group">
                <label for="reason">Reason for Vacation</label>
                <textarea class="form-control" name="reason" rows="3" placeholder="Enter reason for leave" required></textarea>
            </div>
            <input type="submit" class="btn btn-primary btn-block" name="sub" value="Submit Request" >
        </form>
    </div>
    
    
    </body>
    </html>
    
    """%(i[2],i[12],rn,i[9],i[10],i[11]))
sub=form.getvalue("sub")
st=form.getvalue("st")
roll=form.getvalue("roll")
rn=form.getvalue("rn")
de=form.getvalue("de")
yr=form.getvalue("yr")
dep=form.getvalue("dep")
leave=form.getvalue("leave")
reason=form.getvalue("reason")
bdate= datetime.now().strftime('%d-%m-%Y')
if leave:
    fleave = datetime.strptime(leave, "%Y-%m-%d").strftime("%d-%m-%Y")
    if sub!=None:
            v="""insert into vacation (Reg_Date,Student_Name,Roll_No,Room_No,Degree,Year,Department,Leaving_Date,Reason,Status) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','Requested')"""%(bdate,st,roll,rn,de,yr,dep,fleave,reason)
            b.execute(v)
            a.commit()
            print("""<script>alert('You have been Successfully Registered Your Vacation Form');</script>""")
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
s=""
for kk in r:
    s=kk[2]
query = "SELECT * FROM rooms"
b.execute(query)
room = b.fetchall()
roo=""
for k in room:
    roo=k[2]
student_query = """ 
    SELECT s.Name, b.Year, b.room_no 
    FROM book b
    INNER JOIN student s ON b.Student_Name = s.Name
    WHERE s.Name = %s AND b.Status = 'Paid' 
"""

b.execute(student_query, (s,))
students = b.fetchall()

rn = ""
for ll in students:
    rn = ll[2]



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
        </style></head>""")
print("""
<body >
<nav class="navbar navbar-expand-lg-none navbar-dark bg-dark fixed-top">
    <a class="navbar-brand" href="#">Dormitory Haven</a>
        <button type="button" class="navbar-toggler d-sm-block d-lg-none" data-toggle="collapse" data-target="#b">
          <span class="navbar-toggler-icon"></span>
      </button> 
      <div class="collapse navbar-collapse " id="b">
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
      <ul id="w" ><span class="fa fa-hand-o-left"></span> <a href="home.py" style="color:black;" >Logout</a></ul>
    </nav>  <br> <br>""" % ( id, id, id, id, id, id, id, id, id, id, id))
print("""
    <div class="row">
     <nav id="t" class="d-xl-block d-lg-block d-none">
      <br> <br>
     
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
  """ % (id, id, id, id, id, id, id, id, id, id, id))
for i in r:
    print("""<div class="col-lg-9">
    <div class="container mt-5">
        <h2 class="text-center">Hostel Vacation Leave Request Form</h2>
        <form method="post">
            <div class="form-group">
                <label for="studentName">Student Name</label>
                <input type="text" class="form-control" name="st" value="%s"  readonly>
            </div>
                <input type="hidden" class="form-control" name="roll" value="%s"  required>
                <input type="hidden" class="form-control" name="rn"  value="%s" required>
                <input type="hidden" class="form-control"  name="de" value="%s" required>
                <input type="hidden" class="form-control"  name="yr" value="%s" required>
                   <input type="hidden" class="form-control"  name="dep" value="%s" required>
            <div class="form-group">
                <label for="leave">Leaving Date</label>
                <input type="date" class="form-control" name="leave" required>
            </div>
            <div class="form-group">
                <label for="reason">Reason for Vacation</label>
                <textarea class="form-control" name="reason" rows="3" placeholder="Enter reason for leave" required></textarea>
            </div>
            <input type="submit" class="btn btn-primary btn-block" name="sub" value="Submit Request" >
        </form>
    </div>
    
    
    </body>
    </html>
    
    """%(i[2],i[12],rn,i[9],i[10],i[11]))
sub=form.getvalue("sub")
st=form.getvalue("st")
roll=form.getvalue("roll")
rn=form.getvalue("rn")
de=form.getvalue("de")
yr=form.getvalue("yr")
dep=form.getvalue("dep")
leave=form.getvalue("leave")
reason=form.getvalue("reason")
bdate= datetime.now().strftime('%d-%m-%Y')
if leave:
    fleave = datetime.strptime(leave, "%Y-%m-%d").strftime("%d-%m-%Y")
    if sub!=None:
            v="""insert into vacation (Reg_Date,Student_Name,Roll_No,Room_No,Degree,Year,Department,Leaving_Date,Reason,Status) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','Requested')"""%(bdate,st,roll,rn,de,yr,dep,fleave,reason)
            b.execute(v)
            a.commit()
            print("""<script>alert('You have been Successfully Registered Your Vacation Form');</script>""")
>>>>>>> c403f4a19814397122cdcefd156ae16b6abcd48e

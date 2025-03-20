<<<<<<< HEAD
#!C:/Users/Dell/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgitb, pymysql, cgi
from datetime import datetime
cgitb.enable()
a = pymysql.connect(host="localhost", user="root", password="", database="hostel")
b = a.cursor()
reg = cgi.FieldStorage()
id = reg.getvalue("id")
v = """select * from student where id='%s' """ % (id)
b.execute(v)
re = b.fetchall()
st=""
yr=""
for j in re:
    st=j[2]
    yr=j[10]

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
  height: 663px;
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
          table {
  border-collapse: collapse;
  width: 100%;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

th {
  background-color: #0F172A;
  color: #FFFFFF;
  padding: 12px;
  text-align: left;
  font-weight: bold;
}

tr:nth-child(even) {
  background-color: #F9FAFB;
}

tr:nth-child(odd) {
  background-color: #FFFFFF;
}
.custom-modal {
        background: rgba(0, 0, 0, 0.85);
        color: #f1f1f1;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
    }
    .custom-modal-header {
   background: linear-gradient(45deg, #ff5e62, #ffb299);
    border-top-left-radius: 15px;
    border-top-right-radius: 15px;
}
.modal-body {
    background: linear-gradient(45deg, #70e1a1, #1dd8b3); 
    color: #fff;
   
}
.modal-footer {
   background: linear-gradient(45deg, #70e1a1, #1dd8b3);
    color: #fff;
   
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
  <ul  id="w"><span class="fa fa-hand-o-left"></span> <a href="home.py" style="color:black;">Logout</a></ul></nav><br><br>""" % (
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
print(""" <div class="col-lg-9" style="margin-left:20px; margin-top:40px;"> 
    <h1 style="font-family:Times New Roman; text-align:center; color:black; text-shadow: 2px 3px 5px  black; font-weight:500;">Menus</h1>
        <table class="table table-bordered table-hover mt-3">
            <thead style=" font-family:Times New Roman; background-color:#1A237E; color:white; font-size:18px;">
                <tr>
                    <th>Day</th>
                    <th>Breakfast</th>
                    <th>Lunch</th>
                    <th>Snacks</th>
                    <th>Dinner</th>
                    <th>Action</th>
                </tr>
            </thead>
  """)
v = """select * from food_plan where Status='New' or Status='Updated' """
b.execute(v)
r = b.fetchall()
for i in r:
    print("""
                    <tbody>
                        <tr>

                            <td style="color:green; font-weight:600;">%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td><input  class="btn btn-primary" value="Request Menu" data-toggle="modal" data-target="#change%s" ></td>
                """ % (i[1], i[2], i[3], i[4], i[5],i[0]))
    print("""
                       <div class="modal fade" id="change%s">
        <div class="modal-dialog modal-md">
            <div class="modal-content custom-modal"> 
                <div class="modal-header custom-modal-header">
                    <h3 class="modal-title text-center text-white w-100">Details</h3>
                    <button type="button" class="close text-white" data-dismiss="modal">&times;</button>
                </div>
                <div class="modal-body">
                    <div class="row">
                        <div class="col-lg-6 col-6">
                      
                            <p><strong>Day</strong></p>
                            <p style="margin-top:30px;"><strong>Menu Type</strong></p>
                            <p style="margin-top:30px;"><strong>Dish</strong></p>  
                        </div>
                        <div class="col-lg-6 col-6">
                        <form method="post">
                        <input value="%s" name="stu" type="hidden">
                        <input value="%s" name="yr" type="hidden">
                     
                        <p><input  class="form-control" name="day" value="%s" readonly></p>  
                            <p><select class="form-control" id="ty" name="ty" required>
                        <option value="">Select Menu Type</option>
                        <option value="Breakfast">Breakfast</option>
                        <option value="Lunch">Lunch</option>
                        <option value="Snacks">Snacks</option>
                        <option value="Dinner">Dinner</option>
                    </select></p>
                        <p><input  class="form-control" name="dish"></p>  
                        </div>
                    </div>
                </div>
                <div class="modal-footer">
                 <input type="submit" class="btn btn-primary" name="sub" value="Submit">
                    <button class="btn btn-danger" data-dismiss="modal">Close</button>
                </div>
            </div></form>
        </div>
    </div>
    """ % (i[0],st,yr,i[1]))


print("</tbody></table>")
sub=reg.getvalue("sub")
day=reg.getvalue("day")
ty=reg.getvalue("ty")
dish=reg.getvalue("dish")
sn=reg.getvalue("stu")
y=reg.getvalue("yr")
if sub!=None:
    c = datetime.now()
    f = c.strftime("%d-%m-%Y")
    vv="""insert into req_menu(Req_Date,student_name,Year,type,Dish,Status) values ('%s','%s','%s','%s','%s','Requested')"""%(f,sn,y,ty,dish)
    b.execute(vv)
    a.commit()
=======
#!C:/Users/Dell/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgitb, pymysql, cgi
from datetime import datetime
cgitb.enable()
a = pymysql.connect(host="localhost", user="root", password="", database="hostel")
b = a.cursor()
reg = cgi.FieldStorage()
id = reg.getvalue("id")
v = """select * from student where id='%s' """ % (id)
b.execute(v)
re = b.fetchall()
st=""
yr=""
for j in re:
    st=j[2]
    yr=j[10]

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
  height: 663px;
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
          table {
  border-collapse: collapse;
  width: 100%;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

th {
  background-color: #0F172A;
  color: #FFFFFF;
  padding: 12px;
  text-align: left;
  font-weight: bold;
}

tr:nth-child(even) {
  background-color: #F9FAFB;
}

tr:nth-child(odd) {
  background-color: #FFFFFF;
}
.custom-modal {
        background: rgba(0, 0, 0, 0.85);
        color: #f1f1f1;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
    }
    .custom-modal-header {
   background: linear-gradient(45deg, #ff5e62, #ffb299);
    border-top-left-radius: 15px;
    border-top-right-radius: 15px;
}
.modal-body {
    background: linear-gradient(45deg, #70e1a1, #1dd8b3); 
    color: #fff;
   
}
.modal-footer {
   background: linear-gradient(45deg, #70e1a1, #1dd8b3);
    color: #fff;
   
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
  <ul  id="w"><span class="fa fa-hand-o-left"></span> <a href="home.py" style="color:black;">Logout</a></ul></nav><br><br>""" % (
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
print(""" <div class="col-lg-9" style="margin-left:20px; margin-top:40px;"> 
    <h1 style="font-family:Times New Roman; text-align:center; color:black; text-shadow: 2px 3px 5px  black; font-weight:500;">Menus</h1>
        <table class="table table-bordered table-hover mt-3">
            <thead style=" font-family:Times New Roman; background-color:#1A237E; color:white; font-size:18px;">
                <tr>
                    <th>Day</th>
                    <th>Breakfast</th>
                    <th>Lunch</th>
                    <th>Snacks</th>
                    <th>Dinner</th>
                    <th>Action</th>
                </tr>
            </thead>
  """)
v = """select * from food_plan where Status='New' or Status='Updated' """
b.execute(v)
r = b.fetchall()
for i in r:
    print("""
                    <tbody>
                        <tr>

                            <td style="color:green; font-weight:600;">%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td><input  class="btn btn-primary" value="Request Menu" data-toggle="modal" data-target="#change%s" ></td>
                """ % (i[1], i[2], i[3], i[4], i[5],i[0]))
    print("""
                       <div class="modal fade" id="change%s">
        <div class="modal-dialog modal-md">
            <div class="modal-content custom-modal"> 
                <div class="modal-header custom-modal-header">
                    <h3 class="modal-title text-center text-white w-100">Details</h3>
                    <button type="button" class="close text-white" data-dismiss="modal">&times;</button>
                </div>
                <div class="modal-body">
                    <div class="row">
                        <div class="col-lg-6 col-6">
                      
                            <p><strong>Day</strong></p>
                            <p style="margin-top:30px;"><strong>Menu Type</strong></p>
                            <p style="margin-top:30px;"><strong>Dish</strong></p>  
                        </div>
                        <div class="col-lg-6 col-6">
                        <form method="post">
                        <input value="%s" name="stu" type="hidden">
                        <input value="%s" name="yr" type="hidden">
                     
                        <p><input  class="form-control" name="day" value="%s" readonly></p>  
                            <p><select class="form-control" id="ty" name="ty" required>
                        <option value="">Select Menu Type</option>
                        <option value="Breakfast">Breakfast</option>
                        <option value="Lunch">Lunch</option>
                        <option value="Snacks">Snacks</option>
                        <option value="Dinner">Dinner</option>
                    </select></p>
                        <p><input  class="form-control" name="dish"></p>  
                        </div>
                    </div>
                </div>
                <div class="modal-footer">
                 <input type="submit" class="btn btn-primary" name="sub" value="Submit">
                    <button class="btn btn-danger" data-dismiss="modal">Close</button>
                </div>
            </div></form>
        </div>
    </div>
    """ % (i[0],st,yr,i[1]))


print("</tbody></table>")
sub=reg.getvalue("sub")
day=reg.getvalue("day")
ty=reg.getvalue("ty")
dish=reg.getvalue("dish")
sn=reg.getvalue("stu")
y=reg.getvalue("yr")
if sub!=None:
    c = datetime.now()
    f = c.strftime("%d-%m-%Y")
    vv="""insert into req_menu(Req_Date,student_name,Year,type,Dish,Status) values ('%s','%s','%s','%s','%s','Requested')"""%(f,sn,y,ty,dish)
    b.execute(vv)
    a.commit()
>>>>>>> c403f4a19814397122cdcefd156ae16b6abcd48e
    print("""<script>alert('You have Successfully Requested Your Menu');</script>""")
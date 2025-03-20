<<<<<<< HEAD
#!C:/Users/Dell/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgitb, pymysql, cgi

cgitb.enable()
a = pymysql.connect(host="localhost", user="root", password="", database="hostel")
b = a.cursor()
form = cgi.FieldStorage()
reg = cgi.FieldStorage()
id = reg.getvalue("id")
v = """select * from warden where id='%s' """ % (id)
b.execute(v)
re = b.fetchall()
status =""
query = "SELECT * FROM rooms"
b.execute(query)
room = b.fetchall()

print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Warden Dashboard</title>
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
  height: 596px;
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
        section .card-text {
    font-family: 'Lora', serif;
    font-size: 16px;
    color: #333;
    line-height: 1.6;
    font-style: italic;
}
section .card-body {
    background-color: #ffffff;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
.modal-header {
    border-bottom: none;
    border-top-left-radius: 15px;
    border-top-right-radius: 15px;
}

.modal-content {
    border-radius: 15px;
}
.stylish-name {
    background: linear-gradient(45deg, #ff416c, #ff4b2b);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: bold;
    font-size: 1.5rem;
    text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.3);
    transition: transform 0.3s;
}

.stylish-name:hover {
    transform: scale(1.1);
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
     <ul> <a href="wprofile.py?id=%s" style="color:black;">Profile</a></ul>

    
   <ul class="dropdown">Request Orders    <span class="dropdown-toggle"></span>
      <li  class="dropdown-item" id="s"> <a href="wronew.py?id=%s">New</a></li>
       <li  class="dropdown-item" id="s"> <a href="wroex.py?id=%s">Existing</a></li>
   </ul> 
  <ul class="dropdown">Booking <span class="dropdown-toggle"></span>
      <li  class="dropdown-item" id="s"> <a href="wbooknew.py?id=%s">New</a></li>
      <li  class="dropdown-item" id="s"> <a href="wpp.py?id=%s">Payment Processing</a></li>
       <li  class="dropdown-item" id="s"> <a href="wbookex.py?id=%s">Existing</a></li>
   </ul> 
   <ul><a href="wroom.py?id=%s" style="color:black;">Rooms</a></ul>
    <ul class="dropdown" >Menus <span class="dropdown-toggle"></span>
          <li  class="dropdown-item" id="s"> <a href="wmenu.py?id=%s">New</a></li>
           <li  class="dropdown-item" id="s"> <a href="wmenuex.py?id=%s">Existing</a></li>
       </ul>
         <ul><a href="wst.py?id=%s" style="color:black;">Schedule Timing</a></ul>
        <ul class="dropdown" >Feedback <span class="dropdown-toggle"></span>
          <li  class="dropdown-item" id="s"> <a href="wffood.py?id=%s">Food</a></li>
           <li  class="dropdown-item" id="s"> <a href="wfmain.py?id=%s">Maintenance</a></li>
       </ul>
       <ul class="dropdown" >Vacation <span class="dropdown-toggle"></span>
          <li  class="dropdown-item" id="s"> <a href="wvacnew.py?id=%s">New</a></li>
           <li  class="dropdown-item" id="s"> <a href="wvacex.py?id=%s">Existing</a></li>
       </ul>
      <hr>
      <ul id="w" ><span class="fa fa-hand-o-left"></span> <a href="home.py" style="color:black;" >Logout</a></ul>
    </nav>  <br> <br>""" % ( id, id, id, id, id, id, id, id, id, id, id,id,id,id))
print("""
    <div class="row">
     <nav id="t" class="d-xl-block d-lg-block d-none">
      <br> <br>
     <ul> <a href="wprofile.py?id=%s" style="color:white;">Profile</a></ul>
    
   <ul class="dropdown">Request Orders    <span class="dropdown-toggle"></span>
      <li  class="dropdown-item" id="s"> <a href="wronew.py?id=%s">New</a></li>
       <li  class="dropdown-item" id="s"> <a href="wroex.py?id=%s">Existing</a></li>
   </ul> 
  <ul class="dropdown">Booking <span class="dropdown-toggle"></span>
      <li  class="dropdown-item" id="s"> <a href="wbooknew.py?id=%s">New</a></li>
      <li  class="dropdown-item" id="s"> <a href="wpp.py?id=%s">Payment Processing</a></li>
       <li  class="dropdown-item" id="s"> <a href="wbookex.py?id=%s">Existing</a></li>
   </ul> 
  <ul> <a href="wroom.py?id=%s" style="color:white;">Rooms</a></ul>
   <ul class="dropdown" >Menus <span class="dropdown-toggle"></span>
          <li  class="dropdown-item" id="s"> <a href="wmenu.py?id=%s">New</a></li>
           <li  class="dropdown-item" id="s"> <a href="wmenuex.py?id=%s">Existing</a></li>
       </ul>
        <ul><a href="wst.py?id=%s" style="color:white;">Schedule Timing</a></ul>
        <ul class="dropdown" >Feedback <span class="dropdown-toggle"></span>
          <li  class="dropdown-item" id="s"> <a href="wffood.py?id=%s">Food</a></li>
           <li  class="dropdown-item" id="s"> <a href="wfmain.py?id=%s">Maintenance</a></li>
       </ul>
       <ul class="dropdown" >Vacation <span class="dropdown-toggle"></span>
          <li  class="dropdown-item" id="s"> <a href="wvacnew.py?id=%s">New</a></li>
           <li  class="dropdown-item" id="s"> <a href="wvacex.py?id=%s">Existing</a></li>
       </ul>
  <hr>
  <ul  id="w"><span class="fa fa-hand-o-left"></span> <a href="home.py">Logout</a></ul></nav>
  """ % (id, id, id, id, id, id, id, id, id, id, id,id,id,id))
print("""<div class="col-lg-9"><br><br><br>
<div class="container text-center">
    <img src="./media/ro.jpg" height="300px" width="500px" class="mx-auto d-block">
    <h1 class="text-center">Rooms</h1>
    
""" )
print("""<section class="container my-5">
    <div class="row">
""")

for j in room:
    roo=j[2]
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
                        <strong style="font-size:20px;">Status: </strong> <span class="{'text-success' if status == 'Available' else 'text-danger'}" style="font-size:18px; font-weight:600;">{status}</span><br>
                        <strong style="font-size:20px;">Occupancy: </strong> {j[3]} / {j[4]}
                    </p>
   <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#studentModal%s">
        View Students
    </button></div></div></div>
            """%(j[0]))
    print("""
    <!-- Trendy Modal -->
    <div class="modal fade" id="studentModal%s" tabindex="-1" role="dialog" aria-labelledby="studentModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-lg" role="document">
            <div class="modal-content">
                <div class="modal-header bg-info text-white">
                    <h5 class="modal-title" id="studentModalLabel">
                        <i class="fa fa-users"></i> Students in Room
                    </h5>
                    <button type="button" class="close text-white" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <div class="row">
                    <input type="hidden" value="%s" name="room_id">
    """ % (j[0], j[2]))

    student_query = """ SELECT s.Name,s.Profile, b.Degree, b.Year 
             FROM book b
             INNER JOIN student s ON b.Student_Name = s.Name
             INNER JOIN rooms r ON b.room_no = r.ID
             WHERE r.Room_Number = %s AND b.Status = 'Paid' """%(roo)
    b.execute(student_query)
    students = b.fetchall()
    if students:
        for student in students:
            print(f"""
                <div class="col-md-3 col-6">
        <div class="card mb-4 shadow-sm border-0">
            <div class="card-body">
             <img src="./media/{student[1]}" width="50px;" height="50px;" style="border-radius:30%;">
                <h5 class="card-title stylish-name">{student[0]}</h5>
                <p class="card-text">
                    <strong>Degree:</strong> {student[2]}<br>
                    <strong>Year:</strong> {student[3]}
                </p>
            </div>
        </div>
    </div>
            """)
    else:
        print("""
            <div class="col-12">
                <div class="alert alert-warning" role="alert">
                    No students assigned to this room.
                </div>
            </div>
        """)
    print("""
                </div>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
        </div>
    </div>
</div>
""")





print("""
</div>
</body>
</html>
""")
=======
#!C:/Users/Dell/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgitb, pymysql, cgi

cgitb.enable()
a = pymysql.connect(host="localhost", user="root", password="", database="hostel")
b = a.cursor()
form = cgi.FieldStorage()
reg = cgi.FieldStorage()
id = reg.getvalue("id")
v = """select * from warden where id='%s' """ % (id)
b.execute(v)
re = b.fetchall()
status =""
query = "SELECT * FROM rooms"
b.execute(query)
room = b.fetchall()

print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Warden Dashboard</title>
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
  height: 596px;
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
        section .card-text {
    font-family: 'Lora', serif;
    font-size: 16px;
    color: #333;
    line-height: 1.6;
    font-style: italic;
}
section .card-body {
    background-color: #ffffff;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
.modal-header {
    border-bottom: none;
    border-top-left-radius: 15px;
    border-top-right-radius: 15px;
}

.modal-content {
    border-radius: 15px;
}
.stylish-name {
    background: linear-gradient(45deg, #ff416c, #ff4b2b);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: bold;
    font-size: 1.5rem;
    text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.3);
    transition: transform 0.3s;
}

.stylish-name:hover {
    transform: scale(1.1);
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
     <ul> <a href="wprofile.py?id=%s" style="color:black;">Profile</a></ul>

    
   <ul class="dropdown">Request Orders    <span class="dropdown-toggle"></span>
      <li  class="dropdown-item" id="s"> <a href="wronew.py?id=%s">New</a></li>
       <li  class="dropdown-item" id="s"> <a href="wroex.py?id=%s">Existing</a></li>
   </ul> 
  <ul class="dropdown">Booking <span class="dropdown-toggle"></span>
      <li  class="dropdown-item" id="s"> <a href="wbooknew.py?id=%s">New</a></li>
      <li  class="dropdown-item" id="s"> <a href="wpp.py?id=%s">Payment Processing</a></li>
       <li  class="dropdown-item" id="s"> <a href="wbookex.py?id=%s">Existing</a></li>
   </ul> 
   <ul><a href="wroom.py?id=%s" style="color:black;">Rooms</a></ul>
    <ul class="dropdown" >Menus <span class="dropdown-toggle"></span>
          <li  class="dropdown-item" id="s"> <a href="wmenu.py?id=%s">New</a></li>
           <li  class="dropdown-item" id="s"> <a href="wmenuex.py?id=%s">Existing</a></li>
       </ul>
         <ul><a href="wst.py?id=%s" style="color:black;">Schedule Timing</a></ul>
        <ul class="dropdown" >Feedback <span class="dropdown-toggle"></span>
          <li  class="dropdown-item" id="s"> <a href="wffood.py?id=%s">Food</a></li>
           <li  class="dropdown-item" id="s"> <a href="wfmain.py?id=%s">Maintenance</a></li>
       </ul>
       <ul class="dropdown" >Vacation <span class="dropdown-toggle"></span>
          <li  class="dropdown-item" id="s"> <a href="wvacnew.py?id=%s">New</a></li>
           <li  class="dropdown-item" id="s"> <a href="wvacex.py?id=%s">Existing</a></li>
       </ul>
      <hr>
      <ul id="w" ><span class="fa fa-hand-o-left"></span> <a href="home.py" style="color:black;" >Logout</a></ul>
    </nav>  <br> <br>""" % ( id, id, id, id, id, id, id, id, id, id, id,id,id,id))
print("""
    <div class="row">
     <nav id="t" class="d-xl-block d-lg-block d-none">
      <br> <br>
     <ul> <a href="wprofile.py?id=%s" style="color:white;">Profile</a></ul>
    
   <ul class="dropdown">Request Orders    <span class="dropdown-toggle"></span>
      <li  class="dropdown-item" id="s"> <a href="wronew.py?id=%s">New</a></li>
       <li  class="dropdown-item" id="s"> <a href="wroex.py?id=%s">Existing</a></li>
   </ul> 
  <ul class="dropdown">Booking <span class="dropdown-toggle"></span>
      <li  class="dropdown-item" id="s"> <a href="wbooknew.py?id=%s">New</a></li>
      <li  class="dropdown-item" id="s"> <a href="wpp.py?id=%s">Payment Processing</a></li>
       <li  class="dropdown-item" id="s"> <a href="wbookex.py?id=%s">Existing</a></li>
   </ul> 
  <ul> <a href="wroom.py?id=%s" style="color:white;">Rooms</a></ul>
   <ul class="dropdown" >Menus <span class="dropdown-toggle"></span>
          <li  class="dropdown-item" id="s"> <a href="wmenu.py?id=%s">New</a></li>
           <li  class="dropdown-item" id="s"> <a href="wmenuex.py?id=%s">Existing</a></li>
       </ul>
        <ul><a href="wst.py?id=%s" style="color:white;">Schedule Timing</a></ul>
        <ul class="dropdown" >Feedback <span class="dropdown-toggle"></span>
          <li  class="dropdown-item" id="s"> <a href="wffood.py?id=%s">Food</a></li>
           <li  class="dropdown-item" id="s"> <a href="wfmain.py?id=%s">Maintenance</a></li>
       </ul>
       <ul class="dropdown" >Vacation <span class="dropdown-toggle"></span>
          <li  class="dropdown-item" id="s"> <a href="wvacnew.py?id=%s">New</a></li>
           <li  class="dropdown-item" id="s"> <a href="wvacex.py?id=%s">Existing</a></li>
       </ul>
  <hr>
  <ul  id="w"><span class="fa fa-hand-o-left"></span> <a href="home.py">Logout</a></ul></nav>
  """ % (id, id, id, id, id, id, id, id, id, id, id,id,id,id))
print("""<div class="col-lg-9"><br><br><br>
<div class="container text-center">
    <img src="./media/ro.jpg" height="300px" width="500px" class="mx-auto d-block">
    <h1 class="text-center">Rooms</h1>
    
""" )
print("""<section class="container my-5">
    <div class="row">
""")

for j in room:
    roo=j[2]
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
                        <strong style="font-size:20px;">Status: </strong> <span class="{'text-success' if status == 'Available' else 'text-danger'}" style="font-size:18px; font-weight:600;">{status}</span><br>
                        <strong style="font-size:20px;">Occupancy: </strong> {j[3]} / {j[4]}
                    </p>
   <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#studentModal%s">
        View Students
    </button></div></div></div>
            """%(j[0]))
    print("""
    <!-- Trendy Modal -->
    <div class="modal fade" id="studentModal%s" tabindex="-1" role="dialog" aria-labelledby="studentModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-lg" role="document">
            <div class="modal-content">
                <div class="modal-header bg-info text-white">
                    <h5 class="modal-title" id="studentModalLabel">
                        <i class="fa fa-users"></i> Students in Room
                    </h5>
                    <button type="button" class="close text-white" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <div class="row">
                    <input type="hidden" value="%s" name="room_id">
    """ % (j[0], j[2]))

    student_query = """ SELECT s.Name,s.Profile, b.Degree, b.Year 
             FROM book b
             INNER JOIN student s ON b.Student_Name = s.Name
             INNER JOIN rooms r ON b.room_no = r.ID
             WHERE r.Room_Number = %s AND b.Status = 'Paid' """%(roo)
    b.execute(student_query)
    students = b.fetchall()
    if students:
        for student in students:
            print(f"""
                <div class="col-md-3 col-6">
        <div class="card mb-4 shadow-sm border-0">
            <div class="card-body">
             <img src="./media/{student[1]}" width="50px;" height="50px;" style="border-radius:30%;">
                <h5 class="card-title stylish-name">{student[0]}</h5>
                <p class="card-text">
                    <strong>Degree:</strong> {student[2]}<br>
                    <strong>Year:</strong> {student[3]}
                </p>
            </div>
        </div>
    </div>
            """)
    else:
        print("""
            <div class="col-12">
                <div class="alert alert-warning" role="alert">
                    No students assigned to this room.
                </div>
            </div>
        """)
    print("""
                </div>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
        </div>
    </div>
</div>
""")





print("""
</div>
</body>
</html>
""")
>>>>>>> c403f4a19814397122cdcefd156ae16b6abcd48e

#!C:/Users/Dell/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgitb, pymysql, cgi
cgitb.enable()
a = pymysql.connect(host="localhost", user="root", password="", database="hostel")
b = a.cursor()
reg = cgi.FieldStorage()
id = reg.getvalue("id")
v = """select * from warden where id='%s' """ % (id)
b.execute(v)
re = b.fetchall()
print("""
<!DOCTYPE html>
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
    </nav><br><br>""" % (id, id, id, id, id, id, id, id, id, id, id,id,id,id))
print("""
    <div class="row">
     <nav id="t" class="d-xl-block d-lg-block d-none" style="margin-top:20px;">
      <br> 
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
                </tr>
            </thead>
  """)
v="""select * from food_plan where Status='New' or Status='Updated' """
b.execute(v)
r=b.fetchall()
for i in r:
    print("""
                    <tbody>
                        <tr>
                          
                            <td style="color:green; font-weight:600;">%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                """ % (i[1], i[2], i[3], i[4], i[5]))

print("</tbody></table>")

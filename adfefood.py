#!C:/Users/Dell/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgitb, pymysql

cgitb.enable()
a = pymysql.connect(host="localhost", user="root", password="", database="hostel")
b = a.cursor()
s = """select * from feedback where feedback_type='food' """
b.execute(s)
rec = b.fetchall()
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
  height: 580px;
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
   background: linear-gradient(45deg, #ff5e62, #ffb299); /* Example gradient */
    border-top-left-radius: 15px;
    border-top-right-radius: 15px;
}
.modal-body {
    background: linear-gradient(45deg, #70e1a1, #1dd8b3); /* Lighter green to light teal gradient */
    color: #fff;

}
.modal-footer {
   background: linear-gradient(45deg, #70e1a1, #1dd8b3); /* Lighter green to light teal gradient */
    color: #fff;

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
 """)
print("""
 <div class="col-lg-9" style="margin-left:20px; margin-top:40px;"> 
    <h1 style="font-family:Times New Roman; text-align:center; color:black; text-shadow: 2px 3px 5px  black; font-weight:500;">Food Feedback</h1>
        <table class="table table-bordered table-hover mt-3">
            <thead style=" font-family:Times New Roman; background-color:#1A237E; color:white; font-size:18px;">
                <tr>
                    <th>S.No</th>
                    <th>Feedback Date</th>
                    <th>Room Number</th>
                    <th>Student Name</th>
                    <th>Overall Rating</th>
                    <th>Food Quality</th>
                    <th>Issues</th>
                </tr>
            </thead>
  """)
h = 1
for i in rec:
    print("""
                    <tbody>
                        <tr>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                           <td>%s</td>
                           </tr>
                    </tbody>
                """ % (h, i[8], i[2], i[1], i[4],i[6], i[7]))
    h += 1
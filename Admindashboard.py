<<<<<<< HEAD
#!C:/Users/Dell/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgitb, pymysql
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
       >
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
  <div class="col-lg-2"></div>
  <div class="col-lg-4" style="text-align: center;">
  <br>
      <h1 style="color: #333; text-shadow: 2px 2px 4px rgba(0,0,0,0.2); margin-top: 40px;">Welcome Admin!</h1>
  </div>
=======
#!C:/Users/Dell/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgitb, pymysql
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
       >
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
  <div class="col-lg-2"></div>
  <div class="col-lg-4" style="text-align: center;">
  <br>
      <h1 style="color: #333; text-shadow: 2px 2px 4px rgba(0,0,0,0.2); margin-top: 40px;">Welcome Admin!</h1>
  </div>
>>>>>>> c403f4a19814397122cdcefd156ae16b6abcd48e
    </div>""")
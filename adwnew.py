#!C:/Users/Dell/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql,os,smtplib
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
  height: 1370px;
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
  
<div class="container mt-5">
        <h2>Warden Registration</h2>
        <form action="#" method="POST" enctype="multipart/form-data">
            <div class="form-group">
                <label>Full Name</label>
                <input type="text" class="form-control" name="fullname" required>
            </div>
            <div class="form-group">
                <label>Email ID</label>
                <input type="email" class="form-control" name="email" required>
            </div>
            <div class="form-group">
                <label>Date of Birth</label>
                <input type="date" class="form-control" name="dob" required>
            </div>
            <div class="form-group"  required>
                <label>Gender</label>
                <br>
                <input type="radio" id="css" name="gender" value="Female">
                <label for="css" style="color:black;">Female</label>
                <input type="radio" id="javascript" name="gender" style="margin-left:10px;" value="Male">
                <label for="javascript" style="color:black;">Male</label>
            </div>
            <div class="form-group">
                <label>Phone Number</label>
                <input type="text" maxlength="10" pattern="[6-9]{1}[0-9]{9}"
                    title="Phone number must start with 6-9 and be exactly 10 digits" class="form-control" name="phone" required>
            </div>
             <div class="form-group">
             <label>Work Experience</label>
             <select name="exp"  class="form-control" required>
              <option value="0 year">0 Year</option>
              <option value="1 Year">1 Year</option>
              <option value="2 Years">2 Years</option>
              <option value="3 Years">3 Years</option>
              <option value="4 Years">4 Years</option>
              <option value="5 Years">5 Years</option>
              <option value="6 Years">6 Years</option>
              <option value="7 Years">7 Years</option>
            </select>
            </div>
            <div class="form-group">
                <label>City</label>
                <input type="text" class="form-control" name="city" required>
            </div>
            <div class="form-group">
                <label>State</label>
                <input type="text" class="form-control" name="state" required>
            </div>
             <div class="form-group">
                <label>Joining Date</label>
                <input type="date" class="form-control" name="jd" required>
            </div>
            <div class="form-group">
             <label>Assigned Year</label>
             <select name="yr"  class="form-control" required>
             <option value="">Select</option>
              <option value="I year">I Year</option>
              <option value="II Year">II Year</option>
              <option value="III Year">III Year</option>
              <option value="IV Year">IV Year</option>
            </select>
            </div>
           
            <div class="form-group">
                <label>Profile</label>
                <input type="file" class="form-control" name="profile" required>
            </div>
            <div class="form-group">
                <label>Aadhaar Number</label>
                <input type="text" maxlength="12" pattern="[2-9]{1}[0-9]{11}"
                    title="Aadhaar must be 12 digits and cannot start with 0 or 1" class="form-control" name="aadhaar" required>
            </div>
            <div class="form-group">
                <label>Password</label>
                <input type="password"  class="form-control" name="password" required>
            </div>
            <br>
            <div class="row">
                <div class="col-lg-3 col-12"></div>
                <div class="col-lg-4">
                    <button type="submit" class="btn btn-register" name="sub">Register</button>
                </div>
                <div class="col-lg-2 col-12">
                    <a href="home.py" class="btn btn-link">Cancel</a>
                </div>
                <div class="col-lg-2"></div>
            </div>
          <br>
          
        </form>
    </div>
    </div>
 
    """)
form=cgi.FieldStorage()
if len(form) != 0:
    submit=form.getvalue("sub")
    if submit!=None:
        name=form.getvalue("fullname")
        email=form.getvalue("email")
        dob=form.getvalue("dob")
        gen=form.getvalue("gender")
        phone=form.getvalue("phone")
        city=form.getvalue("city")
        state=form.getvalue("state")
        join = form.getvalue("jd")
        join_date = datetime.strptime(join, "%Y-%m-%d")
        jo = join_date.strftime("%d-%m-%Y")
        assyear = form.getvalue("yr")
        exp=form.getvalue("exp")
        profile=form['profile']
        aadhaar=form.getvalue("aadhaar")
        password=form.getvalue("password")

        birth_date = datetime.strptime(dob, '%Y-%m-%d')

        today = datetime.now()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        if age < 25:
            print("""
                                       <script>
                                           alert("You must be above 25 years old to register.");
                                           window.history.back();
                                       </script>
                                       """)
        else:
            ward = """SELECT COUNT(*) FROM warden WHERE Email = %s"""
            b.execute(ward, (email,))
            e = b.fetchone()[0]
            stu = """SELECT COUNT(*) FROM student WHERE Email = %s"""
            b.execute(stu, (email,))
            o = b.fetchone()[0]
            if e > 0 or o > 0:
                print("""
                       <script>
                           alert("This email is already registered. Please use a different email");
                       </script>
                       """)

            else:
                if profile.filename:
                    l = datetime.now()
                    k = l.strftime("%d-%m-%Y")
                    z = os.path.basename(profile.filename)
                    open("media/" + z, "wb").write(profile.file.read())
                    update_query = """INSERT INTO warden(Register_Date,Name,Email,Date_of_Birth,Gender,Phone_Number,City,State,Work_Exp,Profile,Aadhaar,Password,status,Joining_Date,Ass_Year) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','Unblocked','%s','%s')"""%(k,name,email,dob,gen,phone,city,state,exp,z,aadhaar,password,jo,assyear)
                    b.execute(update_query)
                    a.commit()
                    fromadd = 'dharshinitharika213@gmail.com'
                    Password = 'ecnl invr idrc mpdv'
                    toadd = email
                    subject = "Regarding Password given by Admin"
                    body = "Your Password is: {}".format(password)
                    msg = """Subject:{} \n\n {}""".format(subject, body)
                    server = smtplib.SMTP("smtp.gmail.com:587")
                    server.ehlo()
                    server.starttls()
                    server.login(fromadd, Password)
                    server.sendmail(fromadd, toadd, msg)
                    server.quit()
                    print("""
                        <script> alert('Registered Successfully') ;
                        location.href="adwnew.py"
                        </script>""")
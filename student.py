#!C:/Users/Dell/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql, os
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
    <title>Student Registration</title>
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
  height: 1500px;
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
        #contact{
background: linear-gradient(45deg, #007bff, #00d4ff);
}
section h2 {
    font-family: 'Lora', serif;
    font-size: 36px;
    font-weight: 700;
    color: #ff6347; /* Coral color for the headings */
    text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3);
    margin-bottom: 25px;
    letter-spacing: 1px;
}
section p {
    font-family: 'Roboto', sans-serif;
    font-size: 18px;
    color: yellow;
    line-height: 1.8;
    text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
}

</style>
</head>
<body >
 <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
    <a class="navbar-brand" href="#">Dormitory Haven</a>
  
</nav>
<br><br><br>
<div class="container mt-5">
        <h2>Student Registration</h2>
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
                <label for="css" style="color:black">Female</label>
                <input type="radio" id="javascript" name="gender" style="margin-left:10px;" value="Male">
                <label for="javascript" style="color:black;">Male</label>
            </div>
            <div class="form-group">
                <label>Phone Number</label>
                <input type="text" maxlength="10" pattern="[6-9]{1}[0-9]{9}"
                    title="Phone number must start with 6-9 and be exactly 10 digits" class="form-control" name="phone" required>
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
             <label>Current Degree</label>
             <select name="cd"  class="form-control" required>
             <option value="">Select</option>
            <option value="BE">BE</option>
              <option value="BTech">BTech</option>

            </select>
            </div>
             <div class="form-group">
             <label>Current Year</label>
             <select name="cy"  class="form-control" required>
             <option value="">Select</option>
              <option value="I year">I Year</option>
              <option value="II Year">II Year</option>
              <option value="III Year">III Year</option>
              <option value="IV Year">IV Year</option>
            </select>
            </div>
             <div class="form-group">
             <label>Department</label>
             <select name="dep"  class="form-control" required>
             <option value="">Select</option>
              <option value="Mechanical Engineering">Mechanical Engineering</option>
              <option value="Computer Science and Engineering">Computer Science and Engineering</option>
              <option value="Civil Engineering">Civil Engineering</option>
              <option value="Electronics and Communication Engineering">Electronics and Communication Engineering</option>
              <option value="Electronics and Electrical Engineering">Electronics and Electrical Engineering</option>
              <option value="Information Technology">Information Technology</option>
              <option value="Artificial Intelligence and Machine Learning">Artificial Intelligence and Machine Learning</option> 
              <option value="Biomedical Engineering">Biomedical Engineering</option>
            </select>
            </div>
             <div class="form-group">
                <label>Roll Number</label>
                <input type="number" class="form-control" name="roll" required>
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
            </div> <br>
            <div class="row">
                <div class="col-lg-3 col-12"></div>
                <div class="col-lg-4 col-12">
                    <button type="submit" class="btn btn-register" name="sub">Register</button>
                </div>
                <div class="col-lg-2 col-12">
                    <a href="home.py" class="btn btn-link">Cancel</a>
                </div>
                <div class="col-lg-2"></div>
            </div>
        <br>
    <div class="row">
    <div class="col-lg-2"></div>
                <div class="col-lg-8">
                  <p style="color: black; text-align:center;">Already you have an account ? <a href="home.py">Login</a>
                  </p>
                </div>
                <div class="col-lg-2"></div>
              </div>
            </div>
          </form>
        </div>
        
      </div>
<br><br><br>
 <section id="contact" class="text-white py-5">
        <div class="contain text-center">
            <h2 style="color:black;">Contact Us</h2>
            <p style="color:black;">Email: hostel@college.edu | Phone: +91 89760 54321</p>
            <p style="color:black;" >Copyrights <span class="fa fa-copyright"></span> 2025 Dormitory Haven. All Rights Reserved. 
        </div>
    </section>   
    """)
form = cgi.FieldStorage()
if len(form) != 0:
    submit = form.getvalue("sub")
    if submit != None:
        name = form.getvalue("fullname")
        email = form.getvalue("email")
        dob = form.getvalue("dob")
        gen = form.getvalue("gender")
        phone = form.getvalue("phone")
        city = form.getvalue("city")
        state = form.getvalue("state")
        cd = form.getvalue("cd")
        cy = form.getvalue("cy")
        dep = form.getvalue("dep")
        roll = form.getvalue("roll")
        profile = form['profile']
        aadhaar = form.getvalue("aadhaar")
        password = form.getvalue("password")
        birth_date = datetime.strptime(dob, '%Y-%m-%d')
        today = datetime.now()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        if age < 18:
            print("""
                                       <script>
                                           alert("You must be atleast 18 years old to register.");
                                           window.history.back();
                                       </script>
                                       """)
        else:
            stu = """SELECT COUNT(*) FROM student WHERE Email = %s"""
            b.execute(stu, (email,))
            o = b.fetchone()[0]
            ward = """SELECT COUNT(*) FROM warden WHERE Email = %s"""
            b.execute(ward, (email,))
            e = b.fetchone()[0]
            if o > 0 or e > 0:
                print("""
                       <script>
                           alert("This email is already registered. Please use a different email.");
                       </script>
                       """)

            else:
                if profile.filename:
                    l = datetime.now()
                    k = l.strftime("%d-%m-%Y")
                    z = os.path.basename(profile.filename)
                    open("media/" + z, "wb").write(profile.file.read())
                    update_query = """INSERT INTO student(Register_Date,Name,Email,Date_of_Birth,Gender,Phone_Number,City,State,Current_Degree,Year,Department,Roll_Number,Profile,Aadhaar,Password,status) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','Unblocked')""" % (
                    k, name, email, dob, gen, phone, city, state,cd,cy,dep,roll, z, aadhaar,password)
                    b.execute(update_query)
                    a.commit()
                    print("""
                        <script> alert('Registered Successfully') ;
                        location.href="ward.py?Year=%s&Name=%s"
                        </script>"""%(cy,name))
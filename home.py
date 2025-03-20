#!C:/Users/Dell/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql
cgitb.enable()
a = pymysql.connect(host="localhost", user="root", password="", database="hostel")
b = a.cursor()
reg=cgi.FieldStorage()
status =""
query = "SELECT * FROM rooms"
b.execute(query)
room = b.fetchall()
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>College Hostel Management</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
   <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.2/dist/js/bootstrap.bundle.min.js"></script> <script src="https://kit.fontawesome.com/a076d05399.js" crossorigin="anonymous"></script>
     <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">

    <style>
body {
    margin: 0;
    font-family: 'Roboto', sans-serif;
    background-color: #f4f4f4;
}
.hero {
    background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url('./media/hw.jpg') no-repeat center center/cover;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
    text-align: center;
}
.hero div {
    max-width: 700px;
    padding: 40px;
    background-color: rgba(0, 0, 0, 0.5);
    border-radius: 15px;
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
section .card-title {
    font-family: 'Poppins', sans-serif;
    font-size: 22px;
    font-weight: 600;
    color: #007bff; /* Blue color for card titles */
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 10px;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
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
h1 {
    font-size: 56px;
    font-weight: 700;
    text-shadow: 3px 3px 20px rgba(0, 0, 0, 0.7);
    margin-bottom: 20px;
    font-family: 'Roboto', sans-serif;
}
.btn-light {
    background-color: #ff6347;
    color: white;
    font-weight: 600;
    padding: 12px 35px;
    border-radius: 50px;
    text-transform: uppercase;
    transition: background-color 0.3s ease, transform 0.3s ease;
}
.btn-light:hover {
    background-color: #ff4500;
    transform: scale(1.1);
}
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
.navbar-nav .nav-item .nav-link {
    color: #ffffff !important;
    font-weight: 600;
    padding: 10px 15px;
    transition: color 0.3s ease;
}
.navbar-nav .nav-item .nav-link:hover {
    color: #ffcc00 !important;
}
.nav-item .nav-link.btn {
    background-color: rgba(255, 255, 255, 0.2);
    border: 2px solid white;
    padding: 10px 25px;
    border-radius: 25px;
    transition: all 0.3s ease;
}
.nav-item .nav-link:hover {
    transform: scale(1.1);
}
.nav-item .dropdown-menu {
    border-radius: 10px;
}
@media (max-width: 768px) {
    h1 {
        font-size: 40px;
    }
    section h2 {
        font-size: 28px;
    }
    section p {
        font-size: 16px;
    }
}
#contact{
background: linear-gradient(45deg, #007bff, #00d4ff);
}

   

    </style>
</head>
<body>
 <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
    <a class="navbar-brand" href="#">Dormitory Haven</a>
    <button class="navbar-toggler" type="button"  data-toggle="collapse" data-target="#navbarNav">
        <span class="navbar-toggler-icon" ></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ml-auto" >
            <li class="nav-item mx-3"><a class="nav-link" href="ro.py">Rooms</a></li>
           
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle btn text-white ml-2" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" style="margin-right:50px; border:2px solid black;">
                    <i class="fa fa-user-plus mr-2"></i> Register
                </a>
                <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                    <a class="dropdown-item" href="student.py">Student</a>
                </div>
            </li>
           <br>
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle btn text-white ml-2" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" style="margin-right:50px; border:2px solid black;">
                    <i class="fa fa-hand-o-right mr-2"></i> Login
                </a>
                <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                    <a class="dropdown-item" href="#" data-toggle="modal" data-target="#adminlogin" >Admin</a>
                    <a class="dropdown-item" href="#" data-toggle="modal" data-target="#wardenlogin">Warden</a>
                    <a class="dropdown-item" href="#" data-toggle="modal" data-target="#studentlogin">Student</a>
                </div>
            </li>
            
        </ul>
       
    </div>
</nav>
<div class="modal fade" id="adminlogin" tabindex="-1" role="dialog" aria-labelledby="loginModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content" style="border-radius: 15px; box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);">
            <div class="modal-header" style="background-color: #333; color: white; border-bottom: none; border-top-left-radius: 15px; border-top-right-radius: 15px; display: flex; justify-content: center; align-items: center;">
                <h5 class="modal-title" id="loginModalLabel" style="font-family: 'Poppins', sans-serif; font-weight: 600; text-align: center;">Admin Login</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close" style="color: white;">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body" style="background-color: #f9f9f9; padding: 30px; border-radius: 10px;">
                <form  method="post" data-toggle="modal">
                    <div class="form-group">
                        <label for="name" style="font-size: 16px; font-weight: 600;">Name</label>
                        <input type="text" class="form-control" name="admin" id="name" placeholder="Enter your name" required style="border-radius: 10px; box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.1);">
                    </div>
                    <div class="form-group">
                        <label for="password" style="font-size: 16px; font-weight: 600;">Password</label>
                        <input type="password" class="form-control" name="pas" id="password" placeholder="Enter your password" required style="border-radius: 10px; box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.1);">
                    </div>
                
            </div>
            <div class="modal-footer" style="border-top: none; padding: 20px;">
                <div class="form-group text-center">
                    <input type="submit" class="btn btn-primary btn-block" name="sub" style="background: linear-gradient(45deg, #ff6347, #ff4500); border-radius: 30px; padding: 12px 20px; font-weight: 600; transition: all 0.3s ease-in-out; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);" value="Login">
                </div></form>
                <div class="form-group text-center">
                    <button type="button" class="btn btn-secondary btn-block" data-dismiss="modal" style="border-radius: 30px; padding: 12px 20px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); transition: all 0.3s ease-in-out;">Close</button>
                </div>
            </div>
        </div>
    </div>  
</div>

<div class="modal fade" id="wardenlogin" tabindex="-1" role="dialog" aria-labelledby="loginModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content" style="border-radius: 15px; box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);">
            <div class="modal-header" style="background-color: #333; color: white; border-bottom: none; border-top-left-radius: 15px; border-top-right-radius: 15px; display: flex; justify-content: center; align-items: center;">
                <h5 class="modal-title" id="loginModalLabel" style="font-family: 'Poppins', sans-serif; font-weight: 600; text-align: center;">Warden Login</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close" style="color: white;">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body" style="background-color: #f9f9f9; padding: 30px; border-radius: 10px;">
                <form action="" method="post" data-toggle="modal">
                    <div class="form-group">
                        <label for="name" style="font-size: 16px; font-weight: 600;">Name</label>
                        <input type="text" class="form-control" id="name" name="wa" placeholder="Enter your name" required style="border-radius: 10px; box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.1);">
                    </div>
                    <div class="form-group">
                        <label for="password" style="font-size: 16px; font-weight: 600;">Password</label>
                        <input type="password" class="form-control" id="password" name="pa" placeholder="Enter your password" required style="border-radius: 10px; box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.1);">
                    </div><a href="fpwarden.py">Forgot Password?</a>
                    
              
            </div>
            <div class="modal-footer" style="border-top: none; padding: 20px;">
                <div class="form-group text-center">
                    <input type="submit" class="btn btn-primary" name="su" style="background: linear-gradient(45deg, #ff6347, #ff4500); border-radius: 30px; padding: 12px 20px; font-weight: 600; transition: all 0.3s ease-in-out; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);" value="Login">
                </div>
                <div class="form-group text-center">
                    <button type="button" class="btn btn-danger" data-dismiss="modal" style="border-radius: 30px; padding: 12px 20px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); transition: all 0.3s ease-in-out;">Close</button>
                </div>
            </div> </form> 
        </div>
    </div>   
</div>
<div class="modal fade" id="studentlogin" tabindex="-1" role="dialog" aria-labelledby="loginModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content" style="border-radius: 15px; box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);">
            <div class="modal-header" style="background-color: #333; color: white; border-bottom: none; border-top-left-radius: 15px; border-top-right-radius: 15px; display: flex; justify-content: center; align-items: center;">
                <h5 class="modal-title" id="loginModalLabel" style="font-family: 'Poppins', sans-serif; font-weight: 600; text-align: center;">Student Login</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close" style="color: white;">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body" style="background-color: #f9f9f9; padding: 30px; border-radius: 10px;">
                <form action="" method="post" data-toggle="modal">
                    <div class="form-group">
                        <label for="name" style="font-size: 16px; font-weight: 600;">Name</label>
                        <input type="text" class="form-control" id="name" name="stu" placeholder="Enter your name" required style="border-radius: 10px; box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.1);">
                    </div>
                    <div class="form-group">
                        <label for="password" style="font-size: 16px; font-weight: 600;">Password</label>
                        <input type="password" class="form-control" id="password" name="p" placeholder="Enter your password" required style="border-radius: 10px; box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.1);">
                    </div><a href="fpstudent.py">Forgot Password?</a>
                
            </div>
            <div class="modal-footer" style="border-top: none; padding: 20px;">
                <div class="form-group text-center">
                <input type="submit" class="btn btn-primary" name="submit" style="background: linear-gradient(45deg, #ff6347, #ff4500); border-radius: 30px; padding: 12px 20px; font-weight: 600; transition: all 0.3s ease-in-out; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);" value="Login">
                </div>
                <div class="form-group text-center">
                    <button type="button" class="btn btn-secondary btn-block" data-dismiss="modal"  style="border-radius: 30px; padding: 12px 20px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); transition: all 0.3s ease-in-out;">Close</button>
                </div>
            </div></form>
        </div>
    </div>  
</div>""")
print("""  <section class="hero">
        <div>
            <h1>Welcome to Our  Hostel</h1>
            <p>Safe, Comfortable, and Affordable Accommodation</p>
            <a href="#rooms" class="btn btn-light">Explore Rooms</a>
        </div>
    </section>
    
   <section id="rooms" class="container my-5">
    <h2 class="text-center">Rooms</h2><br>
    <div class="row">
        <!-- Rooms Section -->
        <div class="container text-center">
    <img src="./media/ro.jpg" height="300px" width="500px" class="mx-auto d-block">
   <br><br></div></div></section>
     
""")
print("""<section class="container my-5">
    <div class="row">
""")

for j in room:
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
    """)

    if status == "Available":
        print(f"""
                    <form method="post">
                        <input type="submit" class="btn btn-primary w-100" name="book" value="Book Now">
                    </form>
        """)

    print("""
                </div>
            </div>
        </div>
    """)

print("""</div>""")


print(""" 
    <h2 class="text-center my-5" id="fac">Additional Facilities</h2>
    <div class="row">
        <!-- Maintenance Section -->
        <div class="col-lg-4 col-12 mb-4">
            <div class="card">
                <img src="./media/main.jpg" class="card-img-top" alt="Maintenance">
                <div class="card-body">
                    <h5 class="card-title">Maintenance</h5>
                    <p class="card-text">24/7 maintenance services to ensure everything is in perfect condition.</p>
                </div>
            </div>
        </div>
        
        <!-- Mess Section -->
        <div class="col-lg-4 col-12 mb-4">
            <div class="card">
                <img src="./media/mess.jpg" class="card-img-top" alt="Mess">
                <div class="card-body">
                    <h5 class="card-title">Mess</h5>
                    <p class="card-text">Nutritious and affordable meals served daily in our hostel mess.</p>
                </div>
            </div>
        </div>
        
        <div class="col-lg-4 col-12 mb-4">
            <div class="card">
                <img src="./media/st.jpg" class="card-img-top" alt="Room">
                <div class="card-body">
  <h5 class="card-title">Stationery</h5>
  <p class="card-text">Explore our well-designed, professional stationery for hostel communications.</p>
</div>

            </div>
        </div>
    </div>
</section>

    <section id="contact" class="text-white py-5">
        <div class="container text-center">
            <h2 style="color:black;">Contact Us</h2>
            <p style="color:black;">Email: hostel@college.edu | Phone: +91 89760 54321</p>
            <p style="color:black;" >Copyrights <span class="fa fa-copyright"></span> 2025 Dormitory Haven. All Rights Reserved. 
        </div>
    </section>   
</body>
</html>
""")

submit=reg.getvalue("sub")
Name=reg.getvalue("admin")
Password=reg.getvalue("pas")
if submit!=None:
    p = """select id from admin where Name='%s' and Password='%s'""" % (Name, Password)
    b.execute(p)
    resu = b.fetchone()
    if resu != None:
        print("""
        <script>
         alert("Logined Successfully");
          location.href="Admindashboard.py"
        </script> """ )
    else:
        print("""
                <script>
                 alert("Admin Not Found");
                 location.href="home.py"
                </script> """)

book=reg.getvalue("book")
if book!=None:
    print("""<script> alert('Please Register/Login and Book Your Room')</script>""")

sub=reg.getvalue("su")
wa=reg.getvalue("wa")
Passw=reg.getvalue("pa")
if sub!=None:
    l = """select id from warden where Name='%s' and Password='%s' and status='Unblocked' """ % (wa,Passw)
    b.execute(l)
    re = b.fetchone()
    if re != None:
        print("""
        <script>
         alert("Logined Successfully");
          location.href="wardendashboard.py?id=%s"
        </script> """ %(re[0]))
    else:
        print("""
                <script>
                 alert("Warden Not Found");
                 location.href="home.py"
                </script> """)
sun=reg.getvalue("submit")
stu=reg.getvalue("stu")
Pa=reg.getvalue("p")
if sun!=None:
    t = """select id from student where Name='%s' and Password='%s' and status='Unblocked' """ % (stu, Pa)
    b.execute(t)
    r = b.fetchone()
    if r != None:
        print("""
        <script>
         alert("Logined Successfully");
          location.href="studentdashboard.py?id=%s"
        </script> """ %(r[0]))
    else:
        print("""
                <script>
                 alert("Student Not Found");
                 location.href="home.py"
                </script> """)
#!C:/Users/Dell/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql

cgitb.enable()
a = pymysql.connect(host="localhost", user="root", password="", database="hostel")
b = a.cursor()
reg = cgi.FieldStorage()
status = ""
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
.search-box {
            width: 100%;
            max-width: 500px;
            margin: 0 auto;
        }


    </style>
</head>
<body>
 <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
    <a class="navbar-brand" href="#">Dormitory Haven</a>
    </nav><br><br>""")

print(""" <section id="rooms" class="container my-5">
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

print("""</div></section>""")
print("""    <section id="contact" class="text-white py-5">
        <div class="container text-center">
            <h2 style="color:black;">Contact Us</h2>
            <p style="color:black;">Email: hostel@college.edu | Phone: +91 89760 54321</p>
            <p style="color:black;" >Copyrights <span class="fa fa-copyright"></span> 2025 Dormitory Haven. All Rights Reserved. 
        </div>
    </section>   
</body>
</html>
""")
book=reg.getvalue("book")
if book!=None:
    print("""<script> alert('Please Register/Login and Book Your Room');
    location.href="home.py"</script>""")

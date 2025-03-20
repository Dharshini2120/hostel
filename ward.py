#!C:/Users/Dell/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql

cgitb.enable()
a = pymysql.connect(host="localhost", user="root", password="", database="hostel")
b = a.cursor()
reg = cgi.FieldStorage()
year=reg.getvalue("Year")
name=reg.getvalue("Name")
v = """SELECT w.* FROM warden w JOIN student s ON w.Ass_Year = s.Year WHERE s.Year = '%s' and s.Name='%s' and w.status='Unblocked' """%(year,name)
b.execute(v)
rec = b.fetchall()
na = ""
for i in rec:
    na = i[2]
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
<br><br><br>""")
for i in rec:

    print(f""" 
    <div class="row">
    <div class="col-lg-4"></div>
      <div class="col-lg-5" style="margin-left:60px;">
    <div class="card" style="background: linear-gradient(135deg, #FF416C 0%, #FF4B2B 100%); color: white; padding: 20px; 
    margin-top:90px; height:330px; width:350px; border-radius: 15px; box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);">
    <img src="./media/{i[10]}" height="130px" width="130px" style="margin-left:78px; margin-top:10px; border-radius:40%; box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);" > 
    <h4 style="font-family: 'Arial', sans-serif; margin-top:5%; text-align: center; font-weight:900; background-size: 400%; color:white;"> {i[2]}
    </h4>
    <h6 style="font-family: 'Arial', sans-serif; margin-top:3%;  text-align: center; font-weight:900; background-size: 400%; color:white;">{i[15]} - Warden</h6>
   <a class="btn btn-primary"  href="home.py" style="margin-top:5%; font-weight:600;">Ok</a>
    </div>  
</div>
   <div class="col-lg-3"></div></div>

""")

print("""
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

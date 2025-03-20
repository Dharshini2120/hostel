#!C:/Users/Dell/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgitb, pymysql, cgi
from datetime import datetime
cgitb.enable()
a = pymysql.connect(host="localhost", user="root", password="", database="hostel")
b = a.cursor()
reg = cgi.FieldStorage()
id = reg.getvalue("id")
v = """SELECT Name FROM student WHERE id='%s'""" % (id)
b.execute(v)
re = b.fetchone()
name = re[0]
ss = """ SELECT b.room_no FROM student s JOIN book b ON s.Name = b.Student_Name WHERE s.Name = '%s' """ % (name)
b.execute(ss)
r = b.fetchone()
roomno = r[0]
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
  height: 563px;
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
print("""
    <div class="container mt-5">
        <h2 class="text-center">Feedback Form</h2>
        <form id="feedbackForm" method="post">
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" class="form-control" id="name" value="%s" readonly>
            </div>
            <div class="form-group">
                <label for="roomNumber">Room Number:</label>
                <input type="text" class="form-control" id="roomNumber" value="%s" readonly>
            </div>
            <div class="form-group">
                <label for="feedbackType">Type:</label>
                <select class="form-control" id="feedbackType" name="feedbackType" required>
                    <option value="">Select Type</option>
                    <option value="maintenance">Maintenance</option>
                    <option value="food">Food</option>
                </select>
            </div>
            <div id="maintenanceFeedback" style="display: none;">
                <h4>Maintenance Feedback</h4>
                <div class="form-group">
                    <label for="maintenanceRating">Overall Rating:</label>
                    <select class="form-control" id="maintenanceRating" name="maintenanceRating">
                        <option value="">Select Rating</option>
                        <option>Excellent</option>
                        <option>Good</option>
                        <option>Average</option>
                        <option>Poor</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="cleanliness">Cleanliness:</label>
                    <select class="form-control" id="cleanliness" name="cleanliness">
                        <option value="">Select Rating</option>
                        <option>Excellent</option>
                        <option>Good</option>
                        <option>Average</option>
                        <option>Poor</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="maintenanceIssues">Issues (if any):</label>
                    <textarea class="form-control" id="maintenanceIssues" name="maintenanceIssues" rows="3"></textarea>
                </div>
            </div>
            <div id="foodFeedback" style="display: none;">
                <h4>Food Feedback</h4>
                <div class="form-group">
                    <label for="foodRating">Overall Rating:</label>
                    <select class="form-control" id="foodRating" name="foodRating">
                        <option value="">Select Rating</option>
                        <option>Excellent</option>
                        <option>Good</option>
                        <option>Average</option>
                        <option>Poor</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="foodQuality">Food Quality:</label>
                    <select class="form-control" id="foodQuality" name="foodQuality">
                        <option value="">Select Rating</option>
                        <option>Excellent</option>
                        <option>Good</option>
                        <option>Average</option>
                        <option>Poor</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="foodIssues">Issues (if any):</label>
                    <textarea class="form-control" id="foodIssues" name="foodIssues" rows="3"></textarea>
                </div>
            </div>
            <button type="submit" class="btn btn-primary">Submit Feedback</button>
        </form>
    </div>
    <script>
        document.getElementById('feedbackType').addEventListener('change', function() {
            const type = this.value;
            document.getElementById('maintenanceFeedback').style.display = type === 'maintenance' ? 'block' : 'none';
            document.getElementById('foodFeedback').style.display = type === 'food' ? 'block' : 'none';
        });
    </script>
""" % (name, roomno))
if reg.getvalue("feedbackType"):
    feedback_type = reg.getvalue("feedbackType")
    overall_rating = reg.getvalue("maintenanceRating") if feedback_type == 'maintenance' else reg.getvalue("foodRating")
    cleanliness = reg.getvalue("cleanliness") if feedback_type == 'maintenance' else None
    food_quality = reg.getvalue("foodQuality") if feedback_type == 'food' else None
    issues = reg.getvalue("maintenanceIssues") if feedback_type == 'maintenance' else reg.getvalue("foodIssues")
    current_date = datetime.now().strftime('%d-%m-%Y')
    insert_query = """
        INSERT INTO feedback (student_name, room_no, feedback_type, overall_rating, cleanliness, food_quality, issues,date)
        VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s','%s')
    """%(name, roomno, feedback_type, overall_rating, cleanliness, food_quality, issues,current_date)
    b.execute(insert_query)
    a.commit()
    print("<script>alert('Feedback submitted successfully!');</script>")
b.close()
a.close()


#!C:/Users/Dell/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgitb, pymysql, cgi, math
cgitb.enable()
a = pymysql.connect(host="localhost", user="root", password="", database="hostel")
b = a.cursor()
form = cgi.FieldStorage()
page = int(form.getvalue("page") or 1)
records_per_page = 5
offset = (page - 1) * records_per_page
v = "SELECT COUNT(*) FROM student WHERE status='Unblocked' OR status='Blocked'"
b.execute(v)
total_records = b.fetchone()[0]
total_pages = math.ceil(total_records / records_per_page)
query = """SELECT * FROM student WHERE status='Unblocked' OR status='Blocked' LIMIT %s OFFSET %s"""
b.execute(query, (records_per_page, offset))
re = b.fetchall()
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
   <div class="col-lg-9" style="margin-left:20px; margin-top:40px;"> 
    <h1 style="font-family:Times New Roman; text-align:center; color:black; text-shadow: 2px 3px 5px  black; font-weight:500;">Student Details</h1>
        <table class="table table-bordered table-hover mt-3">
            <thead style=" font-family:Times New Roman; background-color:#1A237E; color:white; font-size:18px;">
                <tr>
                    <th>S.No</th>
                    <th>Registered Date</th>
                    <th>Name</th>
                    <th>Degree</th>
                    <th>Year</th>
                    <th>Department</th>
                    <th>More</th>
                    <th>Action</th>
                </tr>
            </thead>
  """)
h = offset + 1
for i in re:
    l = i[16]
    if l == 'Blocked':
        print("""
                    <tbody>
                        <tr>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>
                                <button class="btn" style="border:3px solid; border-radius:10px; width:85px;" data-toggle="modal" data-target="#view%s"><span class="bi bi-eye-fill"></span> View </button></td>

                             <td>    <form method="post">
                            <input type="hidden" name="del" value='%s'>
                            <span class="fa fa-check-circle" style="color:green; font-weight:700;"></span>
                                <input style="border:none; background-color:white; color:green; font-weight:700;" type="submit" name="delete" value="Unblock"></form>
                             </td>
                        </tr>
                    </tbody>
                """ % (h, i[1], i[2],i[9], i[10], i[11], i[0], i[0]))

        print("""
                   <div class="modal fade" id="view%s">
    <div class="modal-dialog modal-md">
        <div class="modal-content custom-modal"> 
            <div class="modal-header custom-modal-header">
                <h3 class="modal-title text-center text-white w-100">Details</h3>
                <button type="button" class="close text-white" data-dismiss="modal">&times;</button>
            </div>
            <div class="modal-body">
                <div class="row">
                    <div class="col-lg-6 col-6">
                       <p><strong>Name</strong></p>
                        <p><strong>Email</strong></p>
                        <p><strong>Phone</strong></p>
                        <p><strong>City</strong></p>
                        <p><strong>State</strong></p>
                        <p><strong>Degree</strong></p>
                        <p><strong>Year</strong></p>
                        <p><strong>Department</strong></p><br>
                        <p><strong>Roll Number</strong></p>
                        <p ><strong>Aadhaar Number</strong></p>
                        <p><strong>Password</strong></p>
                    </div>
                    <div class="col-lg-6 col-6">
                     <p><img class="rounded-circle shadow" width="60px" height="60px" src="./media/%s"></p>
                        <p>%s</p>
                        <p>%s</p>
                        <p>%s</p>
                        <p>%s</p>
                        <p>%s</p>
                        <p>%s</p>
                        <p>%s</p>
                        <p>%s</p>
                        <p>%s</p>
                        <p>%s</p>
                        <form>
                            <input type="text" name="pa" value='%s' class="form-control mb-2">
                            <button class="btn btn-primary" type="submit" name="up" value="%s">Update</button>
                        </form>
                    </div>
                </div>
            </div>
            <div class="modal-footer">
                <button class="btn btn-danger" data-dismiss="modal">Close</button>
            </div>
        </div>
    </div>
</div>
                """ % (i[0],i[13], i[2], i[3], i[6], i[7], i[8], i[9], i[10], i[11], i[12],i[14],i[15], i[0]))
        h += 1
    if l == 'Unblocked':
        print("""
                    <tbody>
                        <tr>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                             <td>%s</td>
                            <td>%s</td>
                            <td>
                                <button class="btn" style="border:3px solid; border-radius:10px; width:85px;" data-toggle="modal" data-target="#view%s"><span class="bi bi-eye-fill"></span> View </button></td>

                            <td> <form method="post">
                                                 <input type="hidden" name="d" value='%s'>
                                               <span class="fa fa-times-circle" style="color:red; font-weight:700;"></span>
                                               <input style="border:none; background-color:white; color:red; font-weight:700;" type="submit" name="de" value="Block"></form>
                                            </td>
                        </tr>
                    </tbody>
                """ % (h, i[1], i[2], i[9],i[10],i[11], i[0], i[0]))

        print("""
                    <div class="modal fade" id="view%s">
    <div class="modal-dialog modal-md">
        <div class="modal-content custom-modal">
            <div class="modal-header custom-modal-header">
                <h3 class="modal-title text-center text-white w-100">Details</h3>
                <button type="button" class="close text-white" data-dismiss="modal">&times;</button>
            </div>
            <div class="modal-body">
            <p><img class="rounded-circle shadow" style="margin-left:180px;" width="70px" height="70px" src="./media/%s"></p>
                <div class="row">
                
                    <div class="col-lg-6 col-6" style="padding-left:30px;">
                        <p><strong>Name</strong></p>
                        <p><strong>Email</strong></p>
                        <p><strong>Phone</strong></p>
                        <p><strong>City</strong></p>
                        <p><strong>State</strong></p>
                        <p><strong>Degree</strong></p>
                        <p><strong>Year</strong></p>
                        <p><strong>Department</strong></p><br>
                        <p><strong>Roll Number</strong></p>
                        <p><strong>Aadhaar Number</strong></p>
                        <p><strong>Password</strong></p>
                    </div>
                    <div class="col-lg-6 col-6">
                     
                        <p>%s</p>
                        <p>%s</p>
                        <p>%s</p>
                        <p>%s</p>
                        <p>%s</p>
                        <p>%s</p>
                         <p>%s</p>
                        <p>%s</p>
                        <p>%s</p>
                        <p>%s</p>
                        <form>
                            <input type="text" name="pa" value='%s' class="form-control mb-2">
                            <button class="btn btn-primary" type="submit" name="up" value="%s">Update</button>
                        </form>
                    </div>
                </div>
            </div>
            <div class="modal-footer">
                <button class="btn btn-danger" data-dismiss="modal">Close</button>
            </div>
        </div>
    </div>
</div>
                """ % (i[0],i[13], i[2], i[3], i[6], i[7], i[8], i[9], i[10], i[11], i[12],i[14],i[15], i[0]))
        h += 1

pa = form.getvalue("pa")
p = form.getvalue("p")
us = form.getvalue("n")
Delete = form.getvalue("delete")
De = form.getvalue("de")
sub = form.getvalue("up")
if sub != None:
    x = """ update warden set Password='%s'  WHERE id='%s' """ % (pa, sub)
    b.execute(x)
    a.commit()
    print("""
            <script> alert('Password Updated Successfully')
            location.href="adwex.py"
            </script>""")
if Delete != None:
    Del = form.getvalue("del")
    c = """Update warden set status='Unblocked' WHERE id='%s'""" % (Del)
    b.execute(c)
    a.commit()
    print("""
                 <script>
                   alert("Warden Unblocked Successfully");
                   location.href="adwex.py";
                 </script> """)
if De != None:
    D = form.getvalue("d")
    g = """Update warden set status='Blocked' WHERE id='%s'""" % (D)
    b.execute(g)
    a.commit()
    print("""
                 <script>
                   alert("Student Blocked Successfully");
                   location.href="adwex.py";
                 </script> """)

print("</tbody></table>")

if total_records > 5:
    print('<nav><ul class="pagination justify-content-center">')

    # Previous Button
    if page > 1:
        print(f'<li class="page-item"><a class="page-link" href="?page={page - 1}">Previous</a></li>')

    # Numbered Pages
    for i in range(1, total_pages + 1):
        active_class = "active" if i == page else ""
        print(f'<li class="page-item {active_class}"><a class="page-link" href="?page={i}">{i}</a></li>')

    # Next Button
    if page < total_pages:
        print(f'<li class="page-item"><a class="page-link" href="?page={page + 1}">Next</a></li>')

    print("</ul></nav>")


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
v = "SELECT COUNT(*) FROM rooms where Status='Updated' or Status='New'"
b.execute(v)
total_records = b.fetchone()[0]
total_pages = math.ceil(total_records / records_per_page)
query = """SELECT * FROM rooms where Status='Updated' or Status='New' LIMIT %s OFFSET %s"""
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
.custom-modal .modal-body {
    background: linear-gradient(45deg, #70e1a1, #1dd8b3); /* Lighter green to light teal gradient */
    color: #fff;

}
.custom-modal .modal-footer {
   background: linear-gradient(45deg, #70e1a1, #1dd8b3); /* Lighter green to light teal gradient */
    color: #fff;

}  

.stylish-name {
    background: linear-gradient(45deg, #ff416c, #ff4b2b);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: bold;
    font-size: 1.5rem;
    text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.3);
    transition: transform 0.3s;
}

.stylish-name:hover {
    transform: scale(1.1);
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
      <ul> <a href="vacation.py" style="text-decoration:none; color:white;">Vacation</a> </ul><hr>
  <ul  id="w"><span class="fa fa-hand-o-left"></span> <a href="home.py">Logout</a></ul></nav>
   <div class="col-lg-9" style="margin-left:20px; margin-top:40px;"> 
    <h1 style="font-family:Times New Roman; text-align:center; color:black; text-shadow: 2px 3px 5px  black; font-weight:500;">Room Details</h1>
        <table class="table table-bordered table-hover mt-3">
            <thead style=" font-family:Times New Roman; background-color:#1A237E; color:white; font-size:18px;">
                <tr>
                    <th>S.No</th>
                    <th>Registered Date</th>
                    <th>Room Number</th>
                    <th>Occupancy</th>
                    <th>Total Capacity</th>
                    <th>Details</th>
                    <th>Action</th>
                </tr>
            </thead>
  """)
h = offset + 1
for i in re:
     print("""
                    <tbody>
                        <tr>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
         <td><button class="btn btn-info" data-toggle="modal" data-target="#studentModal%s">
        View Students
    </button></td>                             <td style="display:flex;">
             <button class="btn btn-primary" data-toggle="modal" data-target="#view%s">Update</button>
             <form method="post">
             <input type="hidden" value='%s' name="kk">
             <input class="btn btn-danger" style="margin-left:10px;" type="submit" name="su"  value="Delete"></form>
                              </td>
                        </tr>
                    </tbody>
                """ % (h, i[1], i[2], i[3], i[4],i[0],i[0],i[0]))
     h += 1
     print("""
                   <div class="modal fade" id="view%s">
    <div class="modal-dialog modal-md">
        <div class="modal-content custom-modal"> 
            <div class="modal-header custom-modal-header">
                <h3 class="modal-title text-center text-white w-100">Details</h3>
                <button type="button" class="close text-white" data-dismiss="modal">&times;</button>
            </div>
            <form method="post">
            <div class="modal-body">
                <div class="row">
                    <div class="col-lg-6 col-6">
                        <p><strong>Room Number</strong></p>
                        <p style="margin-top:25px;"><strong>Occupancy</strong>
                        <p style="margin-top:30px;"><strong >Total Capacity</strong></p>
                       
                    </div>
                    <div class="col-lg-6 col-6">
                        <p><input type="text" name="rn"  class="form-control" value='%s'></p>
                        <p><input type="text"  class="form-control" value='%s' readonly></p>
                         <p><input type="text" name="tc" class="form-control" value='%s'></p>      
                    </div>
                </div>
            </div>
            <div class="modal-footer">
            <input type="hidden" value='%s' name="d">
             <input class="btn btn-primary" type="submit" name="sub" value="Update">
                <button class="btn btn-danger" data-dismiss="modal">Close</button>
            </div>
        </div></form>
    </div>
</div>
                """ % (i[0],i[2], i[3], i[4],i[0]))
     print("""
         <div class="modal fade" id="studentModal%s" tabindex="-1" role="dialog">
             <div class="modal-dialog modal-lg" role="document">
                 <div class="modal-content">
                     <div class="modal-header bg-info text-white">
                         <h5 class="modal-title" id="studentModalLabel">
                             <i class="fa fa-users"></i> Students in Room
                         </h5>
                         <button type="button" class="close text-white" data-dismiss="modal" aria-label="Close">
                             <span aria-hidden="true">&times;</span>
                         </button>
                     </div>
                     <div class="modal-body">
                         <div class="row">
                         <input type="hidden" value="%s" name="room_id">
     """ % (i[0], i[2]))
     student_query = """
             SELECT s.Name,s.Profile, b.Degree, b.Year 
             FROM book b
             INNER JOIN student s ON b.Student_Name = s.Name
             INNER JOIN rooms r ON b.room_no = r.ID
             WHERE r.Room_Number = %s AND b.Status = 'Paid'
         """
     b.execute(student_query, (i[2]))
     students = b.fetchall()
     if students:
             for st in students:

                 print(f"""
                     <div class="col-md-3 col-6">
                         <div class="card mb-4 shadow-sm border-0">
                             <div class="card-body">
                             <img src="./media/{st[1]}" width="50px;" height="50px;" style="border-radius:30%; margin-left:20px;">
                                 <h5 class="card-title stylish-name">{st[0]}</h5>
                                 
                                 <p class="card-text">
                                     <strong>Degree:</strong> {st[2]}<br>
                                     <strong>Year:</strong> {st[3]}
                                 </p>
                             </div>
                         </div>
                     </div>
                 """)
     else:
             print("""
                 <div class="col-12">
                     <div class="alert alert-warning">No students assigned to this room.</div>
                 </div>
             """)

     print("</div></div></div></div></div>")

print("</div></tbody></table>")
sub=form.getvalue("sub")
rn=form.getvalue("rn")
tc=form.getvalue("tc")
d=form.getvalue("d")
if sub!=None:
    vv=""" UPDATE rooms SET Room_Number='%s',Total_Capacity='%s',Status='Updated' WHERE id='%s' """%(rn,tc,d)
    b.execute(vv)
    a.commit()
    print("""<script>alert('Rooms Updated Successfully!');
    location.href="adrex.py";</script>""")

su=form.getvalue("su")
kk=form.getvalue("kk")
if su!=None:
    s="""Update rooms set Status='Deleted' where id='%s' """%(kk)
    b.execute(s)
    a.commit()
    print("""<script>alert('Rooms Deleted Successfully!');
       location.href="adrex.py";</script>""")


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


#!C:/Users/Dell/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgitb, pymysql, cgi,os
cgitb.enable()
a = pymysql.connect(host="localhost", user="root", password="", database="hostel")
b = a.cursor()
reg = cgi.FieldStorage()
id = reg.getvalue("id")
v = """select * from student where id='%s' """ % (id)
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
  <ul  id="w"><span class="fa fa-hand-o-left"></span> <a href="home.py" style="color:black;">Logout</a></ul></nav><br><br>""" % (id,id,id,id, id, id, id, id, id, id,id))
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
  <div class="col-lg-2"></div>""" % (id, id, id, id, id, id, id, id,id,id,id))
for i in rec:
    print(f""" 
<div class="col-lg-5" style="margin-left:60px;">
    <div class="card" style="background: linear-gradient(135deg, #FF416C 0%, #FF4B2B 100%);
    color: white; padding: 20px; margin-top:90px; height:300px; width:350px;
    border-radius: 15px; box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3); text-align: center; position: relative;">
    
    <!-- Profile Image with Photo Icon -->
    <form enctype="multipart/form-data" method="post">
        <div style="position: relative; display: inline-block;">
            <label for="profileInput">
                <img src="./media/{i[13]}" height="130px" width="130px" 
                style="border-radius: 50%; cursor: pointer; box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);" 
                title="Click to change profile picture">
                <span style="position: absolute; bottom: 10px; right: 10px; 
                background: #fff; border-radius: 60%; padding: 8px; cursor: pointer;">
                    <i class="fa fa-camera" style="color: #333; font-size: 18px;"></i>
                </span>
            </label>
        </div>
        <input type="file" id="profileInput" name="pro" accept="image/*" style="display: none;" 
        onchange="this.form.submit();">
        <input type="hidden" name="change_profile" value="1">
    </form>
    
    <h4 style="font-family: 'Arial', sans-serif; font-weight:900; margin-top: 15px;"> {i[2]} </h4>
    <button class="btn" data-toggle="modal" data-target="#change{i[0]}" style="display: block; margin: 10px auto; 
     background: linear-gradient(45deg, #6A82FB, #FC5C7D, #FFB6B9, #6A1B9A); background-size: 400%; color: white; font-weight: 700;
       border: none; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);border-radius: 50px; padding: 15px 30px; outline: none;">Change Password
      </button>
    </div>  
</div>

""")
    print("""<div class="modal fade" id="change%s">
    <div class="modal-dialog modal-md">
        <div class="modal-content custom-modal"> 
            <div class="modal-header custom-modal-header">
                <h3 class="modal-title text-center text-white w-100">Change Password</h3>
                <button type="button" class="close text-white" data-dismiss="modal">&times;</button>
                </div>
                <div class="modal-body">
                       <form enctype="multipart/form-data" method="post">
                      
                        <div class="form-group">
                       
                            <input type="password" class="form-control" placeholder="New Password" name="np">
                        </div>
                        <div class="form-group">
                       
                            <input type="password" class="form-control" placeholder="Confirm Password" name="cp" >
                        </div>
                        <div class="form-group">
                        <input type="hidden" class="form-control" value="%s" name="op"></div>
                    </div>
                    <div class="modal-footer">
                        <input type="submit" value="Done" class="btn btn-primary" name="log">
                        <input type="button" value="Close" class="btn btn-danger"  data-dismiss="modal">
                    </div>
                </div>
            </div>
       </form>
                </div>     
    </div>""" % (i[0], i[15]))


if len(reg) != None:
    submit = reg.getvalue("log")
    if submit != None:
        profile = reg['pro']
        np = reg.getvalue("np")
        cp = reg.getvalue("cp")
        op = reg.getvalue("op")
        if cp != '' and np != '' and profile.filename == '':
            if cp == np:
                if op != np:
                    u = """UPDATE student SET Password='%s' WHERE id='%s' """ % (np, id)
                    b.execute(u)
                    a.commit()
                    print("""<script> alert('Your Password is Updated Successfully')
                                      location.href="home.py"</script>""")
                else:
                    print("""<script> alert('Please Enter the New Password')</script>""")
            else:
                print("""<script> alert('Please Enter the Same Password') </script>""")



if reg.getvalue("change_profile"):
    profile = reg['pro']
    if profile.filename != '':
        fn = os.path.basename(profile.filename)
        open("media/" + fn, "wb").write(profile.file.read())
        u = """UPDATE student SET Profile='%s' WHERE id='%s' """ % (fn, id)
        b.execute(u)
        a.commit()
        print(
            """<script> alert('Profile updated successfully!'); location.href="sprofile.py?id=%s"; </script>""" % (id))



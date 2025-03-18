#!C:/Users/Dell/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgitb, pymysql,smtplib,cgi
cgitb.enable()
a = pymysql.connect(host="localhost", user="root", password="", database="hostel")
b = a.cursor()
form = cgi.FieldStorage()
d="select * from warden"
b.execute(d)
re=b.fetchall()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Warden Dashboard</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">
  <script src="https://cdn.jsdelivr.net/npm/jquery@3.7.1/dist/jquery.slim.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.3/css/all.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
 <style>
   h1{
      font-family: 'Times New Roman', Times, serif; 
      color: black; 
      text-align: center;
      padding-top: 2%;    
    }
  .contain .row .card{
    padding-left: 15px;
    padding-right: 15px;
    padding-top: 10px;
    top: 1%;
    box-shadow: 5px 5px 20px black;
    border-radius: 20px; 
   }
    .contain input{
      border-radius: 5px;
      border-color: black;

    }
    .contain button{
      border-radius: 5px;
      border-color: black;
    }    
.form-group span{
  border-radius: 5px;
  font-size: 25px;
  text-align: center;
  width: 40px;  
}
  .card {
    max-width: 600px;
    background: linear-gradient(135deg, #ffafbd, #ffc3a0);
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.2);
    color: #4f4f4f;
    font-weight: 500;
}
 .card h2 {
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
        .card h2:after {
            content: '';
            position: absolute;
            width: 50px;
            height: 3px;
            background: #007bff;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
        }
 </style>
</head>
<body style="background-color:lightgrey">  
<div class="contain">    
<div class="row">
<div class="col-lg-4">
</div>   
<div class="col-lg-5">
  <br> <br>
        <form  enctype="multipart/form-data" method="post">
          <div class="card">
            <h1>Forgot Password</h1> 
            <div class="form-group">
              
                  <label style="font-weight:600; font-size:20px; color:white;">Email</label>
                <input type="email" class="form-control" placeholder="Enter Mail-ID" name="email" required>
        
              </div>  <br>
            <div class="row">
              <div class="col-lg-2"></div>
              <div class="col-lg-4">
                <div class="form-group">
                  <input type="submit" class="form-control" style="color: white; background-color: blue;" name="sub"></div></div>
                  <div class="col-lg-4">  
                    <div class="form-group">  
                  <button type="reset"  class="form-control" style="color: white; background-color: red; ">Cancel</button> </div>
                </div>
              </div>   </div>  
 </form>
      </div> <div class="col-lg-4">
            </div> </div> </div>
</body>
</html>""")


l=''
email = form.getvalue("email")
submit=form.getvalue("sub")
if submit!=None:
        qu = """select * from warden WHERE Email ='%s' and Status='Unblocked'"""%(email)
        b.execute(qu)
        rec = b.fetchall()
        for i in rec:
            l= i[12]
            fromadd = 'dharshinitharika213@gmail.com'
            Password = 'ecnl invr idrc mpdv'
            toadd = email
            subject = "Regarding Password given by Admin"
            body = "Your Password is: {}".format(l)
            msg = """Subject:{} \n\n {}""".format(subject, body)
            server = smtplib.SMTP("smtp.gmail.com:587")
            server.ehlo()
            server.starttls()
            server.login(fromadd, Password)
            server.sendmail(fromadd, toadd, msg)
            server.quit()
            print("""
                <script> alert('Your Password has been send to your mail')
                </script>""")

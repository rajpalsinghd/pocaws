from flask import *
import jinja2
import requests

app=Flask(__name__)

@app.route("/api/user")
def registration():
 return render_template("add_user.html")

@app.route("/api/user/register",methods=["POST"])
def register():
 if request.method=="POST":
  try:
   username=request.form['name']
   email=request.form['email']
   domain=request.form['domain']
   user={"username":username,"email":email,"domain":domain}
   #instead of localhost use ip address of instance(AWS instance)
   response=requests.post("http://localhost:4000/api/user/register",json={"user":user})   
   if response.status_code==200:
    return render_template("success.html",username=username)
   else:
    return Response("Some error or malformed data",status=400)
  except Exception as e:
   #add logs
   return "some error"

@app.route("/api/user/getusers")
def get_users():
 try:
  #instead of localhost use ip address of instance(AWS instance)
  response=requests.post("http://localhost:4000/api/user/getusers")
  if response.status_code==200:
   users=response.json()
   users=users['users']
   return render_template("users.html",users=users)
  else:
   return "Some error/error.html"
 except Exception as e:
  print(e)


if __name__=="__main__":
 app.run()

from flask import Flask, render_template, url_for, request, redirect #can feed an html file
import csv
app = Flask(__name__)

#gives instructions for the main route
@app.route('/')
def my_home():
    return render_template('index.html') #looks by default in templates folder, so store html there

#add another branch
# @app.route('/project.html')
# def my_projects():
#     return render_template('project.html') 

# @app.route('/about.html')
# def my_about():
#     return render_template('about.html')

# @app.route('/index.html')
# def return_home():
#      return render_template('index.html') 

# @app.route('/contact.html')
# def my_contact():
#      return render_template('contact.html') 

#Use URL syntax to dynamically accept url parameters
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name) 

#We will use the csv function instead
# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email = data["email"] #get from the dictionary we formated in the submit form function
#         subject = data["subject"]
#         message = data["message"]
#         file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"] #get from the dictionary we formated in the submit form function
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) #can feed some options, see documentation
        csv_writer.writerow([email,subject,message]) #can pass in as a list

@app.route('/submit_form', methods=['POST', 'GET']) #methods called post and get
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict() #get everything as a dictionary
        write_to_csv(data)
        return redirect('/thankyou.html') #use the redirect method from flask
    else:
        return 'something went wrong'
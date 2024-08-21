from flask import Flask, render_template,request,redirect
from flask_wtf import CSRFProtect
from flask_wtf.csrf import CSRFError
from flask import *


# Local Modules
from forms import ContactForm
from build_table_email import table_email
from send_telegram_msg import sending_Telegram_Message as telegram_bot

app = Flask(__name__)
app.secret_key='bf6cc269e9594e9caef019ecdc2f4ea1'


@app.route('/')
@app.route('/home/')
def homepage():
    
    return render_template("home.html")


@app.route('/Industry/')
def Industrypage():
    return render_template("Industry.html")


@app.route('/temprary/')
def temprarypage():
    return render_template("temprary.html")

@app.route('/construction/')
def Constructionpage():
    return render_template("construction.html")


@app.route('/predictive/')
def use1page():
    return render_template("predictive_maintenance_use.html")

@app.route('/automated/')
def Automatedpage():
    return render_template("Automated-warehouse.html")
@app.route('/supply/')
def Supply_page():
    return render_template("Supply_chain.html")


@app.route('/security/')
def Securitypage():
    return render_template("security.html")



@app.route('/enhanced/')
def Enhancedpage():
    return render_template("enhanced.html")





@app.route('/manufacturing/')
def Manufacturingpage():
    return render_template("manufacturing.html")





@app.route('/retail/')
def Retail_page():
    return render_template("retail.html")



@app.route('/logistics/')
def Logistics_page():
    return render_template("logistics.html")


#Blog page route
@app.route('/blog/')
def blog_page():
    return render_template("blog.html")
#contact-us page

@app.route('/contact',methods=['GET','POST'])
def contact_page():
    form=ContactForm()
    if request.method=='GET':
        return render_template("contact_us.html",form=form)
    elif request.method=='POST':
        if form.validate_on_submit():
            name=form.name.data
            email=form.email.data
            # print(name,email)
            mobile=form.mobile.data
            # print(mobile)
            individual=form.individual.data
            company_name=form.company_name.data
            help=form.help.data

            """
            Sending Email Start
            """
            user_data = {
                "Platform":[F"Argus Website"],
                'Name': [F"{name}"],
                "Email": [F"{email}"],
                'Mobile': [F"{mobile}"],
                "Individual": [F"{individual}"],
                'Company Name': [F"{company_name}"],
                "Message": [F"{help}"]
            }

            table_email(user_data=user_data)
            """
            Sending Email Start
            """
            msg=F'''Platform : Argus Website\nName: {name}\nEmail : {email}\nMobile : {mobile}\nIndividual : {individual}\nCompany Name : {company_name}\nMessage : {help}'''
            # Email Alert 
            status=telegram_bot(msg)
            print(status)
            # Telegram Bot & Send Alert
           




            flash("You were successfully submitted the form!")
            return redirect('/contact')
        print("PPOST Request")
        print(form.errors)
        # return F'Your Contact Failed'
        return render_template("contact_us.html",form=form)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
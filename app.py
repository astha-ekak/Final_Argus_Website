from flask import Flask, render_template

app = Flask(__name__)

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

@app.route('/contact/')
def contact_page():
    return render_template("contact_us.html")

if __name__ == "__main__":
    app.run(debug=True)
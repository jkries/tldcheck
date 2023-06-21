from flask import Flask,render_template,request
import whois

def is_domain_available(domain):
    try:
        get_info = whois.whois(domain)
        return False
    except:
        return True
    
app = Flask(__name__)
 
 
@app.route("/",methods=["POST","GET"])
def home():
    checkData = "Nothing yet..."
    if request.method == "POST":
        checkDomain = request.form.get("checkDomain")
        domainOpen = is_domain_available(checkDomain)
        if domainOpen:
            checkData = "<div class='available'>" + checkDomain + " is AVAILABLE! &#9989;</div>"
        else:
            checkData = "<div class='taken'>" + checkDomain + " is taken. &#10060;</div>"
        return checkData
    return render_template('home.html', checkData = checkData)
 
 
if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=80)
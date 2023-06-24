from flask import Flask,render_template,request
import whois
import os

def is_domain_available(domain):
    try:
        get_info = whois.whois(domain)
        global expirationDate
        expirationDate = str(get_info.expiration_date)
        return False
    except:
        return True
    
app = Flask(__name__)
 
 
@app.route("/",methods=["POST","GET"])
def home():
    checkData = "Nothing yet..."
    if request.method == "POST":
        checkDomain = request.form.get("checkDomain")
        tldType = os.path.splitext(checkDomain) #Check for tdl type
        tldExt = tldType[1]
        if tldExt == "":
            tldExt = ".com"
            checkDomain = checkDomain + ".com"
        domainOpen = is_domain_available(checkDomain)
        if domainOpen:
            checkData = "<div class='available'><strong>" + checkDomain + "</strong> is AVAILABLE! &#9989;</div>"
        else:
            checkData = "<div class='taken' title='"+ expirationDate +"'><strong>" + checkDomain + "</strong> is taken. &#10060;<br><small>Expires "+ expirationDate[:10] +"</small></div>"
        return checkData
    return render_template('home.html', checkData = checkData)
 
 
if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=80)
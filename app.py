from flask import Flask,render_template,request
import whois
import os

def is_domain_available(domain):
    try:
        get_info = whois.whois(domain)
        global expirationDate
        expirationDate = str(get_info.expiration_date)
        if len(expirationDate) == 19:
            expirationDate = expirationDate[:10]
        return False
    except:
        return True
    
app = Flask(__name__)

@app.route("/get")
def checkDomain():
    checkDomain = request.args.get('domain')
    tldType = os.path.splitext(checkDomain) #Check for tdl type
    tldExt = tldType[1]
    print(tldExt)
    if tldExt == "":
        tldExt = ".com"
        checkDomain = checkDomain + ".com"
    domainOpen = is_domain_available(checkDomain)
    if domainOpen:
        return checkDomain + " is AVAILABLE"
    else:
        return checkDomain + " is TAKEN until " + expirationDate
 
@app.route("/",methods=["POST","GET"])
def home():
    checkData = "Nothing yet..."
    if request.method == "POST":
        checkDomain = request.form.get("checkDomain")
        tldType = os.path.splitext(checkDomain) #Check for tdl type
        tldExt = tldType[1]
        print(tldExt)
        if tldExt == "":
            tldExt = ".com"
            checkDomain = checkDomain + ".com"
        domainOpen = is_domain_available(checkDomain)
        if domainOpen:
            checkData = "<div class='available'><strong>" + checkDomain + "</strong> &#9989;</div>"
        else:
            checkData = "<div class='taken' title='"+ expirationDate +"'> <strong>" + checkDomain + "</strong> &#10060;<br><small>Expires "+ expirationDate +"</small><br><a class='linkVisit' target= '_blank' href='http://www."+ checkDomain +"'>&#128279;</a></div>"
        return checkData
    return render_template('home.html', checkData = checkData)
 
 
if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=80)
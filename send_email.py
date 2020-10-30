import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
import requests

def horoscope(star,day):
    star=star.lower()
    print(f"https://www.astrology.com/horoscope/daily/{day}{star}.html")
    r=requests.get(f"https://www.astrology.com/horoscope/daily/{day}{star}.html",
               headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    main=soup.find("div",{"class":"horoscope-main grid grid-right-sidebar primis-rr"})
                     
    return main.find("p").text

def send_email(email,sign):
    admin="manchaandy253@gmail.com"
    passw='123456789cm'
    user=email
    message=[]
    print(sign)
    if sign!="e":
        message.append(horoscope(sign,"yesterday/"))
        message.append(horoscope(sign,""))
        message.append(horoscope(sign,"tomorrow/"))
        print(message[1])
        msg=MIMEText(str(message[1]))
        msg['Subject']="Horoscope"
        msg["To"]=user
        msg["From"]=admin

        gmail=smtplib.SMTP('smtp.gmail.com',587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login(admin,passw)
        gmail.send_message(msg)
        return (True,message)
    return (False,[])
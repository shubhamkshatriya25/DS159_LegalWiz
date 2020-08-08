from twilio.rest import Client

import schedule
import sqlite3
from datetime import timedelta
import datetime
from django.core.mail import send_mail
from django.conf import settings

def job():
    db = sqlite3.connect('db.sqlite3')
    print('connected')
    cur =db.cursor()
    cur.execute("SELECT nextHearing FROM backend_hearing;")
    print('selected')

    row = cur.fetchall()
    li = list(sum(row, ()))  
    print(li)
    
    cur.execute("SELECT conclusion FROM backend_hearing;")
    print('selected')

    row = cur.fetchall()
    li4 = list(sum(row, ()))  
    #print(li4)
    
        
    dt = (str(datetime.datetime.now())) 
    
    for (i,j) in zip(li, li4):
            
        if str(datetime.datetime.strptime(dt, '%Y-%m-%d %H:%M:%S.%f').date() + timedelta(days=6)) == i:
            print('7 days ago')
            cur.execute("SELECT case_no, title FROM backend_hearing WHERE nextHearing='"+str(i)+"' and conclusion='"+str(j)+"'")
            r = cur.fetchall()
                        
            account_sid = 'ACee6ec8d2c1aaxxxxxxxxxxxxxxxxx'
            auth_token = '5a96e76da74c177xxxxxxxxxxxxxxxxx'
            client = Client(account_sid, auth_token)

            subject = 'LegalWiz account password reset'
            message = "Your case number: "+str(r[0][0])+", and case title: "+str(r[0][1])+", is scheduled on: "+str(i)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user, ]
        
            # print(r[0][0])
            # print(r[0][1])
            message = client.messages.create(
                        body="Your case number: "+str(r[0][0])+", and case title: "+str(r[0][1])+", is scheduled on: "+str(i),
                        from_='+14xxxxxxxxx',
                        to='+91xxxxxxxxxx'
                    )
            send_mail(subject, message, email_from, recipient_list)
            print(message.sid)
            
        if str(datetime.datetime.strptime(dt, '%Y-%m-%d %H:%M:%S.%f').date() + timedelta(days=2)) == i:
            print('3 days ago')
            cur.execute("SELECT case_no, title FROM backend_hearing WHERE nextHearing='"+str(i)+"' and conclusion='"+str(j)+"'")
            r = cur.fetchall()
                        
            account_sid = 'ACee6ec8d2c1aaa9xxxxxxxxxxxxxxxxx'
            auth_token = '5a96e76da74c177xxxxxxxxxxxxxxxxx'
            client = Client(account_sid, auth_token)
            # print(r[0][0])
            # print(r[0][1])
            message = client.messages \
                .create(
                        body="Your case number: "+str(r[0][0])+", and case title: "+str(r[0][1])+", is scheduled on: "+str(i),
                        from_='+14xxxxxxxxxx',
                        to='+91xxxxxxxxxx'
                    )

            print(message.sid)
            
         
        if str(datetime.datetime.strptime(dt, '%Y-%m-%d %H:%M:%S.%f').date() + timedelta(days=1)) == i:
            print('1 day ago ')
            cur.execute("SELECT case_no, title FROM backend_hearing WHERE nextHearing='"+str(i)+"' and conclusion='"+str(j)+"'")
            r = cur.fetchall()
            
            account_sid = '5a96e76da74c177xxxxxxxxxxxxxxxxx'
            auth_token = '5a96e76da74c177xxxxxxxxxxxxxxxxx'
            client = Client(account_sid, auth_token)
            # print(r[0][0])
            # print(r[0][1])
            message = client.messages \
                .create(
                        body="Your case number: "+str(r[0][0])+", and case title: "+str(r[0][1])+", is scheduled on: "+str(i),
                        from_='+14752566797',
                        to='+917228801122'
                    )

            print(message.sid)
       
    
schedule.every().day.at("10:00").do(job)

while True:
    schedule.run_pending()
    # time.sleep(1)


    
    

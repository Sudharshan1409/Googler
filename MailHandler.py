import os
import getpass
import smtplib
import ssl
import colorama


class MailHandler:
    def __init__(self, emails):
        self.__message = """Subject: Googler Prize Distribution\nFrom: From CSI Region-V Student Convention team <sudarshan61kv@gmail.com>\nTo:  <{}>\nHey, Thanks for Participating in Googler. We are pleased to say that, you have won 1st/2nd Prize in the competition. So please do attend the Prize Distribution Program today to collect the Prizes.
                  """
        self.__port = 465
        self.__emails = emails
        
    
    def SendMail(self):
        try:
            email = 'sudarshan61kv@gmail.com'
            password = '1409sudu@8095@gmailpasswd'
            context = ssl.create_default_context()
            try:
                with smtplib.SMTP_SSL("smtp.gmail.com", self.__port, context=context) as server:
                    server.login(email, password)
                    for email_id, score in self.__emails:
                        print("Message sending to", email_id)
                        server.sendmail(email, email_id, self.__message.format(email_id))
            except Exception as e:
                print(e.args)
                print(colorama.Fore.RED, "Hey type correct password", colorama.Fore.WHITE)
        except:
            print("\nbye ")
    
if __name__ == '__main__':
    m = MailHandler([['abhijithabhi191096@gmail.com',50],['meghanaa3521@gmail.com',40]])
    m.SendMail()

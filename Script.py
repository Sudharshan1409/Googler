import pandas as pd
import numpy as np 
from MailHandler import MailHandler

l = []
class Responce():
    def __init__(self,name,email,college,phone,l):
        self.name = name
        self.answers = l.copy()
        self.email = email
        self.college = college 
        self.phone = phone 
        self.score = 0
    
    def __repr__(self):
        return f"Name : {self.name}\nEmail : {self.email}\nCollege : {self.college}\nPhone : {self.phone}\nAnswers : {self.answers}\nScore : {self.score}"

responces = np.array(pd.read_csv('Answers1.csv'))
answer_key = open('answer_key1.txt','r')
answer = answer_key.read().split('\n')
for i,res in enumerate(responces):
    print(res)
    r = Responce(res[2],res[1],res[4],res[3],res[5:])
    for j,ans in zip(range(5,len(res)),answer):
        pass
        if ans.lower() in str(res[j]).lower() or str(res[j]).lower() in ans.lower():
            print('done',res[j],ans)
            r.score += 1
        else:
            print('Not done',res[j],ans)
    l.append(r)
    print(r)
email = []
email_file = open('participants.txt','w')
while True:
    emails = []
    score = int(input('Enter the Score limit : '))
    for i in l:
        if i.score >= score:
            emails.append([i.email,i.score,i.name,i.phone,i.college])
        email_file.write('Name : ' + str(i.name) + '\n' + 'Email : ' + i.email + '\n' + 'Phone : ' + str(i.phone) + '\n' + 'College : ' + str(i.college) + '\n' + 'Score : ' + str(i.score) + '\n\n\n')
    state = input(f"The number of students selected are {len(emails)} do you wish to continue yes/no : ")
    if state.lower() == 'yes':
        break
    
email_file.close()
print(email)


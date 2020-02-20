import pandas as pd
import numpy as np

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
        return f"Name : {self.name}\nEmail : {self.email}\nCollege : {self.college}\nPhone : {self.phone}\nScore : {self.score}"

responces = np.array(pd.read_csv('Answers2.csv'))
answer_key = open('answer_key2.txt','r')
answer = answer_key.read().split('\n')
emails = []

email_file = open('email.txt','r')
records = email_file.read().split('\n')
print(records)
for i in range(len(records)):
    if records[i]:
        records[i] = records[i].split(':')
        emails.append(records[i][0])
print(records)
print(emails)

for i,res in enumerate(responces):
    print(res)
    if res[1] in emails:
        index = emails.index(res[1])
        r = Responce(records[index][2],res[1],records[index][4],records[index][3],res[2:])
        for j,ans in zip(range(2,len(res)),answer):
            pass
            if ans.lower() in str(res[j]).lower() or str(res[j]).lower() in ans.lower():
                print('done',res[j],ans)
                r.score += 1
            else:
                print('Not done',res[j],ans)
        l.append(r)
        print(r)

for i in range(len(l)):
    max = l[i].score
    pos = i
    for j in range(i+1,len(l)):
        if max < l[j].score:
            max = l[j].score
            pos = j
    l[i],l[pos] = l[pos],l[i]
print()
print()
print('===============================================================================')
for i in l:
    print(i)
    print()


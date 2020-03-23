import pandas as pd 
import os
assump={'O+':[1,1,1],'O-':[1,1,1],'AB':[1,1,1],'A':[2,2,1],'B':[3,1,1]}
assump=pd.DataFrame(assump,index=['branch1','branch2','branch3'])
print(assump)
b1={'O+':['JAYNIT','',''],'O-':['NAVEEN','',''],'AB':['SANCHIT','',''],'A':['KARTIK','GOURAB',''],'B':['KALPAJEET','SOURAB','TULSI']}
b1=pd.DataFrame(b1,index=['1','2','3'])
b2={'O+':['JAY','',''],'O-':['LUCKY','',''],'AB':['SACHIN','',''],'A':['AAKASH','ROHIT',''],'B':['PARAM','','']}
b2=pd.DataFrame(b2,index=['1','2','3'])
b3={'O+':['PREM','',''],'O-':['ALLU','',''],'AB':['ASHISH','',''],'A':['ANMOL','',''],'B':['AMAN','','']}
b3=pd.DataFrame(b3,index=['1','2','3'])
b1c={'JAYNIT':3303251234,'NAVEEN':2232001234,'SANCHIT':4544500123,'KARTIK':4444500123,'GOURAB':4542500023,'KALPAJEET':4224450000,'SOURAB':4522445000,'TULSI':4541245000}
b2c={'JAY':33230325,'LUCKY':4223200123,'SACHIN':4435445789,'AAKASH':4543544455,'ROHIT':4434542525,'PARAM':4322244545}
b3c={'PREM':3232312345,'ALLU':2232323123,'ASHISH':4424354450,'ANMOL':4444532456,'AMAN':4542442523}
print('from which branch you require blood')
a=int(input())
print(' which blood type')
b=str(input())
if(a==1):
    if(b=='O+'):
        print('this are the availabe donors')
        print(b1['O+'])
        print('select the donor')
        c=str(input())
        if(c=='JAYNIT'):
             print('contact number is')           
             print(b1c['JAYNIT'])               
if(a==1):
    if(b=='O-'):
        print('this are the availabe donors')
        print(b1['O-'])
        print('select the donor')
        c=str(input())
        if(c=='NAVEEN'):
             print('contact number is')           
             print(b1c['NAVEEN']) 
if(a==1):
    if(b=='AB'):
        print('this are the availabe donors')
        print(b1['AB'])
        print('select the donor')
        c=str(input())
        if(c=='SANCHIT'):
             print('contact number is')           
             print(b1c['SANCHIT'])
if(a==1):
    if(b=='A'):
        print('this are the availabe donors')
        print(b1['A'])
        print('select the donor')
        c=str(input())
        if(c=='KARTIK'):
             print('contact number is')           
             print(b1c['KARTIK'])
        if(c=='GOURAB'):
             print('contact number is')           
             print(b1c['GOURAB'])     
if(a==1):
    if(b=='B'):
        print('this are the availabe donors')
        print(b1['B'])
        print('select the donor')
        c=str(input())
        if(c=='KALPAJEET'):
             print('contact number is')           
             print(b1c['KALPAJEET'])
        if(c=='SOURAB'):
             print('contact number is')           
             print(b1c['SOURAB'])
        if(c=='TULSI'):
             print('contact number is')           
             print(b1c['TULSI'])                             
if(a==2):
    if(b=='O+'):
        print('this are the availabe donors')
        print(b2['O+'])
        print('select the donor')
        c=str(input())
        if(c=='JAY'):
             print('contact number is')           
             print(b2c['JAY'])
if(a==2):
    if(b=='O-'):
        print('this are the availabe donors')
        print(b2['O-'])
        print('select the donor')
        c=str(input())
        if(c=='LUCKY'):
             print('contact number is')           
             print(b2c['LUCKY'])
        
if(a==2):
    if(b=='AB'):
        print('this are the availabe donors')
        print(b2['AB'])
        if(c=='SACHIN'):
             print('contact number is')           
             print(b2c['SACHIN'])
if(a==2):
    if(b=='A'):
        print('this are the availabe donors')
        print(b2['A'])
        if(c=='AAKASH'):
             print('contact number is')           
             print(b2c['AAKASH'])
        if(c=='ROHIT'):
             print('contact number is')           
             print(b2c['ROHIT'])
                 
if(a==2):
    if(b=='B'):
        print('this are the availabe donors')
        print(b2['B'])
        if(c=='PARAM'):
             print('contact number is')           
             print(b2c['PARAM'])                        
if(a==3):
    if(b=='O+'):
        print('this are the availabe donors')
        print(b3['O+'])
        if(c=='PREM'):
             print('contact number is')           
             print(b3c['PREM'])
if(a==3):
    if(b=='O-'):
        print('this are the availabe donors')
        print(b3['O-'])
        if(c=='ALLU'):
             print('contact number is')           
             print(b3c['ALLU'])
if(a==3):
    if(b=='AB'):
        print('this are the availabe donors')
        print(b3['AB'])
        if(c=='ASHISH'):
             print('contact number is')           
             print(b3c['ASHISH'])
if(a==3):
    if(b=='A'):
        print('this are the availabe donors')
        print(b3['A'])
        if(c=='ANMOL'):
             print('contact number is')           
             print(b3c['ANMOL'])
if(a==3):
    if(b=='B'):
        print('this are the availabe donors')
        print(b3['B'])
        if(c=='AMAN'):
             print('contact number is')           
             print(b3c['AMAN'])                        
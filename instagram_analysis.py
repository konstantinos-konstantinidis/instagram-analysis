# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 13:40:45 2018

@author: Κωστας
"""

import json
import calendar
import datetime
import numpy
import csv


instagram_data_path='C:\\Users\\Κωστας\\Downloads\\konstantinos.konstantinidis_20180920'
username='konstantinos.konstantinidis'

jfile_path=instagram_data_path+'\\messages.json'
jfile=open(jfile_path,'r',encoding='utf-8',errors='ignore')
dataz=json.load(jfile)
jfile.close


name_list=[]
total_msg=[]
my_msg=[]
my_words=[]
other_words=[]

msg_year=[]
msg_month=[]
msg_day=[]
msg_hour=[]
msg_mine=[]

n=len(dataz)
for i in range(0,n):
    if len(dataz[i]['participants'])==2:
        name_list.append(dataz[i]['participants'][0])
        name_list.append(dataz[i]['participants'][1])
        name_list.pop(name_list.index(username))
        total_msg.append(len(dataz[i]['conversation']))
        counter=0
        words=0
        owords=0
        for item in range(0,len(dataz[i]['conversation'])):
            if dataz[i]['conversation'][item]['sender']==username:
                counter=counter+1
                msg_mine.append('me')
                try:
                    words=words+len(dataz[i]['conversation'][item]['text'].split(' '))
                except:
                    pass  
            if not(dataz[i]['conversation'][item]['sender']==username):
                msg_mine.append('others')
                try:
                    owords=owords+len(dataz[i]['conversation'][item]['text'].split(' '))
                except:
                    pass
            t_year=(dataz[i]['conversation'][item]['created_at'].split('T')[0].split('-')[0])
            t_month=(dataz[i]['conversation'][item]['created_at'].split('T')[0].split('-')[1])
            t_day=(dataz[i]['conversation'][item]['created_at'].split('T')[0].split('-')[2])
            ymd=datetime.date(int(t_year),int(t_month),int(t_day))
            msg_year.append(ymd.year)
            msg_month.append(calendar.month_name[ymd.month])
            msg_day.append(calendar.day_name[(ymd.weekday())])
            msg_hour.append(dataz[i]['conversation'][item]['created_at'].split('T')[1].split(':')[0])
            
        my_msg.append(counter)
        my_words.append(words)
        other_words.append(owords)
        
total_words=(numpy.array(my_words)+numpy.array(other_words)).tolist()


final1=[['name','total messages','my messages','total words','my words','msg percent','word percent']]
for row in range(0,len(name_list)):
    try:
        msg=my_msg[row]/total_msg[row]
    except:
        msg=0
    try:
        wrd=my_words[row]/total_words[row]
    except:
        wrd=0
    final1.append([name_list[row],total_msg[row],my_msg[row],total_words[row],my_words[row],msg,wrd])
with open('insta_conv_report.csv','w',newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerows(final1)
print('number of messages sent/receved report generated')


fin_mt=[['year','month','weekday','hour','mine']]
for row in range(0,len(msg_year)):
    fin_mt.append([msg_year[row],msg_month[row],msg_day[row],msg_hour[row],msg_mine[row]])
with open('insta_msg_time.csv','w',newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerows(fin_mt)
print('time of messages report generated')












jfile_path=instagram_data_path+'\\connections.json'
jfile=open(jfile_path,'r',encoding='utf-8',errors='ignore')
fol=json.load(jfile)
jfile.close

fo_year=[]
fo_month=[]
fo_day=[]
fo_hour=[]

key_list=list(fol['followers'].keys())
for item in key_list:
    t_year=fol['followers'][item].split('-')[0]
    t_month=fol['followers'][item].split('-')[1]
    t_day=fol['followers'][item].split('-')[2].split('T')[0]
    ymd=datetime.date(int(t_year),int(t_month),int(t_day))
    fo_year.append(ymd.year)
    fo_month.append(calendar.month_name[ymd.month])
    fo_day.append(calendar.day_name[ymd.weekday()])
    fo_hour.append(fol['followers'][item].split('-')[2].split('T')[1].split(':')[0])


fin_fol=[['year','month','weekday','hour']]
for row in range(0,len(fo_year)):
    fin_fol.append([fo_year[row],fo_month[row],fo_day[row],fo_hour[row]])
with open('insta_followers_time.csv','w',newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerows(fin_fol)
print('time of followers report generated')








jfile_path=instagram_data_path+'\\likes.json'
jfile=open(jfile_path,'r',encoding='utf-8',errors='ignore')
likez=json.load(jfile)
jfile.close


n=len(likez['media_likes'])
allikes=[]
num_likes=[]
li_year=[]
li_month=[]
li_day=[]
li_hour=[]
for i in range(0,n):
    allikes.append(likez['media_likes'][i][1])
ppl=list(set(allikes))
for i in range(0,len(ppl)):
    num_likes.append(0)
for i in range(0,n):
    t_name=likez['media_likes'][i][1]
    num_likes[ppl.index(t_name)]=num_likes[ppl.index(t_name)]+1
    t_year=likez['media_likes'][i][0].split('-')[0]
    t_month=likez['media_likes'][i][0].split('-')[1]
    t_day=likez['media_likes'][i][0].split('-')[2].split('T')[0]
    ymd=datetime.date(int(t_year),int(t_month),int(t_day))
    li_year.append(ymd.year)
    li_month.append(calendar.month_name[ymd.month])
    li_day.append(calendar.day_name[ymd.weekday()])
    li_hour.append(likez['media_likes'][i][0].split('-')[2].split('T')[1].split(':')[0])
    
    
fin_like=[['name','likes']]
for row in range(0,len(ppl)):
    fin_like.append([ppl[row],num_likes[row]])
with open('insta_like_report.csv','w',newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerows(fin_like)
print('like report generated')

fin_li=[['year','month','weekday','hour']]
for row in range(0,len(li_year)):
    fin_li.append([li_year[row],li_month[row],li_day[row],li_hour[row]])
with open('insta_likes_time.csv','w',newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerows(fin_li)
print('time of likes report generated')

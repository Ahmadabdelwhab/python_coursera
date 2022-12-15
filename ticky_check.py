#!/usr/bin/env python3

import re
import operator
import csv
error_regex = r'ticky: ERROR ([\w\s]*)'
user_regex  = r'\((.*)\)' 
error_count:dict[str,int] = {}
user_activities:dict[str , list[int]] ={}
##### parsing


with open("syslog.log" , "r") as f:
    for log in f.readlines():
        user_name = re.search(user_regex , log).group(1).strip()
        if user_name not in user_activities:
                user_activities[user_name] = [0]*2
        if "ERROR" in log:
            error = re.search(error_regex , log).group(1).strip()
            
            if error not in error_count:
                error_count[error] = 0
                
            error_count[error]+=1
            user_activities[user_name][1]+=1
            
        if "INFO" in log:
            user_activities[user_name][0]+=1
####sorting
error =sorted(error_count.items(),key = operator.itemgetter(1),reverse=True); 
per_user =sorted(user_activities.items(),key = operator.itemgetter(0)); 

####writing to file

with open("error_messages.csv","w") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Error" , "Count"]);
    for err , count in error:
        csv_writer.writerow([err , count])
with open("user_statistics.csv" , "w") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(("Username", "INFO", "ERROR"));
    for user , activities in per_user:
        info_count , err_count = activities
        csv_writer.writerow([user , info_count , err_count])    
    


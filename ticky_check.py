#!/usr/bin/env python3
# May 27 11:45:40 ubuntu.local ticky: ERROR: Created ticket [#1234] (username)
# Jun 1 11:06:48 ubuntu.local ticky: ERROR: Connection to DB failed (username)
# Jan 31 00:0939 ubuntu,local ticky: INFO Created ticket [#4217] (mdouglas)
# Jan 31 001625 ubuntu,local ticky INFO closed ticket [#1754] (noel)
# Jan 31 00:2130 ubuntu,local ticky: ERROR The ticket was modified while updating (breee)
# Jan 31 00:4434 ubuntu.local ticky: ERROR Permission denied while closing ticket (ac)
# Jan 31 01:0050 ubuntu,local ticky: INFO Commented on ticket [#4709] (blossom)
# Jan 31 01:2916 ubuntu.local ticky: INFO Commented on ticket [#651&] (rr.robinson)
# Jan 31 01:3312 ubuntu,local ticky: ERROR Tried to add information to closed ticket (mcintosh)
# Jan 31 014310 ubuntu,local ticky ERROR Tried to add information to closed ticket (jackowens
# Jan 31 01:4929 ubuntu,local ticky: ERROR Tried to add information to closed ticket (mdouglas)
# Jan 31 02:3004 ubuntu,local ticky ERROR Timeout while retrieving information (oren)
# Jan 31 00:2130 ubuntu.local ticky ERROR The ticket was modified while updating (breee)
# Jan 31 00:4434 ubuntu,local ticky ERROR Permission denied while closing ticket (ac)
# Jan 31 01:3312 ubuntu.local ticky ERROR Tried to add information to closed ticket (mcintosh)
# Jan 31 01:4310 ubuntu,local ticky: ERROR Tried to add information to closed ticket (jackowens
# Jan 31 01:4929 ubuntu.local ticky: ERROR Tried to add information to closed ticket (mdouglas)
# Jan 31 02:3004 ubuntu,local ticky ERROR Timeout while retrieving information (oren)
# Jan 31 02:553I ubuntu.local ticky ERROR Ticket doesn't exist (xlg)
# Jan 31 03:0535 ubuntu,local ticky ERROR Timeout while retrieving information (ahmed.miller)
# Jan 31 03:0&55 ubuntu.local ticky ERROR Ticket doesn't exist (blossom)
# Jan 31 03:3927 ubuntu,local ticky: ERROR The ticket was modified while updating (bpacheco)


import re
import csv
import operator
error_regex = r'ticky: ERROR ([\w\s]*)'
user_regex  = r'\((.*)\)' 
error_count:dict[str,int] = {}
user_activities:dict[str , list[int]] ={}
with open("syslog.log" , "r") as f:
    for log in f.readlines():
        user_name = re.search(user_regex , log)[1].strip()
        if user_name not in user_activities:
                user_activities[user_name] = [0]*2
        if "ERROR" in log:
            error = re.search(error_regex , log)[1].strip()
            
            if error not in error_count:
                error_count[error] = 0
                
            error_count[error]+=1
            user_activities[user_name][1]+=1
            
        if "INFO" in log:
            user_activities[user_name][0]+=1

error_count =sorted(error_count.items(),key = operator.itemgetter(1),reverse=True); 
user_activities =sorted(user_activities.items(),key = operator.itemgetter(0),reverse=True); 
print(error_count)
print("\n"*7)
print(user_activities)



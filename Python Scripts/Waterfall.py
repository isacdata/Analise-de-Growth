import pandas as pd
from datetime import date, timedelta



"""

status:
1 - active
2 - cancelled
3 - deactivate

sub_start
sub_end

period_start
period_end

base:
sub_start <= period_start *1/2
sub_start <= period_start <= sub_end *3

new:
period_start <= First sub_start <= period_end

churned:
period_start <= sub_end <= period_end

ressurected:
if at least on but nothe the first sub_star is contained in [period_start, period_end]

A person can be present in more than one category

"""

#Function

def set_period(p):
    
    period_end = date(2022,10,31)
    period_start = period_end - timedelta(days = p-1)
    
    return (period_start, period_end)

def is_base(df, period_start, period_end):
    
    for i in range(len(df)):
        
        if df['status'][i] == 3:
            if df['sub_start'][i].date() <= period_start <= df['sub_end'][i].date():
                return (True, i)
        
        else:
            if df['sub_start'][i].date() <= period_start:
                return (True, i)
        
    return (False, None)


def is_new(df, period_start, period_end):
    
    if period_start <= df['sub_start'].min().date() <= period_end:
        return (True, 0)
    
    return (False, None)

def is_churned(df, period_start, period_end):
    
    for i in range(len(df)):
        
        if pd.isnull(df['sub_end'][i]):
            continue
        
        if period_start <= df['sub_end'][i].date() <= period_end:
            return (True, i)
        
    return (False, None)
    
    return(False, None)

def is_resurrected(df, period_start, period_end):
    
    for i in range(1, len(df)):
        
        if period_start <= df['sub_start'][i].date() <= period_end:
            return (True, i)
    
    return (False, None)

def generate_user_tags(df, period = 30, period_start = None, period_end = None):
    
    if period_start is None and period_end is None:
        period_start, period_end = set_period(period)
    
    if period_start is None:
        period_start = period_end - timedelta(days = period - 1)
    
    if period_end is None:
        period_end = period_start + timedelta(days = period - 1)
    
    
    
    r = []
    
    
    users = set(df['user_id'])
    
    for user_id in users:
        
        mask = (df['user_id'] == user_id)
        user = df[mask]
        user.reset_index(drop = True, inplace = True)
        
        
        test, index = is_base(user, period_start, period_end)
        if test:
            r.append([ user['user_id'][index], user['status'].iloc[-1], user['plan'][index], "Base" ])
        
        test, index = is_new(user, period_start, period_end)
        if test:
            r.append([ user['user_id'][index], user['status'].iloc[-1], user['plan'][index], "New" ])
        
        test, index = is_churned(user, period_start, period_end)
        if test:
            r.append([ user['user_id'][index], user['status'].iloc[-1], user['plan'][index], "Churned" ])
        
        test, index = is_resurrected(user, period_start, period_end)
        if test:
            r.append([ user['user_id'][index], user['status'].iloc[-1], user['plan'][index], "Resurrected" ])
    
    
    
    result = pd.DataFrame(data = r, columns = ["user_id", "current status", "plan", "tag"])
    result.sort_values(by = "user_id", inplace = True, ignore_index = True)
    
    
    return result
   
#Data Exploration

data = pd.read_csv(r"C:\Users\vieiri2\OneDrive - Boston Scientific\Curso Tableau\Growth Tableau\CSV's\Waterfall_subscriptions.csv")

print(data.head())

print(type(data['sub_start'][0]))

data['sub_start'] = pd.to_datetime(data['sub_start'])
data['sub_end'] = pd.to_datetime(data['sub_end'])

print(data.head())

#Test
test = generate_user_tags(data)
print(test.head())

#Data Export
result_last_30 = generate_user_tags(data, period = 30)
result_last_90 = generate_user_tags(data, period = 90)
result_last_365 = generate_user_tags(data, period = 365)

result_last_30.to_csv('Waterfall_subs_last_30.csv', index = False)
result_last_90.to_csv('Waterfall_subs_last_90.csv', index = False)
result_last_365.to_csv('Waterfall_subs_last_365.csv', index = False)
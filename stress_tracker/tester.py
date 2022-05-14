import datetime
import global_vars
import connector 

user_id = 2

db = connector.Database("test_config.ini")
db.connect_database()

activities = ["sleep", "study", "work", "social","hobby"]

program = "Computer Science"
degree = "Bachelor"

for a in activities:
    criterium = "(stats_degree='"+degree+"' AND stats_program='"+program+"' AND stats_bound = 0)"
    print(criterium)
    get_low = db.getColumnData("stats_"+a, "avg_stats",criterium)
    print(get_low)

def avg(values):
    total = sum(values)
    count = len(values)

    if total == 0:
        avg = 0
    else:
        avg = total/count
        
    return avg

avg_stats = db.getUserData("user",user_id)
print(avg_stats["user_program"][0])




'''
program = "Computer Science"
degree = "Master"


indices = [i for i,v in enumerate(avg_stats["stats_program"]) if v == program]
print(indices)

indices = [i for i in indices if avg_stats["stats_degree"][i] == degree]
print(indices)

'''

'''
lastrec_year = user_stats['stats_year'][-1]
lastrec_weeknr = user_stats['stats_weeknr'][-1]
print(lastrec_year,lastrec_weeknr)

if (year == lastrec_year) and (weeknr == lastrec_weeknr):
    give_feedback = False
else:
    give_feedback = True

print(give_feedback)





datetime.date(2010, 6, 16).isocalendar()[1]
'''

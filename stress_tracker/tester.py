import datetime
import global_vars
import connector 

import encryption

db = connector.Database("test_config.ini")
db.connect_database()



mc = db.connector.cursor()

mc.execute("SELECT stats_sleep,stats_work FROM user,stats WHERE (user.user_id = stats.stats_userid) AND user.user_program = 'tt'")
result = mc.fetchall()

print(result)

data = []

for record in result:
    data.append(record[0])
print(data)

'''
program = "Computer Science"
degree = "Bachelor"


criterium = "(user_degree='"+degree+"' AND user_program='"+program+"')"
userids = db.getColumnData("user_id", "user",criterium)
print(userids)

activities = ["sleep", "study", "work", "social","hobby"]


for a in activities:
    criterium = "(stats_degree='"+degree+"' AND stats_program='"+program+"' AND stats_bound = 0)"
    print(criterium)
    get_low = db.getColumnData("stats_"+a, "avg_stats",criterium)
    print(get_low)
'''



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

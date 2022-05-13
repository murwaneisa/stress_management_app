import datetime
import global_vars
import connector 

user_id = 1

db = connector.Database("test_config.ini")
db.connect_database()




avg_stats = db.getUserData(user_id,"avg_stats")
print(avg_stats)

program = "Computer Science"
degree = "Master"


indices = [i for i,v in enumerate(avg_stats["stats_program"]) if v == program]
print(indices)

indices = [i for i in indices if avg_stats["stats_degree"][i] == degree]
print(indices)



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

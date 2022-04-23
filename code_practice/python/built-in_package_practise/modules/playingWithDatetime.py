import datetime
import pytz


td=datetime.date.today() # current date
tdt=datetime.datetime.now() # current datetime
tt=datetime.datetime.now().time() #current time
tdtu=datetime.datetime.utcnow()
dt=datetime.date(2020,2,22) # date object
dtt=datetime.datetime(2020,2,22,22,10)  #datetime object
t=datetime.time(22,36,56,213245) #time object
dt.weekday() #gives the week day number of week (mon-sun (0-6))
dt.isoweekday() #gives the iso week day number of week (mon-sun (1-7))
td - datetime.timedelta(weeks=1) # gives the date 1 week from today
td - datetime.timedelta(days=1) # gives the date 1 day from today
(td - dt) # this will give you a time delta object containing number of days between two dates
(td - dt).days #  this will extract the 'days' attribute value from timedelta object

(td - dt).total_seconds() #this will extract the number of seconds between two dates
all_tz_set=pytz.all_timezones_set #this will return a lazy set object of all time zones
all_tz_list=pytz.all_timezones #this will return a lazy list object of all time zones
tz_vienna=pytz.timezone("Europe/Vienna") #timezone object using pytz - vienna
tz_india=pytz.timezone("Asia/Kolkata") #timezone object using pytz - India
tdt=tz_india.localize(tdt) # localize the datetime to given timezone so that is time zone aware
tdt.isoformat() # this will convert the date into ISO format YYYY-MM-DD HH:MM:SS.FFFFFF
datetime.datetime.strptime() #this will parse the string in to date time of given format
tdt.strftime() #this will format the given date into mentioned formatted string
print(tdt)
print(tdtu)
print(tdt.astimezone(tz_vienna))


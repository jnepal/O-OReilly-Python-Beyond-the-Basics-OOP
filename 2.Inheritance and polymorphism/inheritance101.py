class Date(object):
    def get_date(self):
        return '2014-10-23'

class Time(Date):
    def get_time(self):
        return '08:13:07'

date = Date()
print(date.get_date())

time = Time()
print(time.get_time())
print(time.get_date())
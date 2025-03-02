import random
from datetime import datetime, timedelta
def random_date(start,end):
    delta = end - start
    random_seconds = random.randint(8,int(delta.total_seconds()))
    random_datetime = start + timedelta(seconds=random_seconds)
    return random_datetime
start_date = datetime.strptime('2023-01-01 00:00:00','%Y-%m-%d %H:%M:%S')
end_date = datetime.strptime('2023-12-31 23:59:59','%Y-%m-%d %H:%M:%S')

random_datetime = random_date(start_date, end_date)
print("Random Date and Time: ",random_datetime)


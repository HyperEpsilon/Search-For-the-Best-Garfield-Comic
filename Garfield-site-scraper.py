import datetime, urllib.request

startdate = datetime.date(1985,1,1)

date = startdate
for _ in range(5):
    if date.isoweekday() == 7:
        continue
    
    day = date.day
    month = date.month
    year = date.year
    
    print("{:04d}-{:02d}-{:02d}".format(year, month, day))
    urllib.request.urlretrieve("https://d1ejxu6vysztl5.cloudfront.net/comics/garfield/1985/{:04d}-{:02d}-{:02d}.gif".format(year, month, day), "comics/{:04d}-{:02d}-{:02d}.gif".format(year, month, day)) 
    
    date += datetime.timedelta(days=1)
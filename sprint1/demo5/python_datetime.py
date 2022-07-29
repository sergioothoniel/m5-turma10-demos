# Código executado na shell do Python durante a demo
from datetime import datetime as dt

dt.now()

x_date = dt.now()
x_date
type(x_date)

x_date.hour
x_date.year
x_date.day

y_date = dt.now()
y_date
y_date - x_date

x_date.timestamp()

x_date.strftime("%a %d %b %Y")

x_date.strftime("%a %d %b %y")


date_str = '03-03-1993'
obj_dt = dt.strptime(date_str, "%d-%m-%Y")
obj_dt
type(obj_dt)

date_string = '12-25-2018'
format = "%Y-%m-d"
try:
  datetime.datetime.strptime(date_string, format)
  print("This is the correct date string format.")
except ValueError:
  print("This is the incorrect date string format. It should be YYYY-MM-DD")
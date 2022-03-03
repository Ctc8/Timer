import time

while True:
  print("--Timer--")
  print("1. Set Interval")
  print("2. Set Time" )
  print("3. Start Time")

  menuChoice = input("Select Option: ")


  if menuChoice == "1.":
    print("Enter a time interval:")
    interval = input()
    interval = int(interval)

  elif menuChoice == "2.":
    print("Set time: ")
    time1 = input("Type in time:")
    time1 = int(time1)

  elif menuChoice == "3.":
    x = time1
    x = int(x)

    while x > 0:
      print(x)
      time.sleep(interval)
      x = x - interval

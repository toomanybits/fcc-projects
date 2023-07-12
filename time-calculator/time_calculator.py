def add_time(start, duration, startday=None):

  # make start time accessable
  stime = start.split()
  time = stime[0].split(":")
  hr = time[0]
  min = time[1]
  meri = stime[1]

  # convert time accorfing to 24 hour norms for addition
  if meri == "PM":
    hr = int(hr) + 12

  # make duration accessable
  atime = duration.split(":")
  ahr = atime[0]
  amin = atime[1]

  #   add time
  fhr = int(ahr) + int(hr)
  fmin = int(amin) + int(min)
  fmeri = "AM"

  # format min
  if fmin >= 60:
    fhr += 1
    fmin = fmin - 60

  # format hr
  message = ""
  day = 0
  if fhr > 24:
    day = fhr / 24
    day = int(day)
    fhr = fhr % 24
    if day == 1:
      message = " (next day)"
    else:
      message = f" ({day} days later)"

  # fomatting hr according to 12 hours norm
  if fhr >= 12:
    fmeri = "PM"
    fhr -= 12

  # convert zero to twelve
  if fhr == 0:
    fhr = 12

  days = [
    "sunday",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
  ]

  # print message according to instrcutions
  if startday == None:
    new_time = f"{fhr}:{fmin:02d} {fmeri}{message}"
  else:
    index = days.index(str(startday).lower())
    index += int(day)
    index = index % 7
    new_time = f"{fhr}:{fmin:02d} {fmeri}, {days[index].capitalize()}{message}"

  return new_time

import datetime
import math

def hour_of_year(year, month, day_of_month, hour):
    tiempo = datetime.datetime(year, month, day_of_month, hour, 0, 0)
    ene_first = datetime.datetime(year, 1, 1, 0, 0, 0)
    return (tiempo-ene_first).total_seconds()

def time_x(year, month, day_of_month, hour):
    hour_year_s = hour_of_year(year, month, day_of_month, hour)
    total_hours = hour_of_year(year, 12, 31, 23)
    return (math.cos(2*math.pi*hour_year_s/total_hours)+1)/2

def time_y(year, month, day_of_month, hour):
    hour_year_s = hour_of_year(year, month, day_of_month, hour)
    total_hours = hour_of_year(year, 12, 31, 23)
    return (math.sin(2*math.pi*hour_year_s/total_hours)+1)/2

def time_day_x (hour):
    return (math.cos(2*math.pi*hour/24)+1)/2

def time_day_y (hour):
    return (math.sin(2*math.pi*hour/24)+1)/2

def is_night(month, hour):
    try:
        if month == 1:
            if hour >= 7 and hour <=16:
                return 0
            else:
                return 1
        if month == 2:
            if hour >= 6 and hour <=17:
                return 0
            else:
                return 1
        if month == 3:
            if hour >= 7 and hour <=18:
                return 0
            else:
                return 1
        if month == 4:
            if hour >= 6 and hour <=19:
                return 0
            else:
                return 1
        if month == 5:
            if hour >= 5 and hour <=20:
                return 0
            else:
                return 1
        if month == 6:
            if hour >= 5 and hour <=20:
                return 0
            else:
                return 1
        if month == 7:
            if hour >= 5 and hour <=20:
                return 0
            else:
                return 1
        if month == 8:
            if hour >= 5 and hour <=19:
                return 0
            else:
                return 1
        if month == 9:
            if hour >= 6 and hour <=18:
                return 0
            else:
                return 1
        if month == 10:
            if hour >= 7 and hour <=17:
                return 0
            else:
                return 1
        if month == 11:
            if hour >=6 and hour <=16:
                return 0
            else:
                return 1
        if month == 12:
            if hour >= 7 and hour <=16:
                return 0
            else:
                return 1
    except:
        return 0
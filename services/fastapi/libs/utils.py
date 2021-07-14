from datetime import datetime


def create_datetime_name():
    now = datetime.now()
    
    str_date = str(now).split(".")[0]

    return str_date

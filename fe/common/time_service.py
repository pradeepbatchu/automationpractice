from datetime import datetime, timedelta


def create_start_time(start_time=None):
    # Date and time format should be given as: 2018-10-31T15:30:00

    if start_time:
        return start_time

    st_date = datetime.today().strftime('%Y-%m-%d')
    time_plus_seconds = datetime.now() + timedelta(seconds=30)
    start_date_time = st_date + 'T' + time_plus_seconds.strftime('%X')
    print(start_date_time)

    return start_date_time

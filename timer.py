from datetime import datetime, timedelta
import time

def get_nearest_multiple_of_3():
    current_minute = datetime.utcnow().minute
    nearest_multiple = (current_minute // 3) * 3
    return nearest_multiple

def utc_countdown_nearest_multiple_of_3(duration_minutes):
    nearest_multiple = get_nearest_multiple_of_3()
    target_time = datetime.utcnow().replace(second=0, microsecond=0, minute=nearest_multiple) + timedelta(minutes=duration_minutes)
    max_duration = datetime.utcnow() + timedelta(minutes=60)  # Maximum duration - 60 minutes from current time

    if duration_minutes > 60:
        duration_minutes = 60  # Limit the countdown to a maximum of 60 minutes

    while datetime.utcnow() < target_time and datetime.utcnow() < max_duration:
        remaining_time = min(target_time, max_duration) - datetime.utcnow()
        remaining_seconds = remaining_time.total_seconds()
        if remaining_seconds > 0:
            minutes, seconds = divmod(int(remaining_seconds), 60)
            print("{:02d}:{:02d}".format(minutes, seconds), end='\r')
            time.sleep(1)

    print("Countdown complete!")

# Example: Start a 15-minute countdown within the 60-minute boundary
utc_countdown_nearest_multiple_of_3(15)

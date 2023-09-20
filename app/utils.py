from datetime import timezone
import datetime

def get_utc_time():
    current_time = datetime.datetime.now(timezone.utc)
    utc_time = current_time.replace(tzinfo=timezone.utc)
    formatted_utc_time = utc_time.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_utc_time
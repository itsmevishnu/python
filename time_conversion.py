from datetime import datetime
import pytz

def generate_utc_time():
    utc = pytz.timezone("UTC")
    now = utc.localize(datetime.utcnow())
    return now

def generate_local_time(timezone, time):
    timezone = pytz.timezone(timezone)
    local_time = time.astimezone(timezone)
    return local_time

def main():
    IST_ZONE = "Asia/Kolkata"
    now = generate_utc_time()
    local_time = generate_local_time(IST_ZONE, now)
    print(f"UTC time = {now}\nLocal time = {local_time}")

if __name__ == '__main__':
    main()

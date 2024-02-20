from datetime import datetime, timedelta

import requests



def send_push_notification(pushkey, text):
    url = f"https://api2.pushdeer.com/message/push?pushkey={pushkey}&text={text}"
    response = requests.get(url)
    if response.status_code == 200:
        print("Push notification sent successfully.")
    else:
        print("Failed to send push notification.")


from datetime import datetime, timedelta

import requests



def send_push_notification(pushkey, text):
    url = f"https://api2.pushdeer.com/message/push?pushkey={pushkey}&text={text}"
    response = requests.get(url)
    if response.status_code == 200:
        print("Push notification sent successfully.")
    else:
        print("Failed to send push notification.")


def monitor_live_status(room_id, pushkey, text):
    global previous_status  # Access the global variable

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
    url = f"https://api.live.bilibili.com/room/v1/Room/get_info?room_id={room_id}"

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        live_status = data["data"]["live_status"]
        live_time = data["data"]["live_time"]
        if live_status == 1:
            # Convert live_time to datetime object
            live_time = datetime.strptime(live_time, '%Y-%m-%d %H:%M:%S')

            # Get current time
            current_time = datetime.now()

            # Calculate the difference between current time and live time
            time_difference = current_time - live_time

            # If the live status is 1 and the time difference is less than or equal to one minute, send a push notification
            if time_difference <= timedelta(minutes=1):
                send_push_notification(pushkey, text)
                print("开播了")
            elif time_difference > timedelta(minutes=1):
                print("已开播")
        else:
            print("未开播")
    else:
        print("Failed to fetch live status.")


if __name__ == "__main__":
    room_id = 123456  # 替换为你要监控的直播间ID
    pushkey = "your_pushkey"  # 替换为你的pushkey
    text = "xxx开播了！"
    monitor_live_status(room_id, pushkey, text)

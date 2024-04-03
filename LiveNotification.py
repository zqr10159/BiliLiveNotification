import time
import requests

previous_status = 0


def send_push_notification(pushkey, text):
    url = f"https://api2.pushdeer.com/message/push?pushkey={pushkey}&text={text}"
    response = requests.get(url)
    if response.status_code == 200:
        print("Push notification sent successfully.")
    else:
        print("Failed to send push notification.")


def monitor_live_status(room_id, pushkey, text):
    global previous_status
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
    url = f"https://api.live.bilibili.com/room/v1/Room/get_info?room_id={room_id}"

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        live_status = data["data"]["live_status"]

        if live_status == 1 and previous_status == 0:
            send_push_notification(pushkey, text)
            print("开播了")
        else:
            print("未开播")
        previous_status = live_status
    else:
        print("Failed to fetch live status.")


if __name__ == "__main__":
    room_id = 123456  # 替换为你要监控的直播间ID
    pushkey = "your_pushkey"  # 替换为你的pushkey
    text = "xxx开播了！"
    while True:
        monitor_live_status(room_id, pushkey, text)
        time.sleep(10) # 每10秒检查一次直播状态
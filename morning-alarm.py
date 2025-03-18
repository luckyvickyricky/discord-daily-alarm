# alarm.py
from datetime import datetime
from zoneinfo import ZoneInfo  # Python 3.9 이상에서 사용 가능
import os
import requests


def get_message():
    # 한국 시간 기준 현재 시간 구하기
    now = datetime.now(ZoneInfo("Asia/Seoul"))
    # weekday()는 월요일(0)부터 일요일(6)까지 반환
    if now.weekday() < 5:
        # 평일: 월~금
        return "좋은 아침입니다! 아침 8시 40분 데일리스크럼 이전까지 기상인증사진(침대에서 벗어나 공부가 준비된 사진)을 올려주세요."
    else:
        # 주말: 토, 일
        return "좋은 주말입니다! 기상인증사진을 선택적으로 인증해주세요."


def send_discord_message(message, webhook_url):
    payload = {"content": message}
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 204:
        print("메시지가 성공적으로 전송되었습니다.")
    else:
        print(f"메시지 전송 실패: {response.status_code} - {response.text}")


if __name__ == "__main__":
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
    if not webhook_url:
        raise ValueError("DISCORD_WEBHOOK_URL 환경 변수가 설정되지 않았습니다.")
    message = get_message()
    send_discord_message(message, webhook_url)

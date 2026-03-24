from playwright.sync_api import sync_playwright
import requests
import os

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def send_message(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})


def check_price():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Alaska 搜尋頁
        url = "https://www.alaskaair.com/"

        page.goto(url)

        page.wait_for_timeout(8000)

        # 這裡只是測試抓價格
        title = page.title()

        send_message(f"Alaska watcher 執行成功\n頁面: {title}")

        browser.close()


check_price()

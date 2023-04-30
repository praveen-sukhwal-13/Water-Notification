import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Drink Water",
            message = "Water is essential...",
            timeout = 2
        )
        time.sleep(60*60)
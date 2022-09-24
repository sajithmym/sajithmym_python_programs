import time
from plyer import notification

while True:
    notification.notify(
        title = 'Sajithmym',
        message = 'Welcome to My Notification application',
        app_icon = 'j.ico',
        timeout = 10
    )
    time.sleep(10)
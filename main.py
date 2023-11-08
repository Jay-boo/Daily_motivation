import notify2
import logging

def get_citation()-> str:
    return ""


if __name__ == "__main__":
    notify2.init("")

    citation=get_citation()
    notification = notify2.Notification(
        "Daily Motivation",
                         citation,
"notification-audio-next"
                        )
    notification.show()

    print("Runnning Cron Job")
    logging.log(level=1,
                msg="Hello from logging my dear")
    # pass

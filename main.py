import notify2
import logging

def get_citation()-> str:
    return "Hello world"


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    logging.info("Start")
    notify2.init("")

    citation=get_citation()
    notification = notify2.Notification(
        "Daily Motivation",
                         citation,
"notification-audio-next"
                        )
    notification.show()

    logging.info("Runnning Cron Job")
    logging.log(level=1,
                msg="Hello from logging my dear")
    # pass

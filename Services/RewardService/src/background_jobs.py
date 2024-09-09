from flask_apscheduler import APScheduler
from src.models.reward_model import Reward

# set configuration values
class BackgroundConfig:
    SCHEDULER_API_ENABLED = True

scheduler = APScheduler()

@scheduler.task('interval', id='add_monthly_points', seconds=10, misfire_grace_time=900)
def add_monthly_points_job():
    Reward.add_monthly_points()
    print('Monthly point added')

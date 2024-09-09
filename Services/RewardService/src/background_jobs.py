from flask_apscheduler import APScheduler
from src.models.reward_model import Reward

# set configuration values
class BackgroundConfig:
    SCHEDULER_API_ENABLED = True

scheduler = APScheduler()

# Test background job run every 10 seconds
@scheduler.task('interval', id='test_add_monthly_points', seconds=10, misfire_grace_time=900)
def test_add_monthly_points_job():
    print('Monthly point added')

# background job run every last day of month
@scheduler.task('interval', id='add_monthly_points', seconds=2592000, misfire_grace_time=900)
def add_monthly_points_job():
    Reward.add_monthly_points()
    print('Monthly point added')

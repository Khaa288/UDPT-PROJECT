from src.models import db
from dataclasses import dataclass
from sqlalchemy import String,DateTime, desc
from src.models import db
from sqlalchemy.orm import Mapped, mapped_column
import datetime

@dataclass
class Activity (db.Model):
    __tablename__ = "Activity"
    ActivityId: Mapped[int] = mapped_column(primary_key=True)
    ActivityName: Mapped[str] = mapped_column(String(128))
    StartTime: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True))
    EndTime: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True))

    ## Manager Account
    def get_all_Activity():
        activities = db.session.query(Activity).order_by(desc(Activity.EndTime)).all()
        return activities
    def get_activity_byId(activity_id):
        return db.get_or_404(Activity,activity_id)
    def create_Activity(activity_name: str, start_time: datetime.datetime, end_time: datetime.datetime):
        newActivity = Activity(
            ActivityName= activity_name,
            StartTime=start_time,
            EndTime=end_time
        )
        db.session.add(newActivity)
        db.session.commit()
        return newActivity
    def update_Activity(activity_id, updated_activity):
        activity = db.get_or_404(Activity,activity_id)
        activity.ActivityName = updated_activity["ActivityName"]
        activity.StartTime = updated_activity["StartTime"]
        activity.EndTime = updated_activity["EndTime"]
        db.session.commit()
        return 1
    ## Employee Account
    
    
    
    





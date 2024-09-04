from src.models.activity_model import Activity
from src.models import db
from dataclasses import dataclass
from sqlalchemy import String,DateTime,ForeignKey
from src.models import db
from sqlalchemy.orm import Mapped, mapped_column
import datetime

@dataclass
class Participant (db.Model):
    __tablename__ = "Participant"
    ActivityId: Mapped[int] = mapped_column()
    ActivityName: Mapped[str] = mapped_column(String(128))
    EndDate: Mapped[datetime.datetime] = mapped_column()
    EmployeeId: Mapped[int] = mapped_column()
    TotalKm: Mapped[int] = mapped_column()
    TotalMinute: Mapped[int] = mapped_column()
    StravaId: Mapped[int] = mapped_column()  # From User's Strava App
    Participant_Id: Mapped[int] = mapped_column(primary_key=True) #dummy primarykey

    ## Manager Account
    def get_Participant_by_ActivityId(activity_id):
       participants = db.session.query(Participant).filter(Participant.ActivityId == activity_id)
       return participants.all()
       
    ## Employee Account
    def get_all_ParticiPant():
        participants = db.session.query(Participant).all()
        return participants
    def get_Participant_by_EmployeeId(employee_id):
        participants = db.session.query(Participant).filter(Participant.EmployeeId == employee_id)
        return participants.all()
    def participate_Activity(activity_id: int, activity_name: str, end_date: datetime.datetime,employee_id: int, strava_id: int):
        newparticipant = Participant(
            ActivityName=activity_name,
            EndDate=end_date,
            EmployeeId=employee_id,
            StravaId= strava_id,
            TotalKm= 0,
            TotalMinute=0
        )
        db.session.add(newparticipant)
        db.session.commit()
        return newparticipant
    

    
    
    







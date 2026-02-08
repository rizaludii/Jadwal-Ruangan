from database import engine, SessionLocal
from models import Base
from scheduling_service import SchedulingService
from observer import StudentObserver, LecturerObserver, AdminObserver

def init_db():
    Base.metadata.create_all(bind=engine)
    print("Database created")

if __name__ == "__main__":
    init_db()
    db = SessionLocal()
    service = SchedulingService(db)
    service.subject.attach(StudentObserver())
    service.subject.attach(LecturerObserver())
    service.subject.attach(AdminObserver())
    print(service.detect_schedule_conflict())

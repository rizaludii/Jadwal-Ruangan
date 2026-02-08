from observer import ScheduleSubject
from models import Schedule

def time_overlap(s1, s2):
    return (s1.jam_mulai < s2.jam_selesai) and (s2.jam_mulai < s1.jam_selesai)

class SchedulingService:
    def __init__(self, db):
        self.db = db
        self.subject = ScheduleSubject()

    def detect_schedule_conflict(self):
        schedules = self.db.query(Schedule).all()
        conflicts = []
        for i in range(len(schedules)):
            for j in range(i+1, len(schedules)):
                s1, s2 = schedules[i], schedules[j]
                if s1.hari == s2.hari and time_overlap(s1, s2):
                    if s1.ruangan == s2.ruangan:
                        conflicts.append({"type":"room_conflict","ids":[s1.id,s2.id]})
                    if s1.dosen == s2.dosen:
                        conflicts.append({"type":"lecturer_conflict","ids":[s1.id,s2.id]})
        return conflicts

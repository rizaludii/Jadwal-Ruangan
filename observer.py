class Observer:
    def update(self, event):
        pass

class StudentObserver(Observer):
    def update(self, event):
        print(f"[EMAIL] Mahasiswa diberitahu: {event}")

class LecturerObserver(Observer):
    def update(self, event):
        print(f"[SMS] Dosen diberitahu: {event}")

class AdminObserver(Observer):
    def update(self, event):
        print(f"[ADMIN] Update diterima: {event}")

class ScheduleSubject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, event_type, data):
        for obs in self.observers:
            obs.update({"event": event_type, "data": data})

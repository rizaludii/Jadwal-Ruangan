from sqlalchemy import Column, Integer, String, Time, ForeignKey
from database import Base

class Schedule(Base):
    __tablename__ = "schedules"
    id = Column(Integer, primary_key=True)
    mata_kuliah = Column(String)
    hari = Column(String)
    jam_mulai = Column(Time)
    jam_selesai = Column(Time)
    ruangan = Column(String)
    kapasitas_ruangan = Column(Integer)
    dosen = Column(String)
    jumlah_mahasiswa = Column(Integer)

class KRS(Base):
    __tablename__ = "krs"
    id = Column(Integer, primary_key=True)
    mahasiswa = Column(String)
    schedule_id = Column(Integer, ForeignKey("schedules.id"))
    status = Column(String, default="VALID")

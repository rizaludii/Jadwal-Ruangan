from models import KRS

def invalidate_krs(db, schedule_id):
    krs_list = db.query(KRS).filter(KRS.schedule_id == schedule_id).all()
    for krs in krs_list:
        krs.status = "INVALID"
    db.commit()

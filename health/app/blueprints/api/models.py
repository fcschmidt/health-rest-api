from health.app.ext.db import db


class Prescription(db.Model):

    __tablename__ = "prescriptions"

    id = db.Column(db.Integer, primary_key=True)
    clinic_id = db.Column(db.Integer, nullable=True)
    physician_id = db.Column(db.Integer, nullable=True)
    patient_id = db.Column(db.Integer, nullable=True)
    text = db.Column(db.String(100), nullable=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'data(id={self.id}, clinic_id={self.clinic_id}, ' \
            f'physician_id={self.physician_id}, patient_id={self.patient_id}, text={self.text})'

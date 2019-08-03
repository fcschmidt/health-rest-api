import pytest
from health.app.blueprints.api.models import Prescription


@pytest.mark.usefixtures('session')
class TestPrescriptionsModel:

    @staticmethod
    def create_prescription():
        prescription = Prescription(
            clinic_id=1,
            physician_id=1,
            patient_id=1,
            text="Dipirona 1x ao dia"
        )
        prescription.save()
        return prescription

    def test_create_prescription(self):
        prescription = self.create_prescription()
        assert prescription.id == 1

    def test_get_prescription(self):
        prescription = self.create_prescription()
        assert prescription.id == 1

        get_prescription = prescription.get_prescription(1)
        assert prescription == get_prescription

    def test_delete_prescription(self):
        prescription = self.create_prescription()
        prescription.delete()
        get_prescription = prescription.get_prescription(1)
        assert get_prescription is None

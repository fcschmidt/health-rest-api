import pytest
from health.app.blueprints.api.models import Prescription


@pytest.mark.usefixtures('session')
class TestPrescriptionsModel:

    def test_create_prescription(self):
        prescription = Prescription(
            clinic_id=1,
            physician_id=1,
            patient_id=1,
            text="Dipirona 1x ao dia"
        )
        prescription.save()
        prescription_id = prescription.id
        assert prescription_id == 1

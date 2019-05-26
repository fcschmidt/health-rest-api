from marshmallow import fields, Schema


class PrescriptionsSchemas(Schema):
    id = fields.Integer(dump_only=True)
    clinic_id = fields.Integer(dump_only=True)
    physician_id = fields.Integer(dump_only=True)
    patient_id = fields.Integer(dump_only=True)
    text = fields.String(dump_only=True)

    class Meta:
        strict = True

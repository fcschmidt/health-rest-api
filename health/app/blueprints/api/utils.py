from health.app.blueprints.api.schemas import PrescriptionsSchemas

prescriptions_schema = PrescriptionsSchemas()


def serializer(content):
    serialized = prescriptions_schema.dump(content, many=True).data
    return serialized

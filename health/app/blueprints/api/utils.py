from health.app.blueprints.api.schemas import PrescriptionsSchemas

prescriptions_schema = PrescriptionsSchemas()


def serializer(content, state):
    serialized = prescriptions_schema.dump(content, many=state).data
    return serialized

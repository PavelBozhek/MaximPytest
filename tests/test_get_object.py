from api.get_object import GetObject


def test_get_valid_object(service):
    object_id = 437133
    response = GetObject(service, object_id, code=200).request()


def test_should_return_400(service):
    object_id = "abc"
    response = GetObject(service, object_id, code=400).request()

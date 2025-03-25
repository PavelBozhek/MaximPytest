from api.get_object import GetObject


def test_get_valid_object(service):
    object_id = 437133
    print(service.url)
    response = GetObject(service, object_id).request()
    print(response)

    assert response.status_code == 200


def test_should_return_400(service):
    object_id = "abc"
    response = GetObject(service, object_id).request()
    assert response.status_code == 400

from api.collection_objects_v1 import CollectionObjectsV1


def test_get_collection_object(service):
    response = CollectionObjectsV1(service, code=200).request()
    assert response.total == len(response.object_ids)


def test_should_return_400(service):
    params = {"metadataDate": "Van Gogh"}
    CollectionObjectsV1(service, code=400, params=params).request()

import json


def test_get_all_members(client):
    response = client.get('/members/')
    assert response.status_code == 200


def test_create_member(client):
    data = {
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    }
    response = client.post('/members/', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 201
    assert response.json['name'] == 'John Doe'


def test_get_member_by_id(client):
    response = client.get('/members/1')
    assert response.status_code in [200, 404]


def test_update_member(client):
    data = {'name': 'Updated Name'}
    response = client.put('/members/1', data=json.dumps(data), content_type='application/json')
    assert response.status_code in [200, 404]


def test_delete_member(client):
    response = client.delete('/members/1')
    assert response.status_code in [200, 404]


def test_get_member_by_email(client):
    response = client.get('/members/email/john.doe@example.com')
    assert response.status_code in [200, 404]

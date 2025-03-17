import json


def test_get_all_books(client):
    response = client.get('/books/')
    assert response.status_code == 200


def test_create_book(client):
    data = {
        'title': 'Test Book',
        'author': 'Test Author'
    }
    response = client.post('/books/', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 201
    assert response.json['title'] == 'Test Book'


def test_get_book_by_id(client):
    response = client.get('/books/1')
    assert response.status_code in [200, 404]


def test_update_book(client):
    data = {'title': 'Updated Book'}
    response = client.patch('/books/1', data=json.dumps(data), content_type='application/json')
    assert response.status_code in [200, 404]


def test_delete_book(client):
    response = client.delete('/books/1')
    assert response.status_code in [200, 404]


def test_borrow_book(client):
    response = client.post('/books/borrow/1/2')
    assert response.status_code in [200, 400, 404]


def test_return_book(client):
    response = client.put('/books/return/1')
    assert response.status_code in [200, 400, 404]

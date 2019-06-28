import json

headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}


def test_homepage(test_client):
    response = test_client.get('/')
    assert response.status_code == 200


def test_get_book(test_client):
    response = test_client.get('/api/books/4')
    print(response.data)
    assert response.status_code == 200


def test_post_book(test_client):
    '''Test if isbn fail'''
    data = dict(
        title="Book test title sample",
        isbn="ABS23",
        year=1996,
        authorId=1,
        status="new",
        created="2015-5-10T10:55:43",
        updated="2015-5-10T10:56:43"
    )
    response = test_client.post('/api/books/', headers=headers, data=json.dumps(data))
    assert response.status_code == 400


def test_post_book1(test_client):
    '''Test if isbn ok'''

    data = dict(
        title="Book test title sample",
        isbn="978-1234-567890",
        year=1996,
        authorId=1,
        status="new",
        created="2015-5-10T10:55:43",
        updated="2015-5-10T10:56:43"
    )

    response = test_client.post('/api/books/', headers=headers, data=json.dumps(data))
    assert response.status_code == 201


def test_delete_book(test_client):
    book = test_client.get('/api/books/isbn/978-1234-567890')

    url = '/api/books/' + str(book.json['id'])
    response = test_client.delete(url)
    assert response.status_code == 204


def test_post_book2(test_client):
    '''Test if wrong year '''

    data = dict(
        title="Book test title sample",
        isbn="AxcxzsdgfdBS",
        year=2099,
        authorId=1,
        status="new",
        created="2015-5-10T10:55:43",
        updated="2015-5-10T10:56:43"
    )

    response = test_client.post('/api/books/', headers=headers, data=json.dumps(data))
    assert response.status_code == 400


def test_post_book3(test_client):
    '''Test if wrong isbn'''

    data = dict(
        title="Book test title sample",
        isbn="Axdf",
        year=2019,
        authorId=1,
        status="new",
        created="2015-5-10T10:55:43",
        updated="2015-5-10T10:56:43"
    )

    response = test_client.post('/api/books/', headers=headers, data=json.dumps(data))
    assert response.status_code == 400


def test_post_author(test_client):
    '''Test if wrong phone author'''

    data = dict(
        firstName="Book test title sample",
        lastName="Axdf",
        email="truong@gmail.com",
        phone="4534se",
        address="new",
        status="active",
        created="2015-5-10T10:55:43",
        updated="2015-5-10T10:56:43"
    )

    response = test_client.post('/api/authors/', headers=headers, data=json.dumps(data))
    assert response.status_code == 400


def test_post_author1(test_client):
    '''Test if wrong email author'''

    data = dict(
        firstName="Book test title sample",
        lastName="Axdf",
        email="truong@gmail",
        phone="4534234",
        address="new",
        status="active",
        created="2015-5-10T10:55:43",
        updated="2015-5-10T10:56:43"
    )

    response = test_client.post('/api/authors/', headers=headers, data=json.dumps(data))
    assert response.status_code == 400


def test_post_author2(test_client):
    '''Test if wrong email author'''

    data = dict(
        firstName="Book test title sample",
        lastName="Axdf",
        email="agmail",
        phone="4534234",
        address="new",
        status="active",
        created="2015-5-10T10:55:43",
        updated="2015-5-   "
                "10T10:56:43"
    )

    response = test_client.post('/api/authors/', headers=headers, data=json.dumps(data))
    assert response.status_code == 400

import pytest
from base_task import create_app
from base_task.models import *

@pytest.fixture(scope='module')
def test_client():
    testApp = create_app()
    testApp.config['BCRYPT_LOG_ROUNDS'] = 4
    testApp.config['TESTING'] = True
    testApp.config['WTF_CSRF_ENABLED'] = False

    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = testApp.test_client()

    # Establish an application context before running the tests.
    ctx = testApp.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()


@pytest.fixture(scope='module')
def init_database():
    # Create the database and the database table
    db.create_all()

    # Insert sample data
    book1 = Books(
        title="Sample book",
        isbn="SDSF",
        year=1997,
        authorId=1,
        status="new",
        created="2015-5-10 10:55:43",
        updated="2015-5-10T10:55:43"
    )

    author1 = Authors(
        firstName="Author",
        lastName="Sample",
        email="sample@gmail.com",
        phone="23423534",
        address="HCM",
        status="active",
        created="2015-5-10 10:55:43",
        updated="2015-5-10 10:55:43"
    )
    db.session.add(book1)
    db.session.add(author1)

    # Commit the changes for the users
    db.session.commit()

    yield db  # this is where the testing happens!

    db.drop_all()
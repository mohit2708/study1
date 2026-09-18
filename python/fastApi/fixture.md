### 🎯**What is Fixture?**
* A fixture in pytest is a reusable setup and teardown mechanism that prepares the required resources for a test and cleans them up after the test execution.
* FastAPI में fixtures का उपयोग commonly database connections, TestClient creation, test data setup, and dependency overrides के लिए किया जाता है।
* Fixture का उपयोग test data, database connection, authentication, object creation, setup/cleanup आदि को बार-बार लिखने से बचाने के लिए किया जाता है।

#### Example
* Without Fixture
```python
# अगर 50 test cases हैं तो हर जगह database setup करना पड़ेगा।
def test_get_user():
    db = SessionLocal()
    
    user = User(name="Mohit")
    db.add(user)
    db.commit()

    response = client.get("/users/1")

    assert response.status_code == 200
```

* With Fixture
```python
import pytest
from app.database import SessionLocal

@pytest.fixture
def db():
    db = SessionLocal()
    yield db
    db.close()

# अब test में use करो:
def test_get_user(db):
    response = client.get("/users/1")
    
    assert response.status_code == 200
```
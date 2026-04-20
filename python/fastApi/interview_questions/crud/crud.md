### Database > schemas > user.py
#### Create email validation
* insatll package for **duplicate email** exist
```python
pip install pydantic[email]
```

```python
# Database > schemas > user.py
from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=255, description="The first name of the user")
    last_name: str = Field(..., min_length=1, max_length=255, description="The last name of the user")
    email: EmailStr = Field(..., description="The email address of the user")
    password: str = Field(..., min_length=1, description="The password of the user")
```



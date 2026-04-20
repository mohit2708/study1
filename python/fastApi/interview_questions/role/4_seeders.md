### Create seeder file
- databse/seeders/role_seeder.py
- databse/seeders/__init__.py
```python
from sqlalchemy.orm import Session
from models.role import Role


def seed_roles(db: Session):
    roles = [
        {
            "name": "admin",
            "slug": "admin"
        },
        {
            "name": "customer",
            "slug": "customer"
        },
        {
            "name": "student",
            "slug": "student"
        },
        {
            "name": "m",
            "slug": "m"
        },
    ]

    for r in roles:
        role = db.query(Role).filter(Role.slug == r["slug"]).first()
        if not role:
            db.add(Role(name=r["name"], slug=r["slug"]))

    # when name only
    # roles = ["admin", "customer", "student"]

    # for role_name in roles:
    #     role = db.query(Role).filter(Role.name == role_name).first()
    #     if not role:
    #         db.add(Role(name=role_name))

    db.commit()


```
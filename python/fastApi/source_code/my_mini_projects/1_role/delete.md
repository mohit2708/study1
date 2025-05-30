### Delete Role data by id
```python
@router.delete("/role/{role_id}/delete")
def delete_role_handler(role_id: int, db: Session = Depends(get_db)):
    db_role = db.query(Role).filter(Role.id == role_id).first()
    if not db_role:
        return JSONResponse(
            content={
                "status": False,
                "code": 404,
                "message": "Role id does not exist!",
            },
            status_code=404
        )
    # Delete the role
    db.delete(db_role)
    db.commit()
    return JSONResponse(
        content={
            "status": True,
            "code": 200,
            "message": "Role has been deleted successfully!",
        },
        status_code=200
    )
```


### Extra code
```python
'''
Delete role
role id does not exist
'''
@router.delete("/role/{role_id}/delete", response_model=RoleDelete)
def delete_role_handler(role_id: int, db: Session = Depends(get_db)):
    deleted_role = delete_role(db, role_id)
    if not deleted_role:
        return JSONResponse(
                content={
                    "status": False,
                    "code": 404,
                    "message": "Role id does not exist!",
                },
                status_code=404
            )
    return deleted_role

def delete_role(db: Session, role_id: int) -> RoleDelete:
    db_role = db.query(Role).filter(Role.id == role_id).first()
    if db_role:
        deleted_role = RoleDelete(**db_role.__dict__)
        db.delete(db_role)
        db.commit()
        return JSONResponse(
            content={
                "status": True,
                "code": 200,
                "message": "Role has been Delete successfully!",
            },
            status_code=200
        )
        # return deleted_role
    return None
```
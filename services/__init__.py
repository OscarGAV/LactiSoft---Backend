from typing import Any, Generic, List, Optional, Type, TypeVar
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from pydantic import BaseModel

from core.database import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, db: Session, pk: Any) -> ModelType:
        obj = db.query(self.model).filter(
            list(self.model.__table__.primary_key.columns)[0] == pk
        ).first()
        if not obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"{self.model.__tablename__} con id {pk} no encontrado",
            )
        return obj

    def get_all(self, db: Session, skip: int = 0, limit: int = 100) -> List[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, obj_in: CreateSchemaType) -> ModelType:
        data = obj_in.model_dump()
        db_obj = self.model(**data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, pk: Any, obj_in: UpdateSchemaType) -> ModelType:
        db_obj = self.get(db, pk)
        data = obj_in.model_dump(exclude_unset=True)
        for field, value in data.items():
            setattr(db_obj, field, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, pk: Any) -> dict:
        db_obj = self.get(db, pk)
        db.delete(db_obj)
        db.commit()
        return {"detail": f"Registro {pk} eliminado correctamente"}

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import create_access_token, create_refresh_token, hash_password, verify_password
from app.repositories.user import UserRepository
from app.schemas.user import TokenSchema, UserSchema


class AuthService:
    def __init__(self, db: Session):
        self.db = db
        self.user_repository = UserRepository(db=db)

    def register(self, email: str, password: str) -> UserSchema:
        existing_user = self.user_repository.get_by_email(email)
        if existing_user:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")

        hashed = hash_password(password=password)

        user = self.user_repository.create(email=email, password=hashed)
        self.db.commit()

        return UserSchema.model_validate(user)

    def login(self, email: str, password: str) -> TokenSchema:
        user = self.user_repository.get_by_email(email=email)

        if not user or not verify_password(password=password, hashed=user.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

        access = create_access_token({"sub": user.id})
        refresh = create_refresh_token({"sub": user.id})

        return TokenSchema(
            access_token=access,
            refresh_token=refresh
        )
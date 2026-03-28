from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from core.database import get_db
from core.security import hash_password, verify_password, create_access_token
from models import Usuario
from schemas import LoginRequest, TokenResponse, UsuarioRegister, UsuarioOut

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=UsuarioOut, status_code=201)
def register(body: UsuarioRegister, db: Session = Depends(get_db)):
    existing = db.query(Usuario).filter(Usuario.Usuario_DNI == body.Usuario_DNI).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Ya existe un usuario con ese DNI",
        )
    usuario = Usuario(
        Usuario_Nombres=body.Usuario_Nombres,
        Usuario_Apellidos=body.Usuario_Apellidos,
        Usuario_FechaNacimiento=body.Usuario_FechaNacimiento,
        Usuario_DNI=body.Usuario_DNI,
        Usuario_Rol=body.Usuario_Rol,
        Usuario_Password=hash_password(body.Usuario_Password),
    )
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario


@router.post("/login", response_model=TokenResponse)
def login(body: LoginRequest, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.Usuario_DNI == body.Usuario_DNI).first()
    if not usuario or not verify_password(body.Usuario_Password, usuario.Usuario_Password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="DNI o contraseña incorrectos",
        )
    token = create_access_token({
        "sub": str(usuario.Usuario_ID),
        "dni": usuario.Usuario_DNI,
        "rol": usuario.Usuario_Rol,
    })
    return {"access_token": token}

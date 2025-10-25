from fastapi import APIRouter, HTTPException
from app.auth.schemas import LoginRequest, TokenResponse

router = APIRouter()

@router.post("/login", response_model=TokenResponse)
def login(request: LoginRequest):
    if request.username == "admin" and request.password == "1234":
        return TokenResponse(
            access_token="mock_access_token",
            refresh_token="mock_refresh_token",
            token_type="bearer",
            expires_in=900,
            user={"id": 1, "full_name": "Administrador", "role": "admin"}
        )
    raise HTTPException(status_code=401, detail="Credenciais inválidas")

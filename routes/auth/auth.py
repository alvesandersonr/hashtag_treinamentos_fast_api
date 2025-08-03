from fastapi import APIRouter, Depends
from models import Usuario
from dependencies import pegar_sessao

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
    """
    Essa é a rota padrão de autenticação do nosso sistema.
    """
    return {"message": "Você acessou a rota de autenticação", "auth": False}

@auth_router.post("/criar-conta")
async def criar_conta(nome: str, email: str, senha: str, session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email == email).first()
    if usuario:
        return {"message": "Usuário já existe"}
    
    novo_usuario = Usuario(nome, email, senha)
    session.add(novo_usuario)
    session.commit()
    session.close()
    return {"message": "Usuário criado com sucesso"}
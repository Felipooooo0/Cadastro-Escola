from datetime import date
from pydantic import BaseModel, EmailStr


# ==========================================
# SCHEMAS - ALUNO
# ==========================================
class AlunoCreate(BaseModel):
    nome: str
    cpf: str
    email: EmailStr
    data_nascimento: date
    telefone: str | None = None
    ra: str


class AlunoResponse(BaseModel):
    codAluno: int
    nome: str
    cpf: str
    email: EmailStr
    data_nascimento: date
    telefone: str | None = None
    ra: str


# ==========================================
# SCHEMAS - PROFESSOR
# ==========================================
class ProfessorCreate(BaseModel):
    nome: str
    cpf: str
    email: EmailStr
    data_nascimento: date
    telefone: str | None = None


class ProfessorResponse(BaseModel):
    codProf: int
    nome: str
    cpf: str
    email: EmailStr
    data_nascimento: date
    telefone: str | None = None


# ==========================================
# SCHEMAS - FUNCIONÁRIO
# ==========================================
class FuncionarioCreate(BaseModel):
    nome: str
    cpf: str
    email: EmailStr
    data_nascimento: date
    telefone: str | None = None


class FuncionarioResponse(BaseModel):
    codFunc: int
    nome: str
    cpf: str
    email: EmailStr
    data_nascimento: date
    telefone: str | None = None


# ==========================================
# SCHEMAS - TURMA
# ==========================================
class TurmaCreate(BaseModel):
    curso: str
    modulo: str
    ano: date


class TurmaResponse(BaseModel):
    codTurma: int
    curso: str
    modulo: str
    ano: date


# ==========================================
# SCHEMAS - VÍNCULOS (TurmaAluno e TurmaProfessor)
# ==========================================
class TurmaAlunoCreate(BaseModel):
    codTurma: int
    codAluno: int


class TurmaAlunoResponse(BaseModel):
    codTurmaAluno: int
    codTurma: int
    codAluno: int


class TurmaProfessorCreate(BaseModel):
    codTurma: int
    codProf: int


class TurmaProfessorResponse(BaseModel):
    codTurmaProfessor: int
    codTurma: int
    codProf: int
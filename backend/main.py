from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from mysql.connector import IntegrityError

from backend.database import criar_conexao
from backend.schemas import (
    AlunoCreate,
    AlunoResponse,
    ProfessorCreate,
    ProfessorResponse,
    FuncionarioCreate,
    FuncionarioResponse,
    TurmaCreate,
    TurmaResponse,
    TurmaAlunoCreate,
    TurmaAlunoResponse,
    TurmaProfessorCreate,
    TurmaProfessorResponse
)

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

app.mount(
    "/frontend",
    StaticFiles(directory=FRONTEND_DIR),
    name="frontend"
)

@app.get("/", include_in_schema=False)
def pagina_inicial():
    return FileResponse(FRONTEND_DIR / "index.html")

@app.get("/cadastro-de-aluno", include_in_schema=False)
def pagina_cadastro_aluno():
    return FileResponse(FRONTEND_DIR / "cadastrodealuno.html")

@app.get("/cadastro-de-professor", include_in_schema=False)
def pagina_cadastro_professor():
    return FileResponse(FRONTEND_DIR / "cadastrodeprofessor.html")

@app.get("/cadastro-de-funcionario", include_in_schema=False)
def pagina_cadastro_funcionario():
    return FileResponse(FRONTEND_DIR / "cadastrodefuncionario.html")


@app.get("/alunos", response_model=list[AlunoResponse])
def listar_alunos():
    conexao = criar_conexao()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos")
    registros = cursor.fetchall()

    cursor.close()
    conexao.close()

    alunos = []
    for registro in registros:
        alunos.append({
            "codAluno": registro[0],
            "nome": registro[1],
            "cpf": registro[2],
            "email": registro[3],
            "data_nascimento": registro[4],
            "telefone": registro[5],
            "ra": registro[6]
        })

    return alunos

@app.post("/alunos", response_model=AlunoResponse)
def cadastrar_aluno(aluno: AlunoCreate):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    sql = '''
        INSERT INTO alunos
        (nome, cpf, email, data_nascimento, telefone, ra)
        VALUES (%s, %s, %s, %s, %s, %s)
    '''
    valores = (
        aluno.nome,
        aluno.cpf,
        aluno.email,
        aluno.data_nascimento,
        aluno.telefone,
        aluno.ra
    )

    try:
        cursor.execute(sql, valores)
        conexao.commit()

        return {
            "codAluno": cursor.lastrowid,
            "nome": aluno.nome,
            "cpf": aluno.cpf,
            "email": aluno.email,
            "data_nascimento": aluno.data_nascimento,
            "telefone": aluno.telefone,
            "ra": aluno.ra
        }

    except IntegrityError as erro:
        conexao.rollback()
        if erro.errno == 1062:
            raise HTTPException(status_code=409, detail="CPF ou RA já cadastrado.")
        raise HTTPException(status_code=500, detail="Erro de integridade no banco de dados.")

    finally:
        cursor.close()
        conexao.close()

@app.get("/professores", response_model=list[ProfessorResponse])
def listar_professores():
    conexao = criar_conexao()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM professor")
    registros = cursor.fetchall()

    cursor.close()
    conexao.close()

    professores = []
    for registro in registros:
        professores.append({
            "codProf": registro[0],
            "nome": registro[1],
            "cpf": registro[2],
            "email": registro[3],
            "data_nascimento": registro[4],
            "telefone": registro[5]
        })

    return professores

@app.post("/professores", response_model=ProfessorResponse)
def cadastrar_professor(professor: ProfessorCreate):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    sql = '''
        INSERT INTO professor
        (nome, cpf, email, data_nascimento, telefone)
        VALUES (%s, %s, %s, %s, %s)
    '''
    valores = (
        professor.nome,
        professor.cpf,
        professor.email,
        professor.data_nascimento,
        professor.telefone
    )

    try:
        cursor.execute(sql, valores)
        conexao.commit()

        return {
            "codProf": cursor.lastrowid,
            "nome": professor.nome,
            "cpf": professor.cpf,
            "email": professor.email,
            "data_nascimento": professor.data_nascimento,
            "telefone": professor.telefone
        }

    except IntegrityError as erro:
        conexao.rollback()
        if erro.errno == 1062:
            raise HTTPException(status_code=409, detail="CPF já cadastrado.")
        raise HTTPException(status_code=500, detail="Erro de integridade no banco de dados.")

    finally:
        cursor.close()
        conexao.close()


@app.get("/funcionarios", response_model=list[FuncionarioResponse])
def listar_funcionarios():
    conexao = criar_conexao()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM funcionario")
    registros = cursor.fetchall()

    cursor.close()
    conexao.close()

    funcionarios = []
    for registro in registros:
        funcionarios.append({
            "codFunc": registro[0],
            "nome": registro[1],
            "cpf": registro[2],
            "email": registro[3],
            "data_nascimento": registro[4],
            "telefone": registro[5]
        })

    return funcionarios

@app.post("/funcionarios", response_model=FuncionarioResponse)
def cadastrar_funcionario(funcionario: FuncionarioCreate):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    sql = '''
        INSERT INTO funcionario
        (nome, cpf, email, data_nascimento, telefone)
        VALUES (%s, %s, %s, %s, %s)
    '''
    valores = (
        funcionario.nome,
        funcionario.cpf,
        funcionario.email,
        funcionario.data_nascimento,
        funcionario.telefone
    )

    try:
        cursor.execute(sql, valores)
        conexao.commit()

        return {
            "codFunc": cursor.lastrowid,
            "nome": funcionario.nome,
            "cpf": funcionario.cpf,
            "email": funcionario.email,
            "data_nascimento": funcionario.data_nascimento,
            "telefone": funcionario.telefone
        }

    except IntegrityError as erro:
        conexao.rollback()
        if erro.errno == 1062:
            raise HTTPException(status_code=409, detail="CPF já cadastrado.")
        raise HTTPException(status_code=500, detail="Erro de integridade no banco de dados.")

    finally:
        cursor.close()
        conexao.close()


@app.get("/turmas", response_model=list[TurmaResponse])
def listar_turmas():
    conexao = criar_conexao()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM turma")
    registros = cursor.fetchall()

    cursor.close()
    conexao.close()

    turmas = []
    for registro in registros:
        turmas.append({
            "codTurma": registro[0],
            "curso": registro[1],
            "modulo": registro[2],
            "ano": registro[3]
        })

    return turmas

@app.post("/turmas", response_model=TurmaResponse)
def cadastrar_turma(turma: TurmaCreate):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    sql = '''
        INSERT INTO turma
        (curso, modulo, ano)
        VALUES (%s, %s, %s)
    '''
    valores = (turma.curso, turma.modulo, turma.ano)

    try:
        cursor.execute(sql, valores)
        conexao.commit()

        return {
            "codTurma": cursor.lastrowid,
            "curso": turma.curso,
            "modulo": turma.modulo,
            "ano": turma.ano
        }

    except Exception as erro:
        conexao.rollback()
        raise HTTPException(status_code=500, detail="Erro ao cadastrar turma.")

    finally:
        cursor.close()
        conexao.close()

@app.post("/turma-aluno", response_model=TurmaAlunoResponse)
def vincular_aluno_turma(vinculo: TurmaAlunoCreate):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    sql = '''
        INSERT INTO turma_aluno
        (codTurma, codAluno)
        VALUES (%s, %s)
    '''
    valores = (vinculo.codTurma, vinculo.codAluno)

    try:
        cursor.execute(sql, valores)
        conexao.commit()

        return {
            "codTurmaAluno": cursor.lastrowid,
            "codTurma": vinculo.codTurma,
            "codAluno": vinculo.codAluno
        }

    except IntegrityError as erro:
        conexao.rollback()
        raise HTTPException(status_code=400, detail="Erro de chave estrangeira: Turma ou Aluno inexistente.")

    finally:
        cursor.close()
        conexao.close()



@app.post("/turma-professor", response_model=TurmaProfessorResponse)
def vincular_professor_turma(vinculo: TurmaProfessorCreate):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    sql = '''
        INSERT INTO turma_professor
        (codTurma, codProf)
        VALUES (%s, %s)
    '''
    valores = (vinculo.codTurma, vinculo.codProf)

    try:
        cursor.execute(sql, valores)
        conexao.commit()

        return {
            "codTurmaProfessor": cursor.lastrowid,  
            "codTurma": vinculo.codTurma,
            "codProf": vinculo.codProf
        }

    except IntegrityError as erro:
        conexao.rollback()
        raise HTTPException(status_code=400, detail="Erro de chave estrangeira: Turma ou Professor inexistente.")

    finally:
        cursor.close()
        conexao.close()
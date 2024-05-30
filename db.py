import sqlite3

def inicailizarBD():
    conexao = sqlite3.connect('RadCadastro.db')
    cur = conexao.cursor()
    create = ["""
    CREATE TABLE IF NOT EXISTS Aluno 
        ( 
         alunoID INT PRIMARY KEY,  
         nomeAluno VARCHAR(50) NOT NULL 
        );""",
    """CREATE TABLE IF NOT EXISTS  Professores 
        ( 
         professorID INT PRIMARY KEY,  
         nomeProfessor VARCHAR(50)
        );
    """,
    """CREATE TABLE IF NOT EXISTS Curso 
        ( 
         cursoID INT PRIMARY KEY,  
         nomeCurso VARCHAR(50) NOT NULL 
        );""",
    """CREATE TABLE IF NOT EXISTS Disciplina 
        ( 
         disciplinaID INT PRIMARY KEY,  
         nomeDisciplina INT NOT NULL
        );
    """]

    fk_create = ['ALTER TABLE  Aluno ADD idCurso REFERENCES Curso (cursoID) ;',
                 'ALTER TABLE  Aluno ADD idDisciplina REFERENCES Disciplina (disciplinaID) ;',
                 'ALTER TABLE  Professores ADD idCurso REFERENCES Curso (cursoID) ;',
                 'ALTER TABLE  Professores ADD idDisciplina REFERENCES Disciplina (disciplinaID) ;',
                 'ALTER TABLE  Disciplina ADD idCurso REFERENCES Curso(cursoID);'
    ]
    for i in create:
        cur.execute(i)
        conexao.commit()
    for i in fk_create:
        cur.execute(i)
        conexao.commit()




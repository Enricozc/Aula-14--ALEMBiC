from models import  Session, Cursos, Alunos

#CRiar as funções do crud
# Cadastrar curso

def cadastrar_curso():
    with Session() as session:
        try:
            nome_curso = input("Digite o nome do curso: ")
            carga_horaria = int(input("Digite a carga horária do curso: "))
            descricao = input("Digite a descrição do curso: ").capitalize()
            curso = Cursos(nome=nome_curso, duracao=carga_horaria, descricao=descricao)
            session.add(curso)
            session.commit()
            print("Curso cadastrado com sucesso!")
        except Exception as e:
            session.rollback()
            print(f"Erro ao cadastrar curso: {e}")

cadastrar_curso()

"""#add aluno
def cadastrar_aluno():
    with Session() as session:
        try:
            nome_aluno = input("Digite o nome do aluno: ")
            email = input("Digite o email do aluno: ")
            curso_id = int(input("Digite o ID do curso que o aluno irá se matricular: "))
            aluno = Alunos(nome=nome_aluno, email=email, curso_id=curso_id)
            session.add(aluno)
            session.commit()
            print("Aluno cadastrado com sucesso!")
        except Exception as e:
            session.rollback()
            print(f"Erro ao cadastrar aluno: {e}")
cadastrar_aluno()"""
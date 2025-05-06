import random
import string
from faker import Faker
import psycopg2



fake = Faker('pt_BR')

# Função para gerar uma string aleatória
def gerar_string_aleatoria(tamanho, letras_ou_numeros='letras'):
    if letras_ou_numeros == 'letras':
        caracteres = string.ascii_letters  # Letras maiúsculas e minúsculas
    elif letras_ou_numeros == 'numeros':
        caracteres = string.digits  # Apenas números
    else:
        caracteres = string.ascii_letters + string.digits  # Letras e números

    return ''.join(random.choice(caracteres) for _ in range(tamanho))

###IDs

#RA_Aluno

IDS_Aluno = []
for i in range(0, 100):
    RA_Aluno = "A" + gerar_string_aleatoria(6, 'numeros')
    IDS_Aluno.append(RA_Aluno)

#Prof_ID

IDS_Prof = []


#Profs de Cordas
IDS_ProfC = []
for i in range(0, 6):

    ID_Prof = "PC" + gerar_string_aleatoria(4, 'numeros') 
    IDS_ProfC.append(ID_Prof)
    IDS_Prof.append(ID_Prof)

#Profs de Percussao
IDS_ProfP = []
for i in range(0, 3):
    ID_Prof = "PP" + gerar_string_aleatoria(4, 'numeros')
    IDS_ProfP.append(ID_Prof)
    IDS_Prof.append(ID_Prof)

#Profs de Sopro
IDS_ProfS = []
for i in range(0, 3):
    ID_Prof = "PS" + gerar_string_aleatoria(4, 'numeros')
    IDS_ProfS.append(ID_Prof)
    IDS_Prof.append(ID_Prof)


#Profs de Outros
IDS_ProfO = []
for i in range(0, 3):
    ID_Prof = "PO" + gerar_string_aleatoria(4, 'numeros')
    IDS_ProfO.append(ID_Prof)
    IDS_Prof.append(ID_Prof)

#Departamentos

IDS_Dept = []

ID_Dept_CO = "DCO" + gerar_string_aleatoria(4, 'numeros')
ID_Dept_PE = "DPE" + gerar_string_aleatoria(4, 'numeros')
ID_Dept_SO = "DSO" + gerar_string_aleatoria(4, 'numeros')
ID_Dept_OU = "DOU" + gerar_string_aleatoria(4, 'numeros')

IDS_Dept.append(ID_Dept_CO)
IDS_Dept.append(ID_Dept_PE)
IDS_Dept.append(ID_Dept_SO)
IDS_Dept.append(ID_Dept_OU)

#Disciplina

IDS_Disc = []

#Dept Cordas
IDS_DiscC = []
for i in range(0, 12):
    ID_Disc = "DC" + gerar_string_aleatoria(4, 'numeros')
    IDS_DiscC.append(ID_Disc)
    IDS_Disc.append(ID_Disc)

#Dept de Percussao
IDS_DiscP = []
for i in range(0, 6):
    ID_Disc = "DP" + gerar_string_aleatoria(4, 'numeros')
    IDS_DiscP.append(ID_Disc)
    IDS_Disc.append(ID_Disc)

#Dept de Sopro
IDS_DiscS = []
for i in range(0, 6):
    ID_Disc = "DS" + gerar_string_aleatoria(4, 'numeros')
    IDS_DiscS.append(ID_Disc)
    IDS_Disc.append(ID_Disc)

#Dept de Outros
IDS_DiscO = []
for i in range(0, 6):
    ID_Disc = "DO" + gerar_string_aleatoria(4, 'numeros')
    IDS_DiscO.append(ID_Disc)
    IDS_Disc.append(ID_Disc)

#Curso
IDS_Curso = []

#Dept de Cordas
IDS_CursoC = []
for i in range(0, 4):
    ID_Curso = "CC" + gerar_string_aleatoria(4, 'numeros')
    IDS_CursoC.append(ID_Curso)
    IDS_Curso.append(ID_Curso)

#Dept de Percussao
IDS_CursoP = []
for i in range(0, 2):
    ID_Curso = "CP" + gerar_string_aleatoria(4, 'numeros')
    IDS_CursoP.append(ID_Curso)
    IDS_Curso.append(ID_Curso)

#Dept de Sopro
IDS_CursoS = []
for i in range(0, 2):
    ID_Curso = "CS" + gerar_string_aleatoria(4, 'numeros')
    IDS_CursoS.append(ID_Curso)
    IDS_Curso.append(ID_Curso)

#Dept de Outros
IDS_CursoO = []
for i in range(0, 2):
    ID_Curso = "CO" + gerar_string_aleatoria(4, 'numeros')
    IDS_CursoO.append(ID_Curso)
    IDS_Curso.append(ID_Curso)

#Nomes

#Nome Aluno
Nomes_Aluno = []
for i in range(0, 100):
    Nome_Aluno = fake.name()
    Nomes_Aluno.append(Nome_Aluno)

#Nome Professor
Nomes_Prof = []
for i in range(0, 15):
    Nome_Prof = fake.name()
    Nomes_Prof.append(Nome_Prof)

#Nome Departamento
Nomes_Dept = []
Nome_Dept1 = "Cordas"
Nome_Dept2 = "Percussao"
Nome_Dept3 = "Sopro"
Nome_Dept4 = "Outros"
Nomes_Dept.append(Nome_Dept1)
Nomes_Dept.append(Nome_Dept2)
Nomes_Dept.append(Nome_Dept3)
Nomes_Dept.append(Nome_Dept4)

#Nome Disciplina
Nomes_Disc = []

Nome_Disc1 = "Violao"
Nome_Disc2 = "Violao"
Nome_Disc3 = "Violao"
Nome_Disc4 = "Baixo"
Nome_Disc5 = "Baixo"
Nome_Disc6 = "Baixo"
Nome_Disc7 = "Guitarra"
Nome_Disc8 = "Guitarra"
Nome_Disc9 = "Guitarra"
Nome_Disc10 = "Piano"
Nome_Disc11 = "Piano"
Nome_Disc12 = "Piano"
Nome_Disc13 = "Flauta"
Nome_Disc14 = "Flauta"
Nome_Disc15 = "Flauta"
Nome_Disc16 = "Trombone"
Nome_Disc17 = "Trombone"
Nome_Disc18 = "Trombone"
Nome_Disc19 = "Bateria"
Nome_Disc20 = "Bateria"
Nome_Disc21 = "Bateria"
Nome_Disc22 = "Pandeiro"
Nome_Disc23 = "Pandeiro"
Nome_Disc24 = "Pandeiro"
Nome_Disc25 = "Teoria Musical"
Nome_Disc26 = "Teoria Musical"
Nome_Disc27 = "Teoria Musical"
Nome_Disc28 = "Canto"
Nome_Disc29 = "Canto"
Nome_Disc30 = "Canto"

Nomes_Disc.append(Nome_Disc1)
Nomes_Disc.append(Nome_Disc2)
Nomes_Disc.append(Nome_Disc3)
Nomes_Disc.append(Nome_Disc4)
Nomes_Disc.append(Nome_Disc5)
Nomes_Disc.append(Nome_Disc6)
Nomes_Disc.append(Nome_Disc7)
Nomes_Disc.append(Nome_Disc8)
Nomes_Disc.append(Nome_Disc9)
Nomes_Disc.append(Nome_Disc10)
Nomes_Disc.append(Nome_Disc11)
Nomes_Disc.append(Nome_Disc12)
Nomes_Disc.append(Nome_Disc13)
Nomes_Disc.append(Nome_Disc14)
Nomes_Disc.append(Nome_Disc15)
Nomes_Disc.append(Nome_Disc16)
Nomes_Disc.append(Nome_Disc17)
Nomes_Disc.append(Nome_Disc18)
Nomes_Disc.append(Nome_Disc19)
Nomes_Disc.append(Nome_Disc20)
Nomes_Disc.append(Nome_Disc21)
Nomes_Disc.append(Nome_Disc22)
Nomes_Disc.append(Nome_Disc23)
Nomes_Disc.append(Nome_Disc24)
Nomes_Disc.append(Nome_Disc25)
Nomes_Disc.append(Nome_Disc26)
Nomes_Disc.append(Nome_Disc27)
Nomes_Disc.append(Nome_Disc28)
Nomes_Disc.append(Nome_Disc29)
Nomes_Disc.append(Nome_Disc30)

#Nome Curso
Nomes_Curso = []

Nome_Curso1 = "Violao"
Nome_Curso2 = "Baixo"
Nome_Curso3 = "Guitarra"
Nome_Curso4 = "Piano"
Nome_Curso5 = "Flauta"
Nome_Curso6 = "Trombone"
Nome_Curso7 = "Bateria"
Nome_Curso8 = "Pandeiro"
Nome_Curso9 = "Teoria Musical"
Nome_Curso10 = "Canto"

Nomes_Curso.append(Nome_Curso1)
Nomes_Curso.append(Nome_Curso2)
Nomes_Curso.append(Nome_Curso3)
Nomes_Curso.append(Nome_Curso4)
Nomes_Curso.append(Nome_Curso5)
Nomes_Curso.append(Nome_Curso6)
Nomes_Curso.append(Nome_Curso7)
Nomes_Curso.append(Nome_Curso8)
Nomes_Curso.append(Nome_Curso9)
Nomes_Curso.append(Nome_Curso10)

#Nível de cada disciplina
Nivel_Disciplina = []
for i in range(0, 10):
    Nivel_Disciplina.append("1")
    Nivel_Disciplina.append("2")
    Nivel_Disciplina.append("3")

#print(len(Nivel_Disciplina))

#Coordenador de cada curso
Cord_Curso = []
Cord_CursoC = []
Cord_CursoP = []
Cord_CursoS = []
Cord_CursoO = []

for i in range(0, len(IDS_CursoC)):
    aux = random.randrange(0, len(IDS_ProfC))
    Cord_CursoC.append(IDS_ProfC[aux])
    Cord_Curso.append(IDS_ProfC[aux])

for i in range(0, len(IDS_CursoP)):
    aux = random.randrange(0, len(IDS_ProfP))
    Cord_CursoP.append(IDS_ProfP[aux])
    Cord_Curso.append(IDS_ProfP[aux])

for i in range(0, len(IDS_CursoS)):
    aux = random.randrange(0, len(IDS_ProfS))
    Cord_CursoS.append(IDS_ProfS[aux])
    Cord_Curso.append(IDS_ProfS[aux])

for i in range(0, len(IDS_CursoO)):
    aux = random.randrange(0, len(IDS_ProfO))
    Cord_CursoO.append(IDS_ProfO[aux])
    Cord_Curso.append(IDS_ProfO[aux])

#print(len(IDS_Curso))
#print(len(Cord_Curso))
#print(Cord_Curso)

#Chefe de cada departamento

Chefe_Dept = []

aux = random.randrange(0, len(IDS_ProfC))
Chefe_DeptC = IDS_ProfC[aux]

aux = random.randrange(0, len(IDS_ProfP))
Chefe_DeptP = IDS_ProfP[aux]
aux = random.randrange(0, len(IDS_ProfS))
Chefe_DeptS = IDS_ProfS[aux]
aux = random.randrange(0, len(IDS_ProfO))
Chefe_DeptO = IDS_ProfO[aux]

Chefe_Dept.append(Chefe_DeptC)
Chefe_Dept.append(Chefe_DeptP)
Chefe_Dept.append(Chefe_DeptS)
Chefe_Dept.append(Chefe_DeptO)

print(Chefe_Dept)

#Departamento de cada curso

Curso_Dept = []
for i in range(0,4):
	Curso_Dept.append(ID_Dept_CO)

for i in range(0,2):
	Curso_Dept.append(ID_Dept_PE)

for i in range(0,2):
	Curso_Dept.append(ID_Dept_SO)

for i in range(0,2):
	Curso_Dept.append(ID_Dept_OU)


#print(Curso_Dept)

#Departamento de cada professor
Profs_Dept = []
for i in range(0, 6):
	Profs_Dept.append(ID_Dept_CO)

for i in range(0, 3):
	Profs_Dept.append(ID_Dept_PE)

for i in range(0,3):
	Profs_Dept.append(ID_Dept_SO)

for i in range(0,3):
	Profs_Dept.append(ID_Dept_OU)

#print(Profs_Dept)


#Disciplina de cada aluno
Aluno_Disc = []
for i in range(0, 100):
	aux = random.randrange(0, len(IDS_Disc))
	Aluno_Disc.append(IDS_Disc[aux])

#Disciplina de cada professor
Prof_Disc = []
for i in range(len(IDS_Disc)):
	Prof_Disc.append(IDS_Disc[i])


#Historico Aluno

#RA
#IDS Aluno

#Disc_ID
#Aluno_Disc

#Ano
Ano_Hist_Aluno  = []
for i in range(0, 100):
	Ano_Hist_Aluno.append("2025")

#Index Aluno
Index_Hist_Aluno = list(range(0, len(IDS_Aluno)))

#Historico Professor

#Prof_ID
Prof_ID_Hist = []
for i in range(0, len(IDS_Prof)):
	for j in range(0, 2):
		Prof_ID_Hist.append(IDS_Prof[i])

#print(len(Prof_ID_Hist))

#Disc_ID
#Prof_Disc

#Ano
Ano_Hist_Prof = []
for i in range(0, len(Prof_ID_Hist)):
	Ano_Hist_Prof.append("2025")

#Index
Index_Hist_Prof = list(range(0, len(IDS_Disc)))

#Alunos especificos

#RA

RA_Aluno_Espec = []
for i in range(0, 50):
    RA_Aluno = "A" + gerar_string_aleatoria(6, 'numeros')
    RA_Aluno_Espec.append(RA_Aluno)

#Nome 
Nome_Aluno_Espec = []
for i in range(0, 50):
    Nome_Aluno = fake.name()
    Nome_Aluno_Espec.append(Nome_Aluno)



#Disciplinas dos alunos especificos
Aluno_Espec_Disc = []
Aluno_Espec_Disc.append(IDS_Disc[2])
Aluno_Espec_Disc.append(IDS_Disc[28])
Aluno_Espec_Disc.append(IDS_Disc[7])
Aluno_Espec_Disc.append(IDS_Disc[28])
Aluno_Espec_Disc.append(IDS_Disc[20])
Aluno_Espec_Disc.append(IDS_Disc[21])
Aluno_Espec_Disc.append(IDS_Disc[4])
Aluno_Espec_Disc.append(IDS_Disc[9])
Aluno_Espec_Disc.append(IDS_Disc[29])
Aluno_Espec_Disc.append(IDS_Disc[12])

aux_previous = None
for i in range(0,90):
	while True:
		aux = random.randrange(0, len(IDS_Disc))
		if aux != aux_previous:
			break
	Aluno_Espec_Disc.append(IDS_Disc[aux])

#print(len(Aluno_Espec_Disc))
	
#Historico aluno especifico

#RA para o historico
RA_Hist = []
for i in range(0, 50):
    for j in range(0, 2):
            RA_Hist.append(RA_Aluno_Espec[i])

#Ano
Ano_Hist_Aluno_Espec = []
for i in range(0, len(RA_Hist)):
    Ano_Hist_Aluno_Espec.append("2025")

#Index
Index_Hist_Aluno_Espec = list(range(len(Index_Hist_Aluno), len(Index_Hist_Aluno) + 100))

#print(len(RA_Hist))
#print(len(Ano_Hist_Aluno_Espec))
#print(len(Index_Hist_Aluno_Espec))

#print(Index_Hist_Prof)
#print(Prof_ID_Hist)
#print(Prof_Disc)
#print(Ano_Hist_Prof)

#print(len(IDS_Aluno))
#print(len(Nomes_Aluno))

#Matriz Curricular

Curso_Matriz = []

for i in range(0, 10):
    for j in range(0, 3):
        Curso_Matriz.append(IDS_Curso[i])

Index_Matriz = list(range(0, len(Curso_Matriz)))

#try:
#    conexao = psycopg2.connect(
#        user="postgres.tcfynslqblbnodeewhdq",
#        password="Foguete50",
#        host="aws-0-sa-east-1.pooler.supabase.com",
#        port="5432",
#        dbname="postgres",
#    )
#    cursor = conexao.cursor()
#
#    sql_delete = """
#    TRUNCATE "Aluno", "Professor", "Departamento", "Disciplina", CASCADE;
#    """
#
#    cursor.execute(sql_delete)
#    conexao.commit()
#
#    print("Todos os dados da tabela foram excluidos com sucesso")
#
#
#except Exception as ex:
#    print("Erro ao inserir dados", ex)
#
#finally:
#    if 'cursor' in locals():
#        cursor.close()
#    if 'conexao' in locals():
#        conexao.close()
#













if __name__ == '__main__':
    try:
        print("Conectando ao banco de dados...")
        conexao = psycopg2.connect(
            user="postgres.tcfynslqblbnodeewhdq",
            password="Foguete50",
            host="aws-0-sa-east-1.pooler.supabase.com",
            port="5432",
            dbname="postgres",
        )
        cursor = conexao.cursor()
        print("Conexão estabelecida com sucesso")

        #Alunos
        for i in range(len(IDS_Aluno)):
            cursor.execute("""
                INSERT INTO "Aluno" ("RA", "Nome")
                VALUES (%s, %s)
                """, (IDS_Aluno[i], Nomes_Aluno[i]))
        print(f"{len(IDS_Aluno)} alunos inseridos com sucesso")
        
        #Departamento
        for i in range(len(IDS_Dept)):
            cursor.execute("""
                INSERT INTO "Departamento" ("Dept_ID", "Nome")
                VALUES (%s, %s)
                """, (IDS_Dept[i], Nomes_Dept[i]))
        print(f"{len(IDS_Dept)} departamentos inseridos com sucesso")

        #Professores
        for i in range(len(IDS_Prof)):
            cursor.execute("""
                INSERT INTO "Professor" ("Prof_ID", "Nome", "Departamento")
                VALUES (%s, %s, %s)
                """, (IDS_Prof[i], Nomes_Prof[i], Profs_Dept[i]))
        print(f"{len(IDS_Prof)} professores inseridos com sucesso")

        #Atualiza chefe de departamento
        for i in range(len(Chefe_Dept)):
            cursor.execute("""
                UPDATE "Departamento"
                SET "Chefe" = %s
                WHERE "Dept_ID" = %s
                """, (Chefe_Dept[i], IDS_Dept[i]))
            print(f"{len(Chefe_Dept)} chefes de departamento inseridos com sucesso")

        #Curso
        for i in range(len(IDS_Curso)):
            cursor.execute("""
                INSERT INTO "Curso" ("Curso_ID", "Instrumento", "Coordenador", "Departamento")
                VALUES (%s, %s, %s, %s)
                """, (IDS_Curso[i], Nomes_Curso[i], Cord_Curso[i], Curso_Dept[i]))
        print(f"{len(IDS_Curso)} cursos inseridos com sucesso")

        #Disciplinas
        for i in range(len(IDS_Disc)):
            cursor.execute("""
                INSERT INTO "Disciplina" ("Disc_ID", "Instrumento", "Nivel")
                VALUES (%s, %s, %s)
                """, (IDS_Disc[i], Nomes_Disc[i], Nivel_Disciplina[i]))
        print(f"{len(IDS_Disc)} disciplinas inseridas com sucesso")

        #Historico Aluno
        for i in range(len(Index_Hist_Aluno)):
            cursor.execute("""
                INSERT INTO "Historico_Aluno" ("Index", "RA", "Disc_ID", "Ano")
                VALUES (%s, %s, %s, %s)
                """, (Index_Hist_Aluno[i], IDS_Aluno[i], Aluno_Disc[i], Ano_Hist_Aluno[i]))
        print(f"{len(Index_Hist_Aluno)} historicos de aluno inseridos com sucesso")

        #Historico Professor
        for i in range(len(Index_Hist_Prof)):
            cursor.execute("""
                INSERT INTO "Historico_Professor" ("Index", "Prof_ID", "Disc_ID", "Ano")
                VALUES (%s, %s, %s, %s)
                """, (Index_Hist_Prof[i], Prof_ID_Hist[i], Prof_Disc[i], Ano_Hist_Prof[i]))
        print(f"{len(Index_Hist_Prof)} historicos de professor inseridos com sucesso")

        #Alunos especificos
        for i in range(len(RA_Aluno_Espec)):
            cursor.execute("""
                INSERT INTO "Aluno" ("RA", "Nome")
                VALUES (%s, %s)
                """, (RA_Aluno_Espec[i], Nome_Aluno_Espec[i]))
        print(f"{len(RA_Aluno_Espec)} alunos especificos inseridos com sucesso")

        #Historico dos alunos especificos
        for i in range(len(Index_Hist_Aluno_Espec)):
            cursor.execute("""
                INSERT INTO "Historico_Aluno" ("Index", "RA", "Disc_ID", "Ano")
                VALUES (%s, %s, %s, %s)
                """, (Index_Hist_Aluno_Espec[i], RA_Hist[i], Aluno_Espec_Disc[i],  Ano_Hist_Aluno_Espec[i]))
        print(f"{len(Index_Hist_Aluno_Espec)} historicos de alunos especificos inseridos com sucesso")

       ##Matriz Curricular
        for i in range(len(Index_Matriz)):
            cursor.execute("""
                INSERT INTO "Matriz_Curricular" ("Index", "Curso", "Disciplina")
                VALUES (%s, %s, %s)
                """, (Index_Matriz[i], Curso_Matriz[i], IDS_Disc[i]))
        print(f"{len(Index_Matriz)} matriz curricular adicionada")

        conexao.commit()

    except Exception as ex:
        print("Erro durante as operações", ex)
        if 'conexao' in locals():
            conexao.rollback()
        print("Todas as operações foram revertidas devido ao erro")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()
            print("Conexão com o banco de dados encerrada")
            



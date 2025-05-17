import psycopg2
from psycopg2 import Error
from datetime import datetime

# --- DETALHES DA CONEXÃO ---
DB_NAME = "postgres"
DB_USER = "postgres.tcfynslqblbnodeewhdq"
DB_PASSWORD = "Foguete50" 
DB_HOST = "aws-0-sa-east-1.pooler.supabase.com"
DB_PORT = "5432"

LOG_FILE = 'validacao_banco_escola_musica.log'

def conectar_banco():
    try:
        connection = psycopg2.connect(
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        return connection
    except (Exception, Error) as error:
        log_message = f"Erro ao conectar ao PostgreSQL: {error}"
        escrever_log(log_message)
        print(log_message) # Adicionado para feedback imediato no console
        return None

def escrever_log(mensagem):
    with open(LOG_FILE, 'a', encoding='utf-8') as arquivo_log:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        arquivo_log.write(f"[{timestamp}] {mensagem}\n")

def validar_regras():
    # Criar cabeçalho do log
    with open(LOG_FILE, 'w', encoding='utf-8') as f: # 'w' para sobrescrever o log a cada execução
        pass # Apenas para limpar/criar o arquivo
    escrever_log("\n" + "="*50)
    escrever_log("INÍCIO DA VALIDAÇÃO DO BANCO DE DADOS - ESCOLA DE MÚSICA")
    escrever_log("="*50 + "\n")

    connection = conectar_banco()
    if not connection:
        escrever_log("FALHA NA CONEXÃO. Validação abortada.")
        escrever_log("="*50 + "\nFIM DA VALIDAÇÃO\n" + "="*50 + "\n")
        return
    
    cursor = connection.cursor()
    total_registros = {
        'aluno': 0,
        'professor': 0,
        'departamento': 0,
        'curso': 0,
        'disciplina': 0,
        'historico_aluno': 0,
        'historico_professor': 0,
        'matriz_curricular': 0
    }
    total_violacoes = 0
    
    try:
        # Contagem total de registros
        cursor.execute('SELECT COUNT(*) FROM "Aluno"')
        total_registros['aluno'] = cursor.fetchone()[0]
        cursor.execute('SELECT COUNT(*) FROM "Professor"')
        total_registros['professor'] = cursor.fetchone()[0]
        cursor.execute('SELECT COUNT(*) FROM "Departamento"')
        total_registros['departamento'] = cursor.fetchone()[0]
        cursor.execute('SELECT COUNT(*) FROM "Curso"')
        total_registros['curso'] = cursor.fetchone()[0]
        cursor.execute('SELECT COUNT(*) FROM "Disciplina"')
        total_registros['disciplina'] = cursor.fetchone()[0]
        cursor.execute('SELECT COUNT(*) FROM "Historico_Aluno"')
        total_registros['historico_aluno'] = cursor.fetchone()[0]
        cursor.execute('SELECT COUNT(*) FROM "Historico_Professor"')
        total_registros['historico_professor'] = cursor.fetchone()[0]
        cursor.execute('SELECT COUNT(*) FROM "Matriz_Curricular"')
        total_registros['matriz_curricular'] = cursor.fetchone()[0]


        escrever_log("RESUMO DO BANCO:")
        escrever_log(f"Total de Alunos: {total_registros['aluno']}")
        escrever_log(f"Total de Professores: {total_registros['professor']}")
        escrever_log(f"Total de Departamentos: {total_registros['departamento']}")
        escrever_log(f"Total de Cursos: {total_registros['curso']}")
        escrever_log(f"Total de Disciplinas: {total_registros['disciplina']}")
        escrever_log(f"Total de Registros em Historico_Aluno: {total_registros['historico_aluno']}")
        escrever_log(f"Total de Registros em Historico_Professor: {total_registros['historico_professor']}")
        escrever_log(f"Total de Registros em Matriz_Curricular: {total_registros['matriz_curricular']}\n")
        
        # 1. Todo Professor deve ter um Departamento
        escrever_log("\nVALIDAÇÃO 1: Professores sem departamento")
        cursor.execute('''
            SELECT "Prof_ID", "Nome" 
            FROM "Professor" 
            WHERE "Departamento" IS NULL OR "Departamento" = '';
        ''')
        profs_sem_dep = cursor.fetchall()
        if profs_sem_dep:
            total_violacoes += len(profs_sem_dep)
            escrever_log(f"VIOLAÇÃO: Foram encontrados {len(profs_sem_dep)} professores sem departamento:")
            for prof in profs_sem_dep:
                escrever_log(f"  Prof_ID: {prof[0]}, Nome: {prof[1]}")
        else:
            escrever_log("✓ Todos os professores possuem departamento atribuído.")

        # 2. Todo Departamento deve ter um Chefe (Professor)
        escrever_log("\nVALIDAÇÃO 2: Departamentos sem chefe")
        cursor.execute('''
            SELECT "Dept_ID", "Nome" 
            FROM "Departamento" 
            WHERE "Chefe" IS NULL OR "Chefe" = '';
        ''')
        deps_sem_chefe = cursor.fetchall()
        if deps_sem_chefe:
            total_violacoes += len(deps_sem_chefe)
            escrever_log(f"VIOLAÇÃO: Foram encontrados {len(deps_sem_chefe)} departamentos sem chefe:")
            for dep in deps_sem_chefe:
                escrever_log(f"  Dept_ID: {dep[0]}, Nome: {dep[1]}")
        else:
            escrever_log("✓ Todos os departamentos possuem chefe atribuído.")

        # 3. Todo Curso deve ter um Coordenador (Professor)
        escrever_log("\nVALIDAÇÃO 3: Cursos sem coordenador")
        cursor.execute('''
            SELECT "Curso_ID", "Instrumento" 
            FROM "Curso" 
            WHERE "Coordenador" IS NULL OR "Coordenador" = '';
        ''')
        cursos_sem_coord = cursor.fetchall()
        if cursos_sem_coord:
            total_violacoes += len(cursos_sem_coord)
            escrever_log(f"VIOLAÇÃO: Foram encontrados {len(cursos_sem_coord)} cursos sem coordenador:")
            for curso in cursos_sem_coord:
                escrever_log(f"  Curso_ID: {curso[0]}, Instrumento: {curso[1]}")
        else:
            escrever_log("✓ Todos os cursos possuem coordenador atribuído.")

        # 4. Todo Curso deve ter um Departamento
        escrever_log("\nVALIDAÇÃO 4: Cursos sem departamento")
        cursor.execute('''
            SELECT "Curso_ID", "Instrumento" 
            FROM "Curso" 
            WHERE "Departamento" IS NULL OR "Departamento" = '';
        ''')
        cursos_sem_dep = cursor.fetchall()
        if cursos_sem_dep:
            total_violacoes += len(cursos_sem_dep)
            escrever_log(f"VIOLAÇÃO: Foram encontrados {len(cursos_sem_dep)} cursos sem departamento:")
            for curso in cursos_sem_dep:
                escrever_log(f"  Curso_ID: {curso[0]}, Instrumento: {curso[1]}")
        else:
            escrever_log("✓ Todos os cursos possuem departamento atribuído.")

        # 5. Todos os Alunos devem estar na tabela Historico_Aluno
        #    (Esta regra também implica que "Todo Aluno deve ter pelo menos uma disciplina")
        escrever_log("\nVALIDAÇÃO 5: Alunos não encontrados em Historico_Aluno")
        cursor.execute('''
            SELECT "RA", "Nome"
            FROM "Aluno"
            WHERE "RA" NOT IN (SELECT DISTINCT "RA" FROM "Historico_Aluno");
        ''')
        alunos_sem_hist = cursor.fetchall()
        if alunos_sem_hist:
            total_violacoes += len(alunos_sem_hist)
            escrever_log(f"VIOLAÇÃO: Foram encontrados {len(alunos_sem_hist)} alunos sem nenhum registro em Historico_Aluno:")
            for aluno in alunos_sem_hist:
                escrever_log(f"  RA: {aluno[0]}, Nome: {aluno[1]}")
        else:
            escrever_log("✓ Todos os alunos possuem registros em Historico_Aluno.")

        # 6. Todos os Professores devem estar na tabela Historico_Professor
        escrever_log("\nVALIDAÇÃO 6: Professores não encontrados em Historico_Professor")
        cursor.execute('''
            SELECT "Prof_ID", "Nome"
            FROM "Professor"
            WHERE "Prof_ID" NOT IN (SELECT DISTINCT "Prof_ID" FROM "Historico_Professor");
        ''')
        profs_sem_hist = cursor.fetchall()
        if profs_sem_hist:
            total_violacoes += len(profs_sem_hist)
            escrever_log(f"VIOLAÇÃO: Foram encontrados {len(profs_sem_hist)} professores sem nenhum registro em Historico_Professor:")
            for prof in profs_sem_hist:
                escrever_log(f"  Prof_ID: {prof[0]}, Nome: {prof[1]}")
        else:
            escrever_log("✓ Todos os professores possuem registros em Historico_Professor.")

        # 7. Todos os Cursos e Disciplinas devem estar na tabela Matriz_Curricular
        escrever_log("\nVALIDAÇÃO 7: Cursos não encontrados em Matriz_Curricular")
        cursor.execute('''
            SELECT "Curso_ID", "Instrumento"
            FROM "Curso"
            WHERE "Curso_ID" NOT IN (SELECT DISTINCT "Curso" FROM "Matriz_Curricular" WHERE "Curso" IS NOT NULL);
        ''') 
        cursos_sem_matriz = cursor.fetchall()
        if cursos_sem_matriz:
            total_violacoes += len(cursos_sem_matriz)
            escrever_log(f"VIOLAÇÃO: Foram encontrados {len(cursos_sem_matriz)} cursos sem nenhum registro em Matriz_Curricular:")
            for curso in cursos_sem_matriz:
                escrever_log(f"  Curso_ID: {curso[0]}, Instrumento: {curso[1]}")
        else:
            escrever_log("✓ Todos os cursos possuem registros em Matriz_Curricular.")

        escrever_log("\nVALIDAÇÃO 8: Disciplinas não encontradas em Matriz_Curricular")
        cursor.execute('''
            SELECT "Disc_ID", "Instrumento", "Nivel"
            FROM "Disciplina"
            WHERE "Disc_ID" NOT IN (SELECT DISTINCT "Disciplina" FROM "Matriz_Curricular" WHERE "Disciplina" IS NOT NULL);
        ''') 
        disciplinas_sem_matriz = cursor.fetchall()
        if disciplinas_sem_matriz:
            total_violacoes += len(disciplinas_sem_matriz)
            escrever_log(f"VIOLAÇÃO: Foram encontradas {len(disciplinas_sem_matriz)} disciplinas sem nenhum registro em Matriz_Curricular:")
            for disc in disciplinas_sem_matriz:
                escrever_log(f"  Disc_ID: {disc[0]}, Instrumento: {disc[1]}, Nível: {disc[2]}")
        else:
            escrever_log("✓ Todas as disciplinas possuem registros em Matriz_Curricular.")


        escrever_log("\n" + "-"*20 + " RESUMO DA VALIDAÇÃO " + "-"*20)
        if total_violacoes == 0:
            escrever_log("STATUS: SUCESSO! Todas as regras de validação foram atendidas.")
            print("STATUS: SUCESSO! Todas as regras de validação foram atendidas.")
        else:
            escrever_log(f"STATUS: FALHA! Foram encontradas {total_violacoes} violações nas regras de validação.")
            print(f"STATUS: FALHA! Foram encontradas {total_violacoes} violações nas regras de validação. Verifique o arquivo '{LOG_FILE}'.")

        escrever_log("\n" + "="*50)
        escrever_log("FIM DA VALIDAÇÃO")
        escrever_log("="*50 + "\n")

    except (Exception, Error) as error:
        log_msg = f"ERRO DURANTE A VALIDAÇÃO: {error}"
        escrever_log(log_msg)
        print(log_msg)
    finally:
        if connection:
            cursor.close()
            connection.close()
            escrever_log("Conexão com o PostgreSQL fechada.")
            # print("Conexão com o PostgreSQL fechada.") 

if __name__ == "__main__":
    validar_regras()

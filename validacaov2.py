import psycopg2
from psycopg2 import Error
from datetime import datetime

LOG_FILE = 'validacao_escola_musica_v2.log'

def conectar_banco():
    try:
        connection = psycopg2.connect(
            database="postgres",
            user="postgres.tcfynslqblbnodeewhdq",
            password="Foguete50",
            host="aws-0-sa-east-1.pooler.supabase.com",
            port="5432"
        )
        return connection
    except (Exception, Error) as error:
        msg = f"Erro ao conectar ao PostgreSQL: {error}"
        escrever_log(msg)
        print(msg)
        return None

def escrever_log(mensagem):
    with open(LOG_FILE, 'a', encoding='utf-8') as arquivo_log:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        arquivo_log.write(f"[{timestamp}] {mensagem}\n")

def validar_regras():
    open(LOG_FILE, 'w', encoding='utf-8').close()
    
    escrever_log("\n" + "="*50)
    escrever_log("INÍCIO DA VALIDAÇÃO - BANCO DE DADOS ESCOLA DE MÚSICA")
    escrever_log("="*50 + "\n")

    connection = conectar_banco()
    if not connection:
        escrever_log("ERRO: Falha na conexão com o banco. Validação cancelada.")
        return
    
    cursor = connection.cursor()
    total_registros = {
        'alunos': 0,
        'professores': 0,
        'departamentos': 0,
        'cursos': 0,
        'disciplinas': 0,
        'historico_aluno': 0,
        'historico_professor': 0,
        'matriz': 0
    }
    violacoes = 0
    
    try:
        cursor.execute('SELECT COUNT(*) FROM "Aluno"')
        total_registros['alunos'] = cursor.fetchone()[0]
        cursor.execute('SELECT COUNT(*) FROM "Professor"')
        total_registros['professores'] = cursor.fetchone()[0]
        cursor.execute('SELECT COUNT(*) FROM "Departamento"')
        total_registros['departamentos'] = cursor.fetchone()[0]
        cursor.execute('SELECT COUNT(*) FROM "Curso"')
        total_registros['cursos'] = cursor.fetchone()[0]
        cursor.execute('SELECT COUNT(*) FROM "Disciplina"')
        total_registros['disciplinas'] = cursor.fetchone()[0]
        cursor.execute('SELECT COUNT(*) FROM "Historico_Aluno"')
        total_registros['historico_aluno'] = cursor.fetchone()[0]
        cursor.execute('SELECT COUNT(*) FROM "Historico_Professor"')
        total_registros['historico_professor'] = cursor.fetchone()[0]
        cursor.execute('SELECT COUNT(*) FROM "Matriz_Curricular"')
        total_registros['matriz'] = cursor.fetchone()[0]

        escrever_log("RESUMO GERAL DO BANCO:")
        escrever_log(f"- Alunos cadastrados: {total_registros['alunos']}")
        escrever_log(f"- Professores cadastrados: {total_registros['professores']}")
        escrever_log(f"- Departamentos registrados: {total_registros['departamentos']}")
        escrever_log(f"- Cursos disponíveis: {total_registros['cursos']}")
        escrever_log(f"- Disciplinas cadastradas: {total_registros['disciplinas']}")
        escrever_log(f"- Registros no Histórico de Alunos: {total_registros['historico_aluno']}")
        escrever_log(f"- Registros no Histórico de Professores: {total_registros['historico_professor']}")
        escrever_log(f"- Registros na Matriz Curricular: {total_registros['matriz']}\n")
        
        escrever_log("\nVERIFICAÇÃO 1 -> Alunos sem disciplinas no histórico")
        cursor.execute('''
            SELECT DISTINCT a."RA", a."Nome" 
            FROM "Aluno" a
            LEFT JOIN "Historico_Aluno" ha ON a."RA" = ha."RA" 
            WHERE ha."RA" IS NULL;
        ''')
        alunos_sem_disciplina = cursor.fetchall()
        if alunos_sem_disciplina:
            violacoes += len(alunos_sem_disciplina)
            escrever_log(f"AVISO: {len(alunos_sem_disciplina)} aluno(s) sem nenhuma disciplina no histórico:")
            for aluno in alunos_sem_disciplina:
                escrever_log(f"  - RA: {aluno[0]} | Nome: {aluno[1]}")
        else:
            escrever_log("OK - Todos os alunos possuem disciplinas no histórico")

        escrever_log("\nVERIFICAÇÃO 2 -> Professores sem histórico de disciplinas")
        cursor.execute('''
            SELECT DISTINCT p."Prof_ID", p."Nome"
            FROM "Professor" p
            LEFT JOIN "Historico_Professor" hp ON p."Prof_ID" = hp."Prof_ID"
            WHERE hp."Prof_ID" IS NULL;
        ''')
        profs_sem_hist = cursor.fetchall()
        if profs_sem_hist:
            violacoes += len(profs_sem_hist)
            escrever_log(f"AVISO: {len(profs_sem_hist)} professor(es) sem histórico de disciplinas:")
            for prof in profs_sem_hist:
                escrever_log(f"  - ID: {prof[0]} | Nome: {prof[1]}")
        else:
            escrever_log("OK - Todos os professores possuem histórico de disciplinas")

        escrever_log("\nVERIFICAÇÃO 3 -> Departamentos sem chefe")
        cursor.execute('''
            SELECT d."Dept_ID", d."Nome"
            FROM "Departamento" d
            WHERE d."Chefe" IS NULL;
        ''')
        deps_sem_chefe = cursor.fetchall()
        if deps_sem_chefe:
            violacoes += len(deps_sem_chefe)
            escrever_log(f"AVISO: {len(deps_sem_chefe)} departamento(s) sem chefe:")
            for dep in deps_sem_chefe:
                escrever_log(f"  - ID: {dep[0]} | Nome: {dep[1]}")
        else:
            escrever_log("OK - Todos os departamentos possuem chefe")

        escrever_log("\nVERIFICAÇÃO 4 -> Professores sem departamento")
        cursor.execute('''
            SELECT p."Prof_ID", p."Nome"
            FROM "Professor" p
            WHERE p."Departamento" IS NULL;
        ''')
        profs_sem_dep = cursor.fetchall()
        if profs_sem_dep:
            violacoes += len(profs_sem_dep)
            escrever_log(f"AVISO: {len(profs_sem_dep)} professor(es) sem departamento:")
            for prof in profs_sem_dep:
                escrever_log(f"  - ID: {prof[0]} | Nome: {prof[1]}")
        else:
            escrever_log("OK - Todos os professores estão vinculados a departamentos")

        escrever_log("\nVERIFICAÇÃO 5 -> Cursos não incluídos na matriz curricular")
        cursor.execute('''
            SELECT DISTINCT c."Curso_ID", c."Instrumento"
            FROM "Curso" c
            LEFT JOIN "Matriz_Curricular" m ON c."Curso_ID" = m."Curso"
            WHERE m."Curso" IS NULL;
        ''')
        cursos_sem_matriz = cursor.fetchall()
        if cursos_sem_matriz:
            violacoes += len(cursos_sem_matriz)
            escrever_log(f"AVISO: {len(cursos_sem_matriz)} curso(s) não incluídos na matriz curricular:")
            for curso in cursos_sem_matriz:
                escrever_log(f"  - ID: {curso[0]} | Instrumento: {curso[1]}")
        else:
            escrever_log("OK - Todos os cursos estão na matriz curricular")

        escrever_log("\nVERIFICAÇÃO 6 -> Disciplinas fora da matriz curricular")
        cursor.execute('''
            SELECT DISTINCT d."Disc_ID", d."Instrumento", d."Nivel"
            FROM "Disciplina" d
            LEFT JOIN "Matriz_Curricular" m ON d."Disc_ID" = m."Disciplina"
            WHERE m."Disciplina" IS NULL;
        ''')
        disc_sem_matriz = cursor.fetchall()
        if disc_sem_matriz:
            violacoes += len(disc_sem_matriz)
            escrever_log(f"AVISO: {len(disc_sem_matriz)} disciplina(s) não incluídas na matriz curricular:")
            for disc in disc_sem_matriz:
                escrever_log(f"  - ID: {disc[0]} | Instrumento: {disc[1]} | Nível: {disc[2]}")
        else:
            escrever_log("OK - Todas as disciplinas estão na matriz curricular")

        escrever_log("\n" + "-"*20)
        escrever_log("RESULTADO DA VALIDAÇÃO:")
        if violacoes == 0:
            msg = "SUCESSO: Nenhuma inconsistência encontrada!"
            escrever_log(msg)
            print(msg)
        else:
            msg = f"ATENÇÃO: Foram encontradas {violacoes} inconsistência(s)!"
            escrever_log(msg)
            print(f"{msg} Verifique o arquivo {LOG_FILE} para mais detalhes.")

        escrever_log("-"*20)
        escrever_log("\n" + "="*50)
        escrever_log("FIM DA VALIDAÇÃO")
        escrever_log("="*50)

    except (Exception, Error) as error:
        msg = f"ERRO DURANTE A VALIDAÇÃO: {error}"
        escrever_log(msg)
        print(msg)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    validar_regras()

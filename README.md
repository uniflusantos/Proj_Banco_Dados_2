# Projeto 2 Banco de Dados

## Autores
Lucas Roberto Boccia dos Santos (22.123.012-1)

Pedro Alexandre Custódio Silva (22.123.049-3)

## Descrição
O projeto 2 de Banco de Dados consiste na implementação de um sistema de banco de dados para uma escola de música em seu primeiro ano de funcionamento (tema escolhido pelo grupo). O sistema deve ser capaz de armazenar e gerenciar as informações mais comuns do dia a dia de uma escola de música.

Nosso projeto conta com 8 tabelas para armazenar as informações, sendo elas:

Tabela Aluno: Armazena o RA (identificador e chave primária) do aluno e o nome do aluno.

Tabela Professor: Armazena o ID (identificador e chave primária) do professor, o nome do professor e o departamento que o professor faz parte (que é uma foreign key da tabela departamento).

Tabela Departamento: Armazena o ID (identificador e chave primária) do departamento, o nome do departamento e o professor que é chefe do departamento (que é uma foreign key da tabela professor).

Tabela Disciplina: Armazena o ID (identificador e chave primária) da disciplina, o instrumento da disciplina (que funciona como o nome da disciplina) e o nível dessa tal disciplina (dividido em I, II ou III).

Tabela Curso: Armazena o ID (identificador e chave primária) do curso, o nome do curso, o professor que é coordenador do curso (que é uma foreign key da tabela professor) e o departamento ao qual o curso pertence (que é uma foreign key da tabela departamento).

Tabela Matriz Curricular: É formada pela junção das tabelas Curso e Disciplina, possuindo o ID do curso (que é uma foreign key da tabela curso) e o ID da disciplina (que é uma foreign key da tabela disciplina), mostrando assim as disciplinas contidas em cada curso.

Tabela Histórico Aluno: É formada pela junção das tabelas Aluno e Disciplina, possuindo o RA do aluno (que é uma foreign key da tabela aluno), o ID da(s) disciplina(s) que o aluno cursa e o ano em que cursou ou está cursando.

Tabela Histórico Professor: É formada pela junção das tabelas Professor e Disciplina, possuindo o ID do professor (que é uma foreign key da tabela professor), o ID da disciplina que o professor leciona (que é uma foreign keu da tabela disciplina) e o ano em que o professor lecionou ou leciona a disciplina.

As três últimas tabelas mencionadas possuem uma chave primária "Index", que serve apenas como identificador das posições na tabela.

## Como Executar
Para executar o projeto, primeiramente deve-se realizar o download dos arquivos disponibilizados no repositório e selecionar um serviço de banco de dados compatível com o PostgreSQL (como o Supabase, que foi o que utilizamos para os testes). Após isso, deve-se executar o script DDL disponibilizado no repositório para implementação das tabelas. Para alimentar as tabelas com dados, pode-se usar o arquivo "gerar_info2.py" disponibilizado no repositório, adaptando as informações necessárias para conexão com o seu banco de dados (como usuário e senha, que são diferentes para cada um). Pode-se validar a consistência das informações inseridas utilizando o arquivo "validacoes.py" disponibilizado no repositório. Por fim, testes podem ser feitos utilizando as queries disponibilizadas no repositório, no entanto, pode ser necessário adaptar algumas informações, como os IDs utilizados, que podem ser diferentes a cada vez que novas informações aleatórias são geradas.

## Modelo Relacional
![MR](https://github.com/user-attachments/assets/bfe06035-15b3-4930-b86d-c4efaa16bcbf)

## Modelo Entidade Relacionamento
#![MER](https://github.com/user-attachments/assets/bb96b5dd-bb4b-4b5a-88a5-416c6f6af050)




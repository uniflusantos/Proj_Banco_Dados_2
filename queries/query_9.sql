--Um professor da escola de música quer montar uma banda com alguns dos alunos da escola. Ele quer alunos que cursaram as disciplinas de guitarra, baixo, bateria e canto. Mostre os nomes dos alunos que cursaram essas disciplinas, além de qual das disciplinas eles cursaram. Ordene pelo nível da disciplina.
SELECT
	a."Nome" AS Nome_Aluno,
	d."Instrumento" AS Disciplina_Cursada,
	d."Nivel" AS Nivel_Disciplina
FROM
	"Aluno" a
	JOIN "Historico_Aluno" ha ON a."RA" = ha."RA"
	JOIN "Disciplina" d ON ha."Disc_ID" = d."Disc_ID"
WHERE
	d."Instrumento" IN ('Guitarra', 'Baixo', 'Bateria', 'Canto')
ORDER BY
	d."Nivel",
	d."Instrumento";

--O dono de um bar entrou em contato com a escola de música, pois queria um artista para se apresentar no bar. Ele quer uma lista de todos os alunos que cursaram as disciplinas de violão ou guitarra, e canto. Mostre o nome do aluno e o nome e nível da disciplina.
SELECT
	a."Nome" AS Nome_Aluno,
	d."Instrumento" AS Nome_Disciplina,
	d."Nivel" AS Nivel_Disciplina
FROM
	"Aluno" a
	JOIN "Historico_Aluno" ha ON a."RA" = ha."RA"
	JOIN "Disciplina" d ON ha."Disc_ID" = d."Disc_ID"
WHERE
	d."Instrumento" IN ('Violão', 'Guitarra', 'Canto')
	AND a."RA" IN (
		SELECT DISTINCT
			ha_inner."RA"
		FROM
			"Historico_Aluno" ha_inner
			JOIN "Disciplina" d_inner ON ha_inner."Disc_ID" = d_inner."Disc_ID"
		WHERE
			d_inner."Instrumento" = 'Canto'
	)
	AND a."RA" IN (
		SELECT DISTINCT
			ha_inner."RA"
		FROM
			"Historico_Aluno" ha_inner
			JOIN "Disciplina" d_inner ON ha_inner."Disc_ID" = d_inner."Disc_ID"
		WHERE
			d_inner."Instrumento" IN ('Violão', 'Guitarra')
	);

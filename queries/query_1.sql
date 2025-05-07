--Query: Retorna as disciplinas feitas por um aluno junto ao professor que lecionou a disciplina ao aluno
SELECT
	d."Disc_ID" AS Codigo_Disciplina,
	d."Instrumento" AS Nome_Disciplina,
	p."Nome" AS Nome_Professor
FROM
	"Historico_Aluno" ha
	JOIN "Disciplina" d ON ha."Disc_ID" = d."Disc_ID"
	LEFT JOIN "Historico_Professor" hp ON ha."Disc_ID" = hp."Disc_ID"
	AND ha."Ano" = hp."Ano"
	LEFT JOIN "Professor" p ON hp."Prof_ID" = p."Prof_ID"
WHERE
	ha."RA" = 'A007522';

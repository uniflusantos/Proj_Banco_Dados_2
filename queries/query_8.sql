--Para os alunos de ID "A007522", "A102603" e "A994253", mostre as disciplinas que eles cursam, junto do nome dos professores que lecionam essas disciplinas.
SELECT
	a."RA" AS ID_Aluno,
	a."Nome" AS Nome_Aluno,
	d."Instrumento" AS Nome_Disciplina,
	d."Nivel" AS Nivel_Disciplina,
	p."Nome" AS Nome_Professor
FROM
	"Aluno" a
	JOIN "Historico_Aluno" ha ON a."RA" = ha."RA"
	JOIN "Disciplina" d ON ha."Disc_ID" = d."Disc_ID"
	LEFT JOIN "Historico_Professor" hp ON ha."Disc_ID" = hp."Disc_ID"
	AND ha."Ano" = hp."Ano"
	LEFT JOIN "Professor" p ON hp."Prof_ID" = p."Prof_ID"
WHERE
	a."RA" IN ('A007522', 'A102603', 'A994253');

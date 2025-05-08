--Encontre os nomes de todos os estudantes que cursaram violão.
SELECT
	a."RA",
	a."Nome"
FROM
	"Aluno" a
	JOIN "Historico_Aluno" ha ON a."RA" = ha."RA"
	JOIN "Disciplina" d ON ha."Disc_ID" = d."Disc_ID"
WHERE
	d."Instrumento" = 'Violao';

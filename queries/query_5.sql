--Recupere os nomes e IDs dos estudantes que tiveram aula com o professor que tem o ID "PO9657".
SELECT
	a."RA" AS ID_Estudante,
	a."Nome" AS Nome_Estudante
FROM
	"Aluno" a
	JOIN "Historico_Aluno" ha ON a."RA" = ha."RA"
	JOIN "Historico_Professor" hp ON ha."Disc_ID" = hp."Disc_ID"
	AND ha."Ano" = hp."Ano"
WHERE
	hp."Prof_ID" = 'PO9657';

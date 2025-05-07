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
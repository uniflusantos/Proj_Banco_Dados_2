SELECT DISTINCT
	c."Instrumento" AS Nome_Curso
FROM
	"Curso" c
	JOIN "Matriz_Curricular" mc ON c."Curso_ID" = mc."Curso"
	JOIN "Historico_Professor" hp ON mc."Disciplina" = hp."Disc_ID"
WHERE
	hp."Prof_ID" IN ('PP0800', 'PO9444');
SELECT
	c."Instrumento" AS Nome_Curso
FROM
	"Curso" c
	JOIN "Departamento" d ON c."Departamento" = d."Dept_ID"
WHERE
	d."Nome" = 'Cordas';
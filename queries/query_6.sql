--Liste os cursos oferecidos pelo departamento de cordas.
SELECT
	c."Curso_ID",
	c."Instrumento" AS Nome_Curso
FROM
	"Curso" c
	JOIN "Departamento" d ON c."Departamento" = d."Dept_ID"
WHERE
	d."Nome" = 'Cordas';

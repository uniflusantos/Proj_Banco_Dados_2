SELECT
	p."Nome" AS Nome_Professor,
	COALESCE(d."Nome", 'nenhum') AS Departamento_Chefiado,
	COALESCE(c."Instrumento", 'nenhum') AS Curso_Coordenado
FROM
	"Professor" p
	LEFT JOIN "Departamento" d ON p."Prof_ID" = d."Chefe"
	LEFT JOIN "Curso" c ON p."Prof_ID" = c."Coordenador";
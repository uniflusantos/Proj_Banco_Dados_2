--Query: Liste todos os chefes de departamento e coordenadores de curso em apenas uma query de forma que a primeira coluna seja o nome do professor, a segunda o nome do departamento coordenado e a terceira o nome do curso que coordena. Substitua os campos em branco do resultado da query pelo texto "nenhum".
SELECT
	p."Nome" AS Nome_Professor,
	COALESCE(d."Nome", 'nenhum') AS Departamento_Chefiado,
	COALESCE(c."Instrumento", 'nenhum') AS Curso_Coordenado
FROM
	"Professor" p
	LEFT JOIN "Departamento" d ON p."Prof_ID" = d."Chefe"
	LEFT JOIN "Curso" c ON p."Prof_ID" = c."Coordenador"
WHERE
	d."Nome" IS NOT NULL
	OR c."Instrumento" IS NOT NULL;

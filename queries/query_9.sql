SELECT
	a."RA" AS ID_Estudante,
	a."Nome" AS Nome_Estudante
FROM
	"Aluno" a
WHERE
	a."RA" NOT IN (
		SELECT DISTINCT
			ha."RA"
		FROM
			"Historico_Aluno" ha
			JOIN "Disciplina" d ON ha."Disc_ID" = d."Disc_ID"
			JOIN "Matriz_Curricular" mc ON d."Disc_ID" = mc."Disciplina"
			JOIN "Curso" c ON mc."Curso" = c."Curso_ID"
			JOIN "Departamento" dep ON c."Departamento" = dep."Dept_ID"
		WHERE
			dep."Nome" = 'Cordas'
	);

SELECT
	p."Nome" AS Nome_Professor,
	COALESCE(d."Nome", 'nenhum') AS Departamento_Chefiado,
	COALESCE(c."Instrumento", 'nenhum') AS Curso_Coordenado
FROM
	"Professor" p
	LEFT JOIN "Departamento" d ON p."Prof_ID" = d."Chefe"
	LEFT JOIN "Curso" c ON p."Prof_ID" = c."Coordenador";
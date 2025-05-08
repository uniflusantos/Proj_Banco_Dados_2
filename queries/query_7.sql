--Liste os cursos que foram ministrados pelos professores de ID"PP0800" e "PO9444".
SELECT DISTINCT
	hp."Prof_ID", -- Adicionado ID do professor
	d."Instrumento" AS Nome_Disciplina,
	d."Nivel"
FROM
	"Disciplina" d
	JOIN "Historico_Professor" hp ON d."Disc_ID" = hp."Disc_ID"
WHERE
	hp."Prof_ID" IN ('PP0800', 'PO9444');

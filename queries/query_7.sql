--Liste os cursos que foram ministrados pelos professores de ID "PC1312" e "PP4708".
SELECT DISTINCT
	hp."Prof_ID", -- Adicionado ID do professor
	d."Instrumento" AS Nome_Disciplina,
	d."Nivel"
FROM
	"Disciplina" d
	JOIN "Historico_Professor" hp ON d."Disc_ID" = hp."Disc_ID"
WHERE
	hp."Prof_ID" IN ('PC1312', 'PP4708');

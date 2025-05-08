--Liste os IDs dos professores que ensinam mais de uma disciplina.
SELECT
	hp."Prof_ID",
	COUNT(DISTINCT hp."Disc_ID") as num_disciplinas
FROM
	"Historico_Professor" hp
GROUP BY
	hp."Prof_ID"
HAVING
	COUNT(DISTINCT hp."Disc_ID") >= 2
ORDER BY
	hp."Prof_ID";

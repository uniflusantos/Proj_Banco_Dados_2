SELECT
	hp."Prof_ID"
FROM
	"Historico_Professor" hp
GROUP BY
	hp."Prof_ID"
HAVING
	COUNT(DISTINCT hp."Disc_ID") > 1;
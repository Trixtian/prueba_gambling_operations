# Consulta para obtener la cantidad de jugadores FTD por mes
FTD_QUERY = """
SELECT 
    YEAR(d.deposit_date) AS year, 
    MONTH(d.deposit_date) AS month, 
    COUNT(DISTINCT d.player_id) AS ftd_count
FROM 
    deposits d
GROUP BY 
    YEAR(d.deposit_date), MONTH(d.deposit_date);
"""

# Consulta para obtener la cantidad de jugadores CPA por mes
CPA_QUERY = """
SELECT 
    YEAR(d.deposit_date) AS year, 
    MONTH(d.deposit_date) AS month, 
    COUNT(DISTINCT d.player_id) AS cpa_count
FROM 
    deposits d
JOIN 
    (SELECT 
        player_id 
     FROM 
        deposits 
     GROUP BY 
        player_id 
     HAVING 
        SUM(deposit_amount) > 100) AS cpa_players
ON 
    d.player_id = cpa_players.player_id
GROUP BY 
    YEAR(d.deposit_date), MONTH(d.deposit_date);
"""

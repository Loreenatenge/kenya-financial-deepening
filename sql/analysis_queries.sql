USE kenya-financial-deepening

SELECT
  
    year,
    private_credit_to_gdp,
    broad_money_to_gdp,
    gdp_growth

FROM economic_indicators
WHERE country = 'Kenya'
ORDER BY year;


SELECT 
    CASE
        WHEN year BETWEEN 1980 AND 1989 THEN '1980s'
        WHEN year BETWEEN 1990 AND 1999 THEN '1990s'
        WHEN year BETWEEN 2000 AND 2009 THEN '2000s'
        WHEN year BETWEEN 2010 AND 2019 THEN '2010s'
        ELSE '2020s'
    END AS decade,
    ROUND(AVG(private_credit_to_gdp), 2) AS avg_private_credit_to_gdp,
    ROUND(AVG(broad_money_to_gdp), 2) AS avg_broad_money_to_gdp,
    ROUND(AVG(gdp_growth), 2) AS avg_gdp_growth
FROM economic_indicators
WHERE country = 'Kenya'
GROUP BY decade
ORDER BY decade;


SELECT 
    year,
    private_credit_gdp,
    gdp_growth,
    CASE
        WHEN private_credit_gdp > 30 THEN 'High credit'
        WHEN private_credit_gdp BETWEEN 20 AND 30 THEN 'Medium credit'
        ELSE 'Low credit'
    END AS credit_category
FROM economic_indicators
WHERE country = 'Kenya'
ORDER BY private_credit_gdp DESC;


SELECT
    year,
    interest_rate_spread,
    gdp_growth
FROM economic_indicators
WHERE country = 'Kenya'
AND interest_rate_spread IS NOT NULL
ORDER BY year;
        

SELECT year, private_credit_to_gdp, gdp_growth
FROM economic_indicators
WHERE country = 'Kenya'
ORDER BY private_credit_to_gdp DESC
LIMIT 5;

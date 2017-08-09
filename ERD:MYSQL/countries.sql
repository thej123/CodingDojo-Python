SELECT name AS countries, language, percentage FROM countries
LEFT JOIN languages
ON countries.id = languages.country_id
WHERE language = 'Slovene'
ORDER BY percentage DESC;

SELECT countries.name AS countries, COUNT(cities.name) AS city_count
FROM countries
LEFT JOIN cities
ON countries.id = cities.country_id
GROUP BY countries.name
ORDER BY city_count DESC;

SELECT cities.name, cities.population
FROM countries
LEFT JOIN cities
ON countries.id = cities.country_id
WHERE countries.name = 'mexico' AND cities.population > 500000;

SELECT countries.name AS countries, languages.language, languages.percentage
FROM countries
LEFT JOIN languages
ON countries.id = languages.country_id
WHERE languages.percentage > 89
ORDER BY percentage DESC;

SELECT name, surface_area, population
FROM countries
WHERE surface_area < 501 AND population > 100000;

SELECT name, capital, life_expectancy
FROM countries
WHERE government_form = 'Constitutional Monarchy' and capital > 200 and life_expectancy > 75;

SELECT countries.name as country, cities.name as city, cities.district, cities.population
FROM countries
LEFT JOIN cities
ON countries.id = cities.country_id
WHERE countries.name = 'Argentina' and cities.district = 'Buenos Aires' and cities.population > 500000;

SELECT region, COUNT(name)
FROM countries
GROUP BY region
ORDER BY count(name) DESC;






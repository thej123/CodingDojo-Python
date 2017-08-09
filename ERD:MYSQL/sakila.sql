SELECT city.city_id, customer.first_name, customer.last_name, customer.email, CONCAT(address.address, " ", address.address2, " ", address.district, " ", address.postal_code, " ", city.city)
FROM address
LEFT JOIN customer
ON address.address_id = customer.address_id
RIGHT JOIN city
ON city.city_id = address.city_id
WHERE city.city_id = 312;

SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name
FROM film
LEFT JOIN film_category
ON film.film_id = film_category.film_id
LEFT JOIN category
ON category.category_id = film_category.category_id
WHERE  category.name = 'Comedy';

SELECT actor.actor_id, CONCAT(actor.first_name, ' ',  actor.last_name) as actor, film.title, film.description, film.release_year
FROM film
LEFT JOIN film_actor
ON film.film_id = film_actor.film_id
LEFT JOIN actor
ON actor.actor_id = film_actor.actor_id
WHERE actor.actor_id = 5;

SELECT store.store_id, city.city_id, customer.first_name, customer.last_name, customer.email, CONCAT_WS(" ", address.address, address.address2, address.district, city.city, country.country, address.postal_code)
FROM customer
JOIN address ON address.address_id = customer.address_id
JOIN city ON city.city_id = address.city_id
JOIN country ON city.country_id = country.country_id
JOIN store ON store.store_id = customer.store_id
WHERE store.store_id = 1 and (city.city_id = 1 or city.city_id = 42 or city.city_id = 312 or city.city_id = 459);

SELECT film.title, film.description, film.release_year, film.rating, film.special_features
FROM film
JOIN film_actor
ON film.film_id = film_actor.film_id
JOIN actor
ON actor.actor_id = film_actor.actor_id
WHERE actor.actor_id = 15 and film.special_features LIKE '%behind the scenes%' and film.rating = 'G';

SELECT film.film_id, film.title, actor.actor_id, CONCAT_WS(" ", actor.first_name, actor.last_name) AS name
FROM film
JOIN film_actor
ON film.film_id = film_actor.film_id
JOIN actor
ON actor.actor_id = film_actor.actor_id
WHERE film.film_id = 369;

SELECT film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features, category.name, film.rental_rate
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON category.category_id = film_category.category_id
WHERE film.rental_rate = 2.99 and category.name = 'Drama'; 

SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name, actor.first_name, actor.last_name
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON category.category_id = film_category.category_id
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE category.name = 'Action' and CONCAT_WS(" ", actor.first_name, actor.last_name) = 'SANDRA KILMER';


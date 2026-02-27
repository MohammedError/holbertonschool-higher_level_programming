-- LISTS ALL CITIES IN THE DATABASE HBTN_0D_USA WITH THEIR STATE NAMES
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;

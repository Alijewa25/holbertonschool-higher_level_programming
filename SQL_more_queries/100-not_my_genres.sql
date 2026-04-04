-- janrlar icinden adlari sec hansi ki ne deyil..
SELECT DISTINCT name
FROM tv_genres
-- (ardı olduğu kimi qalır...)
WHERE name NOT IN (
-- janrlar icinden adlar secirem, bu janrlari tv_shows_genres ile tv_genres e bagla ve orda adi Dexter olana
-- aid olanlari goster
    SELECT name
    FROM tv_genres
    JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
    WHERE tv_shows.title = 'Dexter'
)
-- bunu yazdiq belelikle dextere aid olmayanlari gosterecey
ORDER BY name ASC;

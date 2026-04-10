-- Show title və genre name göstər
SELECT tv_shows.title, tv_genres.name

-- Bütün show-lardan başla
FROM tv_shows

-- Show → show_genres
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id

-- show_genres → genres
LEFT JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id

-- Sıralama
ORDER BY tv_shows.title ASC, tv_genres.name ASC;

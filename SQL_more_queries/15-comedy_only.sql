-- Select all show titles that belong to Comedy genre
SELECT tv_shows.title
FROM tv_shows

-- Link shows to genres
JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id

-- Link to genres table
JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id

-- Filter only Comedy genre
WHERE tv_genres.name = 'Comedy'

-- Sort by title
ORDER BY tv_shows.title ASC;

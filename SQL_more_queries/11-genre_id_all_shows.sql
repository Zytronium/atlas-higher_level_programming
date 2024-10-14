-- lists all shows contained in the database hbtn_0d_tvshows
SELECT tv_shows.title, CASE WHEN EXISTS(tv_show_genres.genre_id) THEN tv_show_genres.genre_id ELSE NULL 
FROM tv_shows, tv_show_genres
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
-- removes all records with a score <= 5 in the table second_table of the database. They're too low to be worthy of being on the scoreboard.
DELETE FROM second_table
WHERE score <= 5;

-- prints a description of the table first_table from the database hbtn_0c_0
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_DEFAULT
FROM information_schema.columns
WHERE table_schema = 'hbtn_0c_0' AND table_name = 'first_table';

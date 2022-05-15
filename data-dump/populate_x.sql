CREATE TABLE IF NOT EXISTS source_table (
   id serial PRIMARY KEY,
   creation_date TIMESTAMP NOT NULL,
   sale_value INT NOT NULL
);

INSERT INTO source_table (id, creation_date, sale_value)
VALUES
	(1, current_date - INTEGER '5', 1000),
	(2, current_date - INTEGER '5', 2000),
	(3, current_date - INTEGER '4', 3000),
	(4, current_date - INTEGER '3', 4000),
	(5, current_date - INTEGER '3', 5000),
	(6, current_date - INTEGER '2', 6000),
	(7, current_date - INTEGER '1', 7000),
	(8, current_date - INTEGER '1', 8000),
	(9, current_date - INTEGER '1', 9000),
	(10, current_date, 10000)
ON CONFLICT(id) DO NOTHING;

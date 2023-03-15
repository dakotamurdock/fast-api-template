CREATE TABLE accounts(
	id INTEGER GENERATED ALWAYS AS IDENTITY,
	name VARCHAR(255) NOT NULL CHECK (name <> ''),
	email VARCHAR(255) NOT NULL CHECK (email <> ''),
	password VARCHAR(255) NOT NULL CHECK (password <> ''),
	UNIQUE(email),
	UNIQUE(id)
)

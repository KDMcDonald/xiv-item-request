PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS users(
	id TEXT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS items(
	id INTEGER PRIMARY KEY,
	item_name VARCHAR(50) UNIQUE NOT NULL,
	availability INTEGER NOT NULL,
	CONSTRAINT chk_availability_binary CHECK (availability IN (0,1))
);

CREATE TABLE IF NOT EXISTS servers(
	id TEXT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS server_crafters(
	server_id TEXT NOT NULL,
	crafter_id TEXT NOT NULL,
	PRIMARY KEY (server_id, crafter_id),
	FOREIGN KEY (server_id) REFERENCES servers(id),
	FOREIGN KEY (crafter_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS orders(
	id INTEGER PRIMARY KEY,
	server_id TEXT,
	crafter_id TEXT,
	customer_id TEXT,
	order_date DATE NOT NULL,
	fulfilled INTEGER NOT NULL,
	FOREIGN KEY (server_id) REFERENCES servers(id),
	FOREIGN KEY (crafter_id) REFERENCES users(id),
	FOREIGN KEY (customer_id) REFERENCES users(id),
	CONSTRAINT chk_fulfilled_binary CHECK (fulfilled IN (0,1))
);

CREATE TABLE IF NOT EXISTS carts(
	order_id INTEGER NOT NULL,
	item_id INTEGER NOT NULL,
	quantity INTEGER NOT NULL,
	PRIMARY KEY (order_id, item_id),
	FOREIGN KEY (order_id) REFERENCES orders(id),
	FOREIGN KEY (item_id) REFERENCES items(id)
);

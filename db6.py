1. -------------------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS contacts (
    contact_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    mobile_phone_number CHAR(10) NOT NULL,
    home_phone_number CHAR(7),
    FOREIGN KEY (customer_id) REFERENCES customers (id)
);

2,3.------------------------------------------------------------------------------------

СREATE TABLE IF NOT EXISTS customer(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer CHAR(35) NOT NULL
);

CREATE TABLE IF NOT EXISTS subdivision(
    subdivision_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    subdivision CHAR(25) NOT NULL,
    job_title   CHAR(50) NOT NULL,
    unit_description VARCHAR(255) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

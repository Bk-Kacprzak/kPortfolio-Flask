
-- DROP TABLE IF EXISTS user; 
DROP TABLE IF EXISTS portfolio; 
DROP TABLE IF EXISTS asset;
-- CREATE TABLE User( 
--     id INTEGER PRIMARY KEY AUTOINCREMENT, 
--     uuid STRING(64) NOT NULL,
--     username TEXT NOT NULL,
--     email TEXT UNIQUE NOT NULL,
--     password TEXT NOT NULL
-- );


CREATE TABLE Portfolio(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    name STRING(64) NOT NULL,
    total_cost INTEGER, 
    FOREIGN KEY (user_id) REFERENCES user(id)
);

CREATE TABLE Asset(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    portfolio_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    transaction_date DATETIME NOT NULL, 
    entry_price INTEGER NOT NULL,
    FOREIGN KEY (portfolio_id) REFERENCES Portfolio(id)
);
-- CREATE TABLE post (
--   id INTEGER PRIMARY KEY AUTOINCREMENT,
--   author_id INTEGER NOT NULL,
--   created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
--   title TEXT NOT NULL,
--   body TEXT NOT NULL,
--   FOREIGN KEY (author_id) REFERENCES user (id)
-- );

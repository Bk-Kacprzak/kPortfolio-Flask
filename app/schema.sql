
-- DROP TABLE IF EXISTS user; 
DROP TABLE IF EXISTS portfolio; 
DROP TABLE IF EXISTS asset;
DROP TABLE IF EXISTS AssetTransaction;
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
    average_buy_price FLOAT NOT NULL,
    total_amount FLOAT,
    average_sell_price FLOAT, 
    cost FLOAT NOT NULL,
    FOREIGN KEY (portfolio_id) REFERENCES Portfolio(id)
);

CREATE TABLE AssetTransaction(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    asset_id INTEGER NOT NULL,
    amount FLOAT NOT NULL,
    -- transaction_date DATETIME NOT NULL, 
    transaction_type TEXT NOT NULL,
    entry_price FLOAT NOT NULL,
    FOREIGN KEY (asset_id) REFERENCES Asset(id)
);
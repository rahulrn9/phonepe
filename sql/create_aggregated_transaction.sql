
CREATE TABLE aggregated_transaction (
    id SERIAL PRIMARY KEY,
    from_date DATE NOT NULL,
    to_date DATE NOT NULL,
    name VARCHAR(100) NOT NULL,
    type VARCHAR(50) NOT NULL,
    count BIGINT NOT NULL,
    amount DOUBLE PRECISION NOT NULL
);

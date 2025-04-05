CREATE TABLE cars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    brand TEXT,
    model TEXT,
    year INTEGER,
    mileage REAL DEFAULT 0,
    fuel_level REAL DEFAULT 100
    );

INSERT INTO cars (brand, model, year) VALUES
('Suzuki', 'Samurai', 1985),
('Nissan', 'Juke', 2010),
('Ford', 'Ranger', 2018),
('Suzuki','S-Cross','2022');

UPDATE cars
SET
    mileage = mileage + 15,
    fuel_level = fuel_level - (15 * 0.1)
WHERE id = 1;

UPDATE cars
SET
    mileage = mileage + 100,
    fuel_level = fuel_level - (100 * 0.1)
WHERE id = 2;

UPDATE cars
SET fuel_level = CASE
    WHEN fuel_level + 30 > 100 THEN 100
    ELSE fuel_level + 30
END
WHERE id = 3;

UPDATE cars
SET
    mileage = mileage + 50,
    fuel_level = fuel_level - (50 * 0.1)
WHERE id = 3;

SELECT SUM(mileage) AS total_mileage FROM cars;

SELECT
    brand,
    model,
    year,
    mileage,
    fuel_level
FROM cars;
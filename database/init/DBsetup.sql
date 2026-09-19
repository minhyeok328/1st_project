CREATE DATABASE IF NOT EXISTS tco_system;
USE tco_system;

DROP TABLE IF EXISTS parts;
CREATE TABLE IF NOT EXISTS parts (
  id INT AUTO_INCREMENT PRIMARY KEY,
  part_name VARCHAR(100) NOT NULL,
  cycle_km INT,
  price_tierA INT NOT NULL,
  price_tierB INT NOT NULL,
  price_tierC INT NOT NULL
);

INSERT
  INTO parts (part_name, cycle_km, price_tierA, price_tierB, price_tierC )
VALUES
('엔진오일', 7500,   75000, 130000, 350000),
('점화플러그', 70000, 65000, 125000, 320000),
('냉각수', 45000,    80000, 130000, 250000),
('타이밍벨트/체인', 115000, 400000, 700000, 1800000),
('브레이크 패드', 40000,   60000, 115000, 300000),
('브레이크 디스크', 80000, 160000, 280000, 750000),
('미션오일', 80000, 150000, 280000, 650000),
('타이어', 50000,   380000, 800000, 1600000),
('배터리', 60000,   130000, 250000, 450000),
('쇼크업소버', 80000,120000, 200000, 550000);

SELECT * FROM parts;

COMMIT;

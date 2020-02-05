-- Create table Margins_per_payment_type with foreign key the classifieds_id
CREATE TABLE Margins_per_payment_type
(
    id INT AUTO_INCREMENT PRIMARY KEY, 
    classifieds_id VARCHAR(32),
    payment_type VARCHAR(8) NOT NULL, 
    margin decimal(5,4) NOT NULL,
    created_at DATETIME(4),
    FOREIGN KEY (classifieds_id)
        REFERENCES Classifieds(id)
        ON DELETE CASCADE
);

-- Create table Margins_per_ad_type with foreign key the classifieds_id
CREATE TABLE Margins_per_ad_type
(
    id INT AUTO_INCREMENT PRIMARY KEY, 
    classifieds_id VARCHAR(32),
    ad_type VARCHAR(10) NOT NULL,
    margin decimal(5,4) NOT NULL,
    created_at DATETIME(4),
    FOREIGN KEY (classifieds_id)
        REFERENCES Classifieds(id)
        ON DELETE CASCADE
);

-- Insert data to the table Margins_per_payment_type created
INSERT INTO `Margins_per_payment_type` (`id`,`classifieds_id`) 
VALUES 
    (1,'d6707ce40a1447baaf012f948fb5b356'),
    (2,'d6708ce40a1547baaf012f948fb5b356'),
    (3,'d6702ce40a1447baaf012f948fb5b356'),
    (4,'d6701ce40a1447baaf012f948fb5b356'),
    (5,'d6701ce40a1447baaf012f948fb5b357');


-- Insert data to the table Margins_per_payment_type created
INSERT INTO `Margins_per_ad_type` (`id`,`classifieds_id`) 
VALUES 
    (1,'d6707ce40a1447baaf012f948fb5b356'),
    (2,'d6708ce40a1547baaf012f948fb5b356'),
    (3,'d6702ce40a1447baaf012f948fb5b356'),
    (4,'d6701ce40a1447baaf012f948fb5b356'),
    (5,'d6701ce40a1447baaf012f948fb5b357');

-- delete tables Margins_per_ad_type and Margins_per_payment_type
drop table Margins_per_payment_type;
drop table Margins_per_ad_type;
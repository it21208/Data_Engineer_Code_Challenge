use aidataengineer;

-- Create table for Classifieds with primary key the id column
CREATE TABLE Classifieds
(
    id VARCHAR(32) UNIQUE NOT NULL, 
    customer_id VARCHAR(32) CHARACTER SET utf8 NOT NULL, 
    created_at DATETIME(4) NOT NULL, 
    ad_text TEXT NOT NULL,
    ad_type VARCHAR(10) NOT NULL CHECK (ad_type IN ('Free','Premium','Platinum')), 
    price decimal(14, 2), 
    currency VARCHAR(10), 
    payment_type VARCHAR(8) CHECK (payment_type IN ('Offline','Card','Paypal')), 
    payment_cost decimal(3, 2)
);

-- Insert data to the table created
INSERT INTO `Classifieds` (`id`,`customer_id`,`created_at`,`ad_text`, `ad_type`, `price`,`currency`,`payment_type`,`payment_cost`) 
VALUES 
    ('d6707ce40a1447baaf012f948fb5b356','8e0fdcefc3ad45acbb5a2abc506c6c9f','2019-05-04T23:34:19.5934998Z','<p>aliquam sith amet dolore consectetuer ut dolore elit dolor euismod elit erat</p>','Premium',29.04,'EUR','Offline',0.30),
    ('d6708ce40a1547baaf012f948fb5b356','8e0fdcefc3ad45acbb5a2abc506c6c8f','2019-05-05T13:34:19.5434998Z','<p>aliquam sed amet dolore consectetuer ut dolore elit dolor euismod elit erat</p>','Platinum',19.04,'EUR','Card',0.17),
    ('d6702ce40a1447baaf012f948fb5b356','8e0fdcefc3ad45acbb5a2abc506c6c6f','2019-08-07T22:31:19.5734998Z','<p>forta sed amet dolore consectetuer nut dolore elit dolor euismod elit erat</p>','Premium',29.14,'EUR','Card',0.20),
    ('d6701ce40a1447baaf012f948fb5b356','8e0fdcefc3ad45acbb5a2abc506c6c5f','2019-09-03T22:34:19.3934998Z','<p>aliquam sed amet dolore consectetuer ut dolore elit dolor euismod elit berat</p>','Free',0,'EUR','Card',0),
    ('d6701ce40a1447baaf012f948fb5b357','8e0fdcefc3ad45acbb5a2abc506c6c5f','2019-09-03T22:34:19.3934998Z','<p>aliquam sed amet dolore consectetuer ut dolore elit dolor euismod elit berat</p>','Premium',3.08,'EUR','Card',0.10);

-- disable foreign key temporarily
SET FOREIGN_KEY_CHECKS=0; 

-- delete table
drop table Classifieds;

-- enable foreign key afterwards
SET FOREIGN_KEY_CHECKS=1;

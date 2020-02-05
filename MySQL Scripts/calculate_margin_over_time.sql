
-- validate that event_scheduler is enabled
SET GLOBAL event_scheduler = ON;
-- or
SET @@GLOBAL.event_scheduler = ON;

-- I was not able to perform the above command because of the following error 
-- ERROR 1227 (42000): Access denied; you need (at least one of) the SUPER privilege(s) for this operation.
-- Because I saw that you have other schemata apart from aidataengineer I did not play around or try ammending user privileges

-- create procedure that calculates margin over time per ad type
DELIMITER //
CREATE PROCEDURE calculate_margin_over_time_per_ad_type(IN per_ad_type VARCHAR(10))
BEGIN
UPDATE Classifieds, Margins_per_ad_type
SET Margins_per_ad_type.ad_type = Classifieds.ad_type,
    Margins_per_ad_type.margin =  (Classifieds.price - Classifieds.payment_cost) / Classifieds.price,
    Margins_per_ad_type.created_at =  NOW()
WHERE Classifieds.id = Margins_per_ad_type.classifieds_id AND Classifieds.ad_type = per_ad_type;
END//
DELIMITER ;

-- create procedure that calculates margin over time per payment type
DELIMITER //
CREATE PROCEDURE calculate_margin_over_time_per_payment_type(IN per_payment_type VARCHAR(8))
BEGIN
UPDATE Classifieds, Margins_per_payment_type
SET Margins_per_payment_type.payment_type = Classifieds.payment_type,
    Margins_per_payment_type.margin =  (Classifieds.price - Classifieds.payment_cost) / Classifieds.price,
    Margins_per_payment_type.created_at =  NOW()
WHERE Classifieds.id = Margins_per_payment_type.classifieds_id AND Classifieds.payment_type = per_payment_type;
END//
DELIMITER ;

-- show all stored procedures
SHOW PROCEDURE STATUS;

-- show stored procedures in a specific database
SHOW PROCEDURE STATUS WHERE Db = 'aidataengineer';

-- delete procedures  calculate_margin_over_time_per_ad_type and calculate_margin_over_time_per_payment_type
drop procedure calculate_margin_over_time_per_ad_type;
drop procedure calculate_margin_over_time_per_payment_type;

-- create an event that will call the procedure calculate_margin_over_time_per_ad_type every hour
CREATE EVENT `calculate_margin_every_hour_per_ad_type`
ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 1 HOUR 
ON COMPLETION PRESERVE
DO CALL calculate_margin_over_time_per_ad_type('Premium');


-- create an event that will call the procedure calculate_margin_over_time_per_ad_type every hour
CREATE EVENT `calculate_margin_every_hour_per_payment_type`
ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 1 HOUR 
ON COMPLETION PRESERVE
DO CALL calculate_margin_over_time_per_payment_type('Card');

-- show all events in aidataengineer
SHOW EVENTS FROM aidataengineer;

-- delete events calculate_margin_every_hour_per_ad_type and calculate_margin_every_hour_per_payment_type
drop event calculate_margin_every_hour_per_ad_type;
drop event calculate_margin_every_hour_per_payment_type;
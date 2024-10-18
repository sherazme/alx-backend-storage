-- creates function SafeDiv that divides (and returns) the first by the second number or returns 0
DROP FUNCTION IF EXISTS SafeDiv;
DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
    IF (b = 0)
    THEN
        RETURN (0);
    ELSE
        RETURN (a / b);
    END IF;
END
$$ 
DELIMITER ;

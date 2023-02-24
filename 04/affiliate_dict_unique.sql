CREATE TABLE affiliate_dict (
    affiliate_id NVARCHAR(10) CONSTRAINT PK_affiliate_dict PRIMARY KEY,
    affiliate_name VARCHAR(30),
    group_name VARCHAR(3),
    commission FLOAT,
    CONSTRAINT UQ_affiliate_id UNIQUE (affiliate_id)
);

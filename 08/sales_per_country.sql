CREATE TABLE sales_per_country (
	invoice_number NVARCHAR(8) NOT NULL,
	salesman_id CHAR(2) NULL,
	market CHAR(2) NULL,
	quantity FLOAT NULL,
	value FLOAT NULL,
	customer NVARCHAR(5) NULL,
	fv_date datetime NULL,
	surname VARCHAR(25) NULL,
	value_up FLOAT NULL,
	rebate_value FLOAT NULL
)

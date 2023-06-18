DROP TABLE if exists inflation_gdp;

CREATE TABLE inflation_gdp(
	country VARCHAR (30) not null,
	country_id integer not null,
	year bigint not null,
	Inflation DOUBLE PRECISION not null,
	GDP DOUBLE PRECISION not null,
	interestRate DOUBLE PRECISION not null,
	unemployment DOUBLE PRECISION not null,
	outcome integer not null
);

select * from inflation_gdp;

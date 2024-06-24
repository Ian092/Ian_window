CREATE TABLE student(
	student_id SERIAL PRIMARY KEY,
	name VARCHAR(20),
	major VARCHAR(20)
);

CREATE TABLE youbike (
  _id SERIAL PRIMARY KEY, 
  sna VARCHAR (50) NOT NULL, 
  sarea VARCHAR (50), 
  ar VARCHAR (100), 
  mday timestamp,
  updateTime timestamp,
  total smallint,
  rent_bikes smallint,
  retune_bike smallint,
  lat real,
  lng real
	
);

INSERT INTO student(name,major)
VALUES ('Ian','學生');

DROP TABLE accounts;
DROP TABLE youbike;

INSERT INTO youbike(sna,sarea,ar,mday,updatetime,total,rent_bikes,return_bikes,lat,lng,act)
VALUES ('臺大明達館北側(員工宿舍)',
	    '臺大公館校區',
	    '明達館前側北空地',
	    '2024-06-24 13:58:29',
	    '2024-06-24 14:21:52',
	    18,
	    18,
	    0,
	    25.02112,
	    121.54469,
	    '1'	
	);



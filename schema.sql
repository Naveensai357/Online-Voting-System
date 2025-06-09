
CREATE TABLE userdata (
	id SERIAL NOT NULL, 
	email VARCHAR, 
	password VARCHAR, 
	PRIMARY KEY (id)
)

;


CREATE TABLE votes (
	id SERIAL NOT NULL, 
	voter_id VARCHAR, 
	candidate VARCHAR, 
	PRIMARY KEY (voter_id)
)

;


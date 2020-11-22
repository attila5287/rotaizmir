CREATE TABLE note(
	id BIGSERIAL NOT NULL PRIMARY KEY, 
	category VARCHAR(32) NOT NULL, 
	date_posted TIMESTAMP NOT NULL, 
	content TEXT NOT NULL, 
	admin_id BIGINT NOT NULL REFERENCES public.user,
	user_id BIGINT NOT NULL REFERENCES public.user
);
DROP TABLE public.notes CASCADE;


DROP TABLE public.requests CASCADE;
CREATE TABLE request(
	id BIGSERIAL NOT NULL PRIMARY KEY, 
	category VARCHAR(32) NOT NULL, 
	date_posted TIMESTAMP NOT NULL, 
	content TEXT NOT NULL, 
	user_id BIGINT NOT NULL REFERENCES public.user
);

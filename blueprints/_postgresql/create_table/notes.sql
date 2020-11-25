DROP TABLE public.note CASCADE;
CREATE TABLE note(
	id BIGSERIAL NOT NULL PRIMARY KEY, 
	type VARCHAR(32) NOT NULL, 
	category VARCHAR(32) NOT NULL, 
	status VARCHAR(32), 
	date_posted TIMESTAMP NOT NULL, 
	content TEXT NOT NULL, 
	admin_id BIGINT,
	user_id BIGINT NOT NULL REFERENCES public.user
);


DROP TABLE public.request CASCADE;

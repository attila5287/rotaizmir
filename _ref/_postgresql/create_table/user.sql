DROP TABLE public.user CASCADE;
DROP TABLE public.post CASCADE;
	CREATE TABLE "user" (
		"id"	BIGSERIAL NOT NULL PRIMARY KEY,
		"username"	VARCHAR(20) NOT NULL UNIQUE,
		"email"	VARCHAR(120) NOT NULL UNIQUE,
		"image_file"	VARCHAR(255) NOT NULL,
		"img_url"	INTEGER NOT NULL,
		"password"	VARCHAR(255) NOT NULL,
		"is_member"	VARCHAR(32) NOT NULL,
		"is_admin"	VARCHAR(32) NOT NULL,
		"is_prez"	VARCHAR(32) NOT NULL
	);


	-- original
CREATE TABLE "user" (
		"id"	BIGSERIAL NOT NULL PRIMARY KEY,
		"username"	VARCHAR(20) NOT NULL UNIQUE,
		"email"	VARCHAR(120) NOT NULL UNIQUE,
		"image_file"	VARCHAR(255),
		"password"	VARCHAR(255),
		"img_url"	INTEGER
	);

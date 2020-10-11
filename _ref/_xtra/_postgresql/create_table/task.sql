-- postgres
CREATE TABLE "task" (
	"id"	BIGSERIAL NOT NULL PRIMARY KEY,
	"title"	VARCHAR(32) NOT NULL,
	"content"	TEXT,
	"done"	BOOLEAN,
	"is_urgent"	TEXT,
	"is_important"	TEXT,
	"matrix_zone"	TEXT,
	"border_style"	TEXT,
	"urg_points"	SMALLINT,
	"imp_points"	SMALLINT,
	"date_posted"	TIMESTAMP,
	"user_id"	BIGINT REFERENCES public.user
);

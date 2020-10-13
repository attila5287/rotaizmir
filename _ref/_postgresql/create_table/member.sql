CREATE TABLE "member" (
  	"id"	BIGSERIAL NOT NULL PRIMARY KEY,
	"user_id"	INTEGER,
	"first_name"	VARCHAR(64) NOT NULL,
	"middle_name"	VARCHAR(64),
	"last_name"	VARCHAR(64) NOT NULL,
	"phone_num"	VARCHAR(64),
	"gender"	VARCHAR(64),
	"email"	VARCHAR(64),
	"is_admin"	VARCHAR(64),
	"is_prez"	VARCHAR(64),
	"img_url"	VARCHAR(256),
	"linkedin"	VARCHAR(256),
	"instagram"	VARCHAR(256),
	"twitter"	VARCHAR(256)
)
;

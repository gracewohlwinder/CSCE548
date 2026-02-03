DROP DATABASE csce548_project;
CREATE DATABASE csce548_project;
USE csce548_project;

CREATE TABLE user (
	id          BIGINT UNSIGNED AUTO_INCREMENT NOT NULL,
	username    VARCHAR(50)  NOT NULL,
	description VARCHAR(200) NOT NULL DEFAULT '',
	created_at  DATETIME     NOT NULL DEFAULT (NOW()),
	PRIMARY KEY (id),
	INDEX (username),
	UNIQUE (username)
);

CREATE TABLE follower (
	user_id     BIGINT UNSIGNED NOT NULL,
	follower_id BIGINT UNSIGNED NOT NULL,
	created_at  DATETIME        NOT NULL DEFAULT (NOW()),
	PRIMARY KEY (user_id, follower_id),
	FOREIGN KEY (user_id)     REFERENCES user (id),
	FOREIGN KEY (follower_id) REFERENCES user (id)
);

CREATE TABLE post (
	id          BIGINT UNSIGNED AUTO_INCREMENT NOT NULL,
	user_id     BIGINT UNSIGNED NOT NULL,
	description TEXT            NOT NULL,
	created_at  DATETIME        NOT NULL DEFAULT (NOW()),
	deleted_at  DATETIME,
	PRIMARY KEY (id),
	FOREIGN KEY (user_id) REFERENCES user (id)
);

CREATE TABLE comment (
	id          BIGINT UNSIGNED AUTO_INCREMENT NOT NULL,
	post_id     BIGINT UNSIGNED NOT NULL,
	user_id     BIGINT UNSIGNED NOT NULL,
	comment     VARCHAR(200)    NOT NULL,
	created_at  DATETIME NOT NULL DEFAULT (NOW()),
	deleted_at  DATETIME,
	PRIMARY KEY (id),
	FOREIGN KEY (post_id) REFERENCES post (id),
	FOREIGN KEY (user_id) REFERENCES user (id)
);

CREATE TABLE favorite (
	post_id    BIGINT UNSIGNED NOT NULL,
	user_id    BIGINT UNSIGNED NOT NULL,
	created_at DATETIME        NOT NULL DEFAULT (NOW()),
	PRIMARY KEY (post_id, user_id),
	FOREIGN KEY (post_id) REFERENCES post (id),
	FOREIGN KEY (user_id) REFERENCES user (id)
);

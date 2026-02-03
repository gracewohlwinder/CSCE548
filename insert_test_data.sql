CREATE USER 'csce548'@'127.0.0.1' IDENTIFIED BY 'csce548';
GRANT ALL PRIVILEGES ON csce548_project.* TO 'csce548'@'127.0.0.1';

INSERT INTO user (username) VALUES
	('userA'),
	('userB'),
	('userC'),
	('userD'),
	('userE');

SET @UserA = (SELECT id FROM user WHERE username = 'userA');
SET @UserB = (SELECT id FROM user WHERE username = 'userB');
SET @UserC = (SELECT id FROM user WHERE username = 'userC');
SET @UserD = (SELECT id FROM user WHERE username = 'userD');
SET @UserE = (SELECT id FROM user WHERE username = 'userE');

UPDATE user SET description = 'userA profile biography' WHERE id = @UserA;

INSERT INTO follower (user_id, follower_id) VALUES
	(@UserA, @UserB),
	(@UserA, @UserC),
	(@UserB, @UserA),
	(@UserB, @UserC),
	(@UserB, @UserD),
	(@UserB, @UserE),
	(@UserC, @UserA),
	(@UserC, @UserD),
	(@UserC, @UserE),
	(@UserD, @UserB),
	(@UserD, @UserE);

INSERT INTO post (user_id, description) VALUES
	(@UserA, 'UserA first post description'),
	(@UserA, 'UserA second post description'),
	(@UserA, 'UserA third post description'),
	(@UserB, 'UserB first post description'),
	(@UserB, 'UserB second post description'),
	(@UserB, 'UserB third post description'),
	(@UserC, 'UserC first post description'),
	(@UserC, 'UserC second post description'),
	(@UserC, 'UserC third post description'),
	(@UserD, 'UserD first post description'),
	(@UserD, 'UserD second post description'),
	(@UserD, 'UserD third post description'),
	(@UserE, 'UserE first post description'),
	(@UserE, 'UserE second post description'),
	(@UserE, 'UserE third post description');

SET @UserA_Post1 = (SELECT id FROM post WHERE user_id = @UserA LIMIT 1);
SET @UserA_Post2 = (SELECT id FROM post WHERE user_id = @UserA LIMIT 1,1);
SET @UserA_Post3 = (SELECT id FROM post WHERE user_id = @UserA LIMIT 2,1);

SET @UserB_Post1 = (SELECT id FROM post WHERE user_id = @UserB LIMIT 1);
SET @UserB_Post2 = (SELECT id FROM post WHERE user_id = @UserB LIMIT 1,1);
SET @UserB_Post3 = (SELECT id FROM post WHERE user_id = @UserB LIMIT 2,1);

SET @UserC_Post1 = (SELECT id FROM post WHERE user_id = @UserC LIMIT 1);
SET @UserC_Post2 = (SELECT id FROM post WHERE user_id = @UserC LIMIT 1,1);
SET @UserC_Post3 = (SELECT id FROM post WHERE user_id = @UserC LIMIT 2,1);

SET @UserD_Post1 = (SELECT id FROM post WHERE user_id = @UserD LIMIT 1);
SET @UserD_Post2 = (SELECT id FROM post WHERE user_id = @UserD LIMIT 1,1);
SET @UserD_Post3 = (SELECT id FROM post WHERE user_id = @UserD LIMIT 2,1);

SET @UserE_Post1 = (SELECT id FROM post WHERE user_id = @UserE LIMIT 1);
SET @UserE_Post2 = (SELECT id FROM post WHERE user_id = @UserE LIMIT 1,1);
SET @UserE_Post3 = (SELECT id FROM post WHERE user_id = @UserE LIMIT 2,1);

INSERT INTO comment (post_id, user_id, comment) VALUES
	(@UserA_Post1, @UserB, 'UserB comment on userA post 1'),
	(@UserA_Post1, @UserC, 'UserC comment on userA post 1'),
	(@UserA_Post1, @UserD, 'UserD comment on userA Post 1'),
	(@UserA_Post1, @UserE, 'UserE comment on userA Post 1'),

	(@UserB_Post1, @UserB, 'UserB comment on userB post 1'),
	(@UserB_Post1, @UserC, 'UserC comment on userB post 1'),
	(@UserB_Post2, @UserD, 'UserD comment on userB Post 2'),
	(@UserB_Post2, @UserE, 'UserE comment on userB Post 2'),
	(@UserB_Post3, @UserD, 'UserA comment on userB Post 3'),
	(@UserB_Post3, @UserE, 'UserC comment on userB Post 3'),

	(@UserC_Post1, @UserB, 'UserB comment on userC post 1'),
	(@UserC_Post1, @UserC, 'UserC comment on userC post 1'),
	(@UserC_Post1, @UserD, 'UserD comment on userC Post 1'),
	(@UserC_Post1, @UserE, 'UserE comment on userC Post 1');

SET @UserB_Comment = (SELECT id FROM comment WHERE user_id = @UserB);
SET @UserC_Comment = (SELECT id FROM comment WHERE user_id = @UserC);
SET @UserD_Comment = (SELECT id FROM comment WHERE user_id = @UserD);
SET @UserE_Comment = (SELECT id FROM comment WHERE user_id = @UserE);

INSERT INTO favorite (post_id, user_id) VALUES
	(@UserA_Post1, @UserB),
	(@UserA_Post1, @UserC),
	(@UserA_Post1, @UserD),
	(@UserA_Post1, @UserE),
	(@UserB_Post2, @UserA),
	(@UserB_Post2, @UserC),
	(@UserB_Post2, @UserD),
	(@UserB_Post2, @UserE);

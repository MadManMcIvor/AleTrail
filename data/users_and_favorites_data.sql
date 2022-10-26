DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id SERIAL NOT NULL UNIQUE,
    first VARCHAR(30) NOT NULL,
    last VARCHAR(30) NOT NULL,
    profile_pic TEXT,
    email TEXT NOT NULL UNIQUE,
    username VARCHAR(20) NOT NULL UNIQUE,
    password TEXT NOT NULL,
    is_brewery_owner BOOLEAN DEFAULT FALSE
);

-- is_brewery_owner is a stretch goal 
-- the password is password 

INSERT INTO users VALUES
  (1, 'James', 'Smith', null, 'james@gmail.com', 'Jsmith', '$2b$12$dmCjJWYHBVDVQGdpW8Jn6ur0mZq9GT7XfJx0Ocl6xAxuRh4y/2unC', false),
  (2, 'David', 'Jones', null, 'david@gmail.com', 'Djones', '$2b$12$yLtujk.cPIgsphM0f1jEPOlm6nJ0L3gh.w7H4ERDSPDIO8gAuCBHK', false),
  (3, 'Patrick', 'Land', null, 'patrick@gmail.com', 'Patrick', '$2b$12$jYh.iRyR/E09Ka5NhPKCkucdnQJEpsyGK5jxC3HRZxdTPWvqF6RoO', false),
  (4, 'Abbie', 'Schmidt', null, 'abbie@gmail.com', 'Abbies', '$2b$12$.mWjCCHJS8upzdyahx7uU.y.TSNEfwJ8HW/F37nNDZ0vSCuXOWLfm', false),
  (5, 'Paul', 'Baker', null, 'paul@gmail.com', 'Pbaker', '$2b$12$I8N8ovWl/SLr0EcuoAxm5e9zg0xl7kClnFxl6ws.g0cyo2hCuv0Ge', false),
  (6, 'Susan', 'Anderson', null, 'susan@gmail.com', 'Susan', '$2b$12$/hfB5lpr1jh4tLztOZCizellgnWJGyLMvdmZ8bFdHh29CCbGnIudC', false),
  (7, 'Matt', 'Williams', null, 'matt@gmail.com', 'Matt', '$2b$12$0jsEnmDDTUsARj3Utta1geyc8YnwlRDWIPg0sv6Y8l6oTRQdPbcvG', false),
  (8, 'Zach', 'Gomez', null, 'zgomez@gmail.com', 'Zach', '$2b$12$dz9GSJks1T46bzrKkuP.ZOXWWQvzYM/o0ullOl9l26yY3RqBzScY2', false),
  (9, 'Will', 'Smith', null, 'will@gmail.com', 'Wsmith', '$2b$12$OweMtrSL1XY.wcwRCsY06.RNC41o64j/8X4C1WI/N.s1VJ.D.MZ9W', false),
  (10, 'Yuri', 'Miller', null, 'yuri@gmail.com', 'Ymiller', '$2b$12$yLtujk.cPIgsphM0f1jEPOlm6nJ0L3gh.w7H4ERDSPDIO8gAuCBHK', false)
  ;

SELECT setval('users_id_seq', (SELECT MAX(id) + 1 FROM users));

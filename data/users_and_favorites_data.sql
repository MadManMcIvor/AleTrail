DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id SERIAL NOT NULL UNIQUE,
    first VARCHAR(30) NOT NULL,
    last VARCHAR(30) NOT NULL,
    profile_pic TEXT,
    email TEXT NOT NULL UNIQUE,
    username VARCHAR(20) NOT NULL UNIQUE,
    password TEXT NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE,
    is_brewery_owner BOOLEAN DEFAULT FALSE
);


INSERT INTO users VALUES
  (1, 'James', 'Smith', null, 'James@gmail.com', 'Jsmith', 'password',false, false),
  (2, 'David', 'Jones', null, 'David@gmail.com', 'Djones', 'password', false, false),
  (3, 'Patrick', 'Land', null, 'Patrick@gmail.com', 'Patrick', 'password', false, false),
  (4, 'Abbie', 'Schmidt', null, 'Abbie@gmail.com', 'Abbies', 'password', false, false),
  (5, 'Paul', 'Baker', null, 'Paul@gmail.com', 'Pbaker', 'password', false, false),
  (6, 'Susan', 'Anderson', null, 'Susan@gmail.com', 'Susan', 'password', false, false),
  (7, 'Matt', 'Williams', null, 'Matt@gmail.com', 'Matt', 'password', false, false),
  (8, 'Zach', 'Gomez', null, 'ZGomez@gmail.com', 'Zach', 'password', false, false),
  (9, 'Will', 'Smith', null, 'Will@gmail.com', 'Wsmith', 'password', false, false),
  (10, 'Yuri', 'Miller', null, 'Yuri@gmail.com', 'Ymiller', 'password', false, false)
  ;


SELECT setval('users_id_seq', (SELECT MAX(id) + 1 FROM users));

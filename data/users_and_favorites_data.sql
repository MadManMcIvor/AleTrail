DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id SERIAL NOT NULL UNIQUE,
    first TEXT NOT NULL,
    last TEXT NOT NULL,
    profile_pic TEXT NULL,
    email TEXT NOT NULL UNIQUE,
    username TEXT NOT NULL UNIQUE,
);


INSERT INTO users VALUES
  (1, 'James', 'Smith', null, 'James@gmail.com', 'Jsmith'),
  (2, 'David', 'Jones', null, 'David@gmail.com', 'Djones',
  (3, 'Patrick', 'Land', null, 'Patrick@gmail.com', 'Patrick'),
  (4, 'Abbie', 'Schmidt', null, 'Abbie@gmail.com', 'Abbies'),
  (5, 'Paul', 'Baker', null, 'Paul@gmail.com', 'Pbaker'),
  (6, 'Susan', 'Anderson', null, 'Susan@gmail.com', 'Susan'),
  (7, 'Matt', 'Williams', null, 'Matt@gmail.com', 'Matt'),
  (8, 'Zach', 'Gomez', null, 'ZGomez@gmail.com', 'Zach'),
  (9, 'Will', 'Smith', null, 'Will@gmail.com', 'Wsmith'),
  (10, 'Yuri', 'Miller', null, 'Yuri@gmail.com', 'Ymiller')
  ;


SELECT setval('users_id_seq', (SELECT MAX(id) + 1 FROM users));

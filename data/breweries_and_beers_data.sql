DROP TABLE IF EXISTS breweries;
DROP TABLE IF EXISTS beers;

CREATE TABLE users_vo (
    users_vo_id SERIAL NOT NULL PRIMARY KEY,

);

CREATE TABLE breweries (
    brewery_id SERIAL NOT NULL PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    street VARCHAR(150) NOT NULL,
    city VARCHAR(150) NOT NULL,
    state VARCHAR(20) NOT NULL,
    zip_code INTEGER NOT NULL,
    phone VARCHAR(25) NULL,
    image_url VARCHAR(300) NULL,
    description TEXT NULL,
    website TEXT NULL
);

Add back later
owner_id INTEGER REFERENCES users("id") ON DELETE CASCADE



CREATE TABLE beers (
    beer_id SERIAL NOT NULL UNIQUE,
    name VARCHAR(150) NOT NULL,
    description TEXT NOT NULL,
    type VARCHAR(150) NOT NULL,
    ibu SMALLINT NOT NULL,
    abv FLOAT NOT NULL,
    brewery INTEGER NOT NULL REFERENCES breweries("brewery_id") ON DELETE CASCADE,
    image_url VARCHAR(300) NULL
);


INSERT INTO breweries VALUES
  (1, '10-56 Brewing Company', '400 Brown Cir', 'Sacramento', 'California', '46534', '6308165790', null, 'A brewery in Sacramento, California', null),
  (2, 'Big Sexy Brewing Company', '5861 88th St Ste 800', 'Sacramento', 'California', '95828', '9163747332', 'https://static.wixstatic.com/media/317ec9_55fb53d685e94e209ec42b88e77d43f9~mv2.png/v1/fill/w_241,h_83,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/Logo%20Dark%20Gray.png', 'A brewery in Sacramento, California', 'http://www.bigsexybrewing.com'),
  (3, '10 Barrel Brewing Co', '62970 18th St', 'Bend', 'Oregon', '97701', '5415851007', 'https://10barrel.com/wp-content/themes/mx-theme/assets/img/logo-retina-white.png', 'A brewery in Bend, Oregon', 'https://10barrel.com/'),
  (4, 'Shade Tree Brewing', '19305 Indian Summer Rd', 'Bend', 'Oregon', '97702', '6308165790', 'https://static.wixstatic.com/media/26a5bf_f8545c3c33884448a499103a490c0b70~mv2.png/v1/fill/w_217,h_158,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/26a5bf_f8545c3c33884448a499103a490c0b70~mv2.png', 'A brewery in Bend, Oregon', 'https://www.shadetreebrewing.com/')
  ;

INSERT INTO beers VALUES
(1, 'Batman Stout', 'A stout as dark as the dark knight himself!', 'Stout', 70, 5.11, 1, 'https://images.pexels.com/photos/5659755/pexels-photo-5659755.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'),
(2, '805 Pale Ale', 'Our flagship beer, perfectly balanced mix of malty and hoppy', 'Pale Ale', 80, 5.21, 1, 'https://images.pexels.com/photos/5530264/pexels-photo-5530264.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'),
(3, 'Orange Dream Sour', 'A farmhouse sour with hints of local oranges', 'Sour', 19, 6.50, 1, 'https://images.pexels.com/photos/1269025/pexels-photo-1269025.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'),
(4, 'Batman Stout', 'A stout as dark as the dark knight himself!', 'Stout', 70, 5.11, 2, 'https://images.pexels.com/photos/5659755/pexels-photo-5659755.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'),
(5, '805 Pale Ale', 'Our flagship beer, perfectly balanced mix of malty and hoppy', 'Pale Ale', 80, 5.21, 2, 'https://images.pexels.com/photos/5530264/pexels-photo-5530264.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'),
(6, 'Orange Dream Sour', 'A farmhouse sour with hints of local oranges', 'Sour', 19, 6.50, 2, 'https://images.pexels.com/photos/1269025/pexels-photo-1269025.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1')
;


SELECT setval('breweries_id_seq', (SELECT MAX(id) + 1 FROM breweries));
SELECT setval('beers_id_seq', (SELECT MAX(id) + 1 FROM beers));


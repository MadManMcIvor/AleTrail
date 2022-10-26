DROP TABLE IF EXISTS brewery_favorites;
DROP TABLE IF EXISTS beer_favorites;
DROP TABLE IF EXISTS beers;
DROP TABLE IF EXISTS breweries;
DROP TABLE IF EXISTS users_vo;

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

CREATE TABLE beers (
    beer_id SERIAL NOT NULL UNIQUE,
    name VARCHAR(150) NOT NULL,
    description TEXT NULL,
    type VARCHAR(150) NOT NULL,
    ibu SMALLINT NOT NULL,
    abv FLOAT NOT NULL,
    brewery INTEGER NOT NULL REFERENCES breweries("brewery_id") ON DELETE CASCADE,
    image_url VARCHAR(300) NULL,
    category VARCHAR(300) NULL,
    vegetarian_friendly VARCHAR(300) NULL
);


INSERT INTO breweries VALUES
  (1, 'Urban Roots', '123 Address St', 'Sacramento', 'California', '95818', '1234567890', 'https://images.squarespace-cdn.com/content/v1/59f24aa4f6576e1429b2de74/1592518376365-T83Z909WWTAZGW1TP1YX/MURALFINAL.png?format=2500w', 'A brewery in Sacramento, California', 'https://www.urbanrootsbrewing.com/'),
  (2, '10-56 Brewing Company', '400 Brown Cir', 'Sacramento', 'California', '95818', '6308165790', 'https://images.getbento.com/accounts/297e701e99e7e970d84246275554d4d2/media/images/98499logo.png?w=600&fit=max&auto=compress,format&h=600', 'The coolest brewery in town!', 'https://www.1056brew.com/'),
  (3, 'Big Sexy Brewing Company', '5861 88th St Ste 800', 'Sacramento', 'California', '95828', '9163747332', 'https://static.wixstatic.com/media/317ec9_55fb53d685e94e209ec42b88e77d43f9~mv2.png/v1/fill/w_241,h_83,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/Logo%20Dark%20Gray.png', 'A brewery in Sacramento, California', 'http://www.bigsexybrewing.com'),
  (4, '10 Barrel Brewing Co', '62970 18th St', 'Sacramento', 'California', '95816', '5415851007', 'https://images.squarespace-cdn.com/content/v1/59f24aa4f6576e1429b2de74/1596055239397-TRV4ZEAB9QLXKQKZKIX7/Bar_2_ec352d8101fbac532d83880aded0acc1.jpg?format=2500w', 'A brewery in Sacramento, California', 'https://10barrel.com/'),
  (5, 'Shade Tree Brewing', '19305 Indian Summer Rd', 'Sacramento', 'California', '95822', '6308165790', 'https://static.wixstatic.com/media/26a5bf_f8545c3c33884448a499103a490c0b70~mv2.png/v1/fill/w_217,h_158,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/26a5bf_f8545c3c33884448a499103a490c0b70~mv2.png', 'A brewery in Sacramento, California', 'https://www.shadetreebrewing.com/'),
  (6, 'Alaro Craft Brewing', '2004 Capitol Ave', 'Sacramento', 'California', '95822', '9162340121', 'https://alarobrewing.com/wp-content/uploads/2022/02/IMG_8416.webp', 'A brewery in Sacramento, California', 'https://alarobrewing.com/'),
  (7, 'Device Brewing', '4432 V St', 'Sacramento', 'California', '95822', '9162340121', 'https://images.squarespace-cdn.com/content/v1/5126cb48e4b08a68a4373d68/1664303212311-QFNHGFRWSWWIJC53GNG0/20220811-_DSC8697-Edit-2.jpg', 'A brewery in Sacramento, California', 'http://devicebrewing.com/')
  ;

INSERT INTO beers VALUES
(1, 'Batman Stout', 'A stout as dark as the dark knight himself!', 'Stout', 70, 5.11, 1, 'https://images.pexels.com/photos/1796698/pexels-photo-1796698.jpeg?cs=srgb&dl=pexels-helena-lopes-1796698.jpg&fm=jpg', 'Stout', 'True'),
(2, '805 Pale Ale', 'Our flagship beer, perfectly balanced mix of malty and hoppy', 'Pale Ale', 80, 5.21, 1, 'https://images.pexels.com/photos/5530264/pexels-photo-5530264.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 'Ale', 'True'),
(3, 'Orange Dream Sour', 'A farmhouse sour with hints of local oranges', 'Sour', 19, 6.50, 1, 'https://images.pexels.com/photos/1269025/pexels-photo-1269025.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 'Sour', 'True'),
(4, 'Flooster', 'German Hefeweizen', 'Wheat Ale', 70, 5.11, 2, 'https://images.pexels.com/photos/1269043/pexels-photo-1269043.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 'Stout', 'True'),
(5, 'EZ PZ', 'A Dry hopped czech-style lager.', 'Pilzner', 40, 4.78, 2, 'https://images.pexels.com/photos/995686/pexels-photo-995686.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 'Ale', 'True'),
(6, 'Luna de Miel', 'A perfectly balanced Mexican lager', 'Lager', 19, 4.50, 2, 'https://images.pexels.com/photos/669213/pexels-photo-669213.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 'Sour', 'True'),
(7, 'Pause for Sunset', 'A Fruited Sour ale', 'Sour', 40, 7.11, 3, 'https://images.pexels.com/photos/969944/pexels-photo-969944.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 'Ale', 'True'),
(8, 'Flavor Chaser', 'An entire crop of hops in one beer.', 'West Coast IPA', 40, 5.91, 4, 'https://images.pexels.com/photos/1269040/pexels-photo-1269040.jpeg?cs=srgb&dl=pexels-elevate-1269040.jpg&fm=jpg', 'Ale', 'True')
;

CREATE TABLE brewery_favorites (
    brewery_favorite_id SERIAL PRIMARY KEY NOT NULL,
    user_id  INTEGER NOT NULL,
    brewery_id INTEGER NOT NULL REFERENCES breweries("brewery_id") ON DELETE CASCADE
);

CREATE TABLE beer_favorites (
    beer_favorite_id SERIAL PRIMARY KEY NOT NULL,
    user_id  INTEGER NOT NULL,
    beer_id INTEGER NOT NULL REFERENCES beers("beer_id") ON DELETE CASCADE
);

INSERT INTO brewery_favorites VALUES
  (1, 2, 2),
  (2, 2, 3),
  (3, 2, 1)
  ;

INSERT INTO beer_favorites VALUES
  (1, 2, 2),
  (2, 2, 3),
  (3, 2, 1)
  ;


SELECT setval('breweries_brewery_id_seq', (SELECT MAX(brewery_id) + 1 FROM breweries));
SELECT setval('beers_beer_id_seq', (SELECT MAX(beer_id) + 1 FROM beers));
SELECT setval('brewery_favorites_brewery_favorite_id_seq', (SELECT MAX(brewery_favorite_id) + 1 FROM brewery_favorites));
SELECT setval('beer_favorites_beer_favorite_id_seq', (SELECT MAX(beer_favorite_id) + 1 FROM beer_favorites));


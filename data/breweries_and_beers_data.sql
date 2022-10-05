DROP TABLE IF EXISTS breweries;
DROP TABLE IF EXISTS beers;

CREATE TABLE breweries (
    brewery_id SERIAL NOT NULL UNIQUE,
    name TEXT NOT NULL,
    last TEXT NOT NULL,
    avatar TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    username TEXT NOT NULL UNIQUE,
    referrer_id INTEGER REFERENCES users("id") ON DELETE CASCADE
);

CREATE TABLE beers (
    id SERIAL NOT NULL UNIQUE,
    name TEXT NOT NULL,
    website TEXT NOT NULL,
    category TEXT NOT NULL check(category = 'American' or category = 'Asian' or category = 'French' or category = 'Mediterranean' or category = 'Indian' or category = 'Italian' or category = 'Latin'),
    vegetarian_friendly BOOLEAN NOT NULL,
    owner_id INTEGER NOT NULL REFERENCES users("id") ON DELETE CASCADE
);


INSERT INTO trucks VALUES
  (1, 'Trucky', 'https://trucky.com', 'American', true, 1),
  (2, 'Necks', 'https://necks.com', 'Mediterranean', true, 2),
  (3, '100% Human Food', 'https://humanfood.com', 'French', false, 2),
  (4, 'Questionably Low Cost', 'https://epa.gov', 'Mediterranean', true, 3),
  (5, 'B-b-bistro', 'https://b-b-b-bitro.com', 'Italian', true, 3),
  (6, 'NaN Naan', 'https://nan-naan.net', 'Indian', true, 4),
  (7, 'White Cheese Queso', 'https://queso-white-cheese.com', 'Latin', false, 4),
  (8, 'Delicious Burgers', 'https://delicious-burgers.com', 'American', false, 4),
  (9, 'Quantifiable Flavor', 'https://delicious-burgers.com', 'American', false, 4),
  (10, 'Dumpling in French Onion Soup', 'https://dumplingsoup.com', 'French', true, 1),
  (11, 'Hello World', 'https://example.com', 'Italian', false, 1)
  ;



SELECT setval('users_id_seq', (SELECT MAX(id) + 1 FROM users));
SELECT setval('trucks_id_seq', (SELECT MAX(id) + 1 FROM trucks));
SELECT setval('menu_items_id_seq', (SELECT MAX(id) + 1 FROM menu_items));
SELECT setval('reviews_id_seq', (SELECT MAX(id) + 1 FROM reviews));

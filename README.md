
# AleTrail 

A single-page application for finding local breweries and beers.

---
## Table of Contents
- [AleTrail](#aletrail)
  - [Table of Contents](#table-of-contents)
  - [Members](#members)
  - [Deployed application](#deployed-application)
  - [Intended market](#intended-market)
  - [Functionality](#functionality)
  - [Project Initialization (locally)](#project-initialization-locally)
  - [Design](#design)
    - [Data Models:](#data-models)
    - [Wireframe:](#wireframe)

---

## Members
* Ryan Spurlock
* Alex Mclvor
* Justin Thomas
* Julie Liao

---

## Deployed application 
Website: https://aletrail.gitlab.io/ale-trail-alpha/

---
## Intended market
This app is designed to allow users to find breweries and beers from those breweries in their local area. The users can also add breweries and beers to their favorites list after making an account so they can view their list of favorites later.

---
## Functionality 
- Visitors to the site can view local breweries and beers 
- On the breweries page visitors/ users can click to view detail of a brewery.
- The detail view displays the address of that brewery
- On the beers page visitors/ users can click to view the description of a beer. 
- Users can create an account, login, and logout. The view of the website changes based on if user is logged in or not.
- Users would have to create an account to use favorites function to keep track of favorite breweries or beers 
- Users can add to favorites or remove from favorites by clicking on the star icon on a beer or brewery.

---
## Project Initialization (locally)
1. Git clone this repository into your local computer 
2. CD into ale-trail-alpha directory
3. Run `docker volume create postgres-data`
4. Run `docker volume create pg-admin`
5. Run `docker-compose build`
6. Run `docker-compose up`
7. Using either PGAdmin or BeeKeeper, seed the databases - users and (breweries and beers) - by making a query with the data in the sql files in the data directory

- Access application on browser at localhost:3000
- Access FastAPI Swagger UI:
  - breweries, beers, and favorites services on localhost:8090/docs
  - users service on localhost:8100/docs 

---

## Design 
This is a single-page application using a React front-end making RESTful API calls to two FastAPI back-end microservices. 

- [API design](/docs/api-design.md)

---
### Data Models:
Breweries:
![Breweries Data Model](/readme_images/breweries_data_model.png)
Beers:
![Beers Data Model](/readme_images/beers_data_model.png)
Users:
![Users Data Model](/readme_images/users_data_model.png)
Breweries Favorites:
![Brewery Favorites Data Model](/readme_images/brewery_favorites_data_model.png)
Beer Favorites:
![Beer Favorites Data Model](/readme_images/beer_favorites_data_model.png)

---
### Wireframe:
![Wire diagram / GHI](/readme_images/Aletrail-wire-diagram.png)

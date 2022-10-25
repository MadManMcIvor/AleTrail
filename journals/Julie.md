## 10/24/22
Merged user test into main. Merged hide and view password function in login page into main. Worked with Alex and made changes to docker-compose.yaml file. 

## 10/20/22 
Today I continued working on unit test. I'm able to get the tests to pass locally, but the tests won't pass on gitlab because the database is not set up on the actual site yet. 

## 10/19/22
Today I worked on writing unit test for users. When I ran the pytest, I got a test failed with 401 error and realized I need to include the token as part of the test. I'm still trying to figure out how to include it in the test for it to pass. 

## 10/18/22 
This morning I did pair programming with Alex and was able to get the error message pop up when trying to create an account with the same email. I was able to hide the favorites page by having the page redirects to login page if there's no token. 

## 10/17/22
Today I did pair programming with Alex. We were able to get the signup page and login page with token to work. We're created a logout modal with pop up confirming logout. 

## 10/14/22 
Today I created the layout for the signup form. I'm still trying to figure out how to implement authentication for the front end while using the functional based component. 

## 10/13/22
Today I discussed with teammates and decided the is_brewery_owner is going to be a stretch goal. I modified the models and tested to make sure nothing is broken, unfortunately I got an error message. I was debugging and finally found that I did not remove %s from one of the endpoint. I'm going to start on the react signup page. 

## 10/12/22
Today I asked for feedback from teammates and removed is_admin from the users table database. The testing data in the database is updated to have hashed password. After the changes, I deleted and rebuild the volume to test the database to make sure nothing is broken. Fixed more endpoints to be protected. 

## 10/11/22
Today I created a signing key and continued to make corrections on the users endpoint because after adding the authentication, the swagger endpoints didn't work correctly. 

## 10/10/22 
The endpoints for users CRUD works, but I need to include password. Today I continued working on my endpoints and made changes to the table to include password, is_admin, and is_brewery_owner. After the changes to the table, I can focus on authentication and testing out all the endpoint requests.  

## 10/6/22 
Today we tested our data in our database and set up beekeeper. I continued working on users routers and queries. Made changes to the user database. I'm going to read the docs/ watch video on authentication. 

## 10/5/22
Today we made changes to the docker-compose.yaml files so we can work on local development. We decided that we want to use PostgreSql for our database and have pgAdmin setup. We worked on creating some database so we can test locally. 

## 10/4/22
We finished drafting our API endpoints and re-evaluate our MVP and made changes to have some features as stretch goals. We decided to have brewery, beers, favorites, and users as our MVP. Reviews as a stretch goal. We divided tasks for each member and wrote issues on gitlab. I decided to work on the users endpoints. 

## 10/3/22
* We continued working on the API endpoints and discussed the possible href and what to include for each CRUD view. Heroku site is running and shows under construction. 

## 9/30/22
* We asked for about pipeline failed and clarification on issues and whether the issue is for each page or each feature of the page. We haven't decide on what database to use. Postgre, SQL, or MongoDB. We saw the exploration is going to be on FASTAPI and SQL and decided we can think about it over the weekend. 

## 9/29/22
* We worked on endpoints and decided on the response shape 
* Cloned project and we followed the directions on live channel for deploying the project. We're weren't sure about step 2 Heroku Variables: CORS_HOST so we asked a SEIR for help.

## 9/28/22
* We continued working on the wireframe and discussed what to include in the MVP.Authentication, brewery list page with detail card, beer list page with detail cards, and user profile page with list view of their favorite breweries and beers. Stretch Goals: add a brewery request form, add a beer request form, add a map that displays breweries and distance from them, add a taste profile to recommend beers, and add challenges and badges to user profiles.

## 9/27/22 
* We worked on wireframe for our app using excalidraw. We discussed what features and designs we want on the webpage. We also decided AleTrail going to be our group name.

## 9/26/22
* We discussed what our project is going to be. In the end we decided on a brewery app where people can see a list of brewery in their city and keep track of their favorite drinks. 

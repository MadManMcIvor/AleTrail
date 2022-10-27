## 10/27/22
* Justin, Julie, and I worked with Andrew to help figure out the issue on the frontend authentication. We figured it out finally. It was an error with the token since it was coming from a different domain. We had to switch the fetch from including credentials to using headers bearer token.
* Worked as a group on the readme and cleaning up the project.

## 10/26/22
* Made a separate Heroku app for the users. Linked up everything on the gitlab ci yml file and made all the necessary corrections. Got it deployed successfully!!!!!! 

* I tweaked some of the seed data so it’s looks better on the website. Also, added the data to our Heroku’s data base so it created the tables and has data there.

* Julie, Justin, and I worked on a bug for the rest of the day. The favoriting is having authentication issues on the deployed site, but not locally and we can’t figure it out!

## 10/25/22 
* Had a bug arise that was really odd. The same code that was passing test yesterday wasn’t passing today. After a few hours of troubleshooting we figure it out. We needed to remove the ‘binary’ from the pyscopg requirements.
* Worked on deployment the rest of the day

## 10/24/22 
* Helped Justin on a frontend issue. He was having trouble trying to get the favorites to register on the breweries page so that they’d show a star that’d be lit up. Worked on that for about an hour or so before he got it working. 

* Then I worked with Julie on cleaning up the project a bit and working on gitlab CI stuff. We got the deployment mostly working, I think. Or at least the pipelines didn’t break. We still need to add data via beekeeper directly to the data base.

## 10/21/22
* got my unit test working.

## 10/20/22
* Moved my mock data over from the users and favorites file to the beers and breweries file, fixed a bug in the create brewery favorite endpoint, and tweaked some of the beers models so they more accurately match what we were looking for.
* Started on my unit test for the favorites back end.

## 10/19/22 
* Finished creating end points for beer and brewery favorites (create, delete, view favorites by user)

## 10/18/22
* We fixed the pop up for the signup page error modal.
* Made the logout modal actually log the user out and redirect them afterwards.
* Started working on the favorites FastAPI ends points

## 10/17/22
* Pair programmed with Julie all day. We set up the signup page, the login page, and the logout page on the front end. We made modals for the logout, and error messages when attempting to login or signup. It took a long time to figure out how to integrate the features, but feels like we're in a good place now.

## 10/14/22
* Linked up the brewery list API to the front-end and deleted the dummy data.

## 10/13/22
* Worked on the Navbar today. I switched it over to a react-bootstrap component rather than just the regular bootstrap how it was. I also added our logo and switched it be white. It took quite a while to figure out why the image wouldn't display for the logo. Turns out React gives it problems so I had to wrap it in a 'required' function.

## 10/12/22
* We figured out how to make merge requests and implemented a few of those.
* Fixed the beers carousels
* Added modals for both beers and breweries

## 10/11/22
* Imported the react-bootstrap library and got the masonry to work on the breweries page.
* Imported a react-carousel library and created some of the components for the beers page. I've mostly got it working but I'm still tweaking it though. 

## 10/10/22
* Transformed the existing "under construction" React into the skeleton for our project. Played with a few different attempts to make masonry work on the breweries page"

## 10/6/22
* Created the tables and dummy data for breweries and beers with Justin. Did some live share for the first time. Also, got Beekeeper up and running.

## 10/5/22
* We decided on using PostgreSQL as our database as opposed to MongoDB
* We worked as a team to get our docker compose file up and working for local development.
* Started to create a data file so we can create the tables and some dummy data for the end points to grab when we dive into them

## 10/4/22
* Reworked our APIs Doc as a team to reflect a re-scope MVP - we're just going to do breweries, beers, favorites, and users. Making reviews a stretch goal if we can get to it.
* We each created our own issues to get us started and figure out our roles. I'm taking the React/frontend side of the project to start
* We got the main project up to speed so everyone can create branches with all of the technical nitty gritty up to date.

## 10/3/22 
Got front end and Heroku working, finished the API list

## 9/30/22  
Discussed API, Issues, DB strategy

## 9/29/22
Worked on the API document. Worked on deploying the project to Heroku

## 9/28/22  
Worked as a group on the wireframe for the site in Excalidraw

## 9/27/22 
Worked as a group on the wireframe for the site in Excalidraw

## 9/26/22 
Brainstormed the ideas and landed on the brewery idea

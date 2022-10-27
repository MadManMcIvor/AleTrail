## 10/27/22 
Worked with Alex and Julie in continuing to troubleshoot the authorization problem on the deployed server. We got the issue resolved. We collectively updated the readme, and are looking for answers on linting expectations. 

## 10/26/22 
Added a ternary operator to nav to display or hide nav elements depending if a user is logged in or not. I fixed a bug where users without any favorites could not add to their favorites. Cleaned up unused console.logs. Star icons were no longer loading on deployed server. Changed their file location and added js require function.

Spent the later half of class helping Alex and Julie troubleshoot the issue with beer and brewery endpoints not being authorized on the deployed server despite it working locally. 


## 10/25/2022
Fixed a bug where favorites was not correctly displaying if a brewery was favorite for every user. It was a hardcoded for a certain user, so i passed in the props from the parent component. Cleaned up some console.logs that were no longer needed, added unique keys to divs, and added more logic to add user ids and if favorite to brewery and beer states.

## 10/24/2022
Worked on getting the favorite button in breweries to correctly reflect if a brewery is a favorite or not. Added favorites endpoints to the favorite component.


## 10/20/22
Discussed with team about project MVP, deadline, and favorites endpoint. Helped point out and resolve bug with favorites endpoint by working with Alex. Discussed taking away favourites star and replacing it with text that just adds to favorite. A user will be able to remove from favorites in favorites tab. Plan to get this implemented over the weekend and have MVP ready by monday. 

## 10/19/22
Continued working on implementing favorite icons and got it prepped for end points. Cleaned up breweries of unused functions, variables, and imports.

## 10/18/22
Added a favorites icon to brewerycardmodal and beercardmodal to use with favorites endpoints ocne they are donw. Finished implementing brewery unit test into yml file. 

## 10/17/22
Created a test that needs to be implemented into yml file. Added authentication for breweries PUT, POST, and DELETE methods.

## 10/14/22
Worked on adding a list of beers associated with a brewery when using brewery API endpoints.

## 10/13/22
Added Update endpoint and an endpoint to get a brewery by specific city. Need to go back and update every endpoint to join the beer table for a list of beers that have the brewery id.

## 10/12/22
Got most CRUD functions working and merged with main except update. Need to create an endpoint for updating a brewery, and need to update GET functions to include a list of all beers for that brewery.

## 10/11/22
Got a functioning GET request for all breweries. Working now to POST request to create a brewery and GET request for a specific brewery. Will need to add a way to filter by city and add in associated beer tables later.

## 10/10/22
Worked on setting up backend for breweries

## 10/5/22
Configured YAML file for each microservice, got docker up and running, added pgadmin

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

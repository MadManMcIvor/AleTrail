import Masonry from 'react-masonry-css'
import BreweryCard from './BreweryCard';
import React, { useEffect, useState } from 'react';

function Breweries() {
  const [breweries, setBreweries] = useState([])
  const [breweryFavs, setBreweryFavs] = useState([])

  // add breweries to state
  useEffect(() => {
    async function getBreweryFavs() {
      const url = `${process.env.REACT_APP_BREWERIES_AND_BEERS_API_HOST}/favorites/breweries`
      const response = await fetch(url, { method: "GET", credentials: "include" });
      if (response.ok) {
        const data = await response.json();
        setBreweryFavs(Array.from(data));
      }
    }

    async function getBreweries() {
      const url = `${process.env.REACT_APP_BREWERIES_AND_BEERS_API_HOST}/breweries`
      const response = await fetch(url);
      if (response.ok) {
        const data = await response.json();
        let formattedData = [];
        data.breweries.map((obj) => {
          return formattedData.push(obj);
        });
        setBreweries(formattedData);
      }
    }

    function addFavsToBreweries() {
      // creates a list of all brewery_ids in Favorite Breweries
      let favs = [];
      for(let i = 0; i < breweryFavs.length; i++){
        if(!(breweryFavs[i]["brewery_id"] in favs)){
          favs.push(breweryFavs[i]["brewery_id"])
        }
      }
      // compares brewery id to list of brew. ids from favorites and add true or false to object depending if in list or not
      for(let i = 0; i < breweries.length; i++){
        if(favs.includes(breweries[i]["brewery_id"])){
          breweries[i]["fav"] = true;
        }else{
          breweries[i]["fav"] = false;
        }
      }
      
    };

    getBreweryFavs();
    getBreweries();
    addFavsToBreweries();
    console.log(breweries);
  }, []);

      // Convert breweries in state to brewery cards
      let breweryCards = breweries.map(function(brewery) {
        return <div key={brewery.brewery_id}>
            <BreweryCard 
            brewery_id = {brewery.brewery_id}
            name = {brewery.name}
            street = {brewery.street}
            city = {brewery.city}
            state = {brewery.state}
            zip_code = {brewery.zip_code}
            phone = {brewery.phone}
            image_url = {brewery.image_url}
            description = {brewery.description}
            website = {brewery.website}
            fav = {brewery.fav}
            />
            </div>
      });

      // create the breakpoint for adjusting columns based on viewport size
      const breakpointColumnsObj = {
        default: 4,
        1100: 3,
        700: 2,
        500: 1
      };

      return (
        <div>
            <h1 className="display-1">Breweries!</h1>
            <Masonry
                breakpointCols={breakpointColumnsObj}
                className="my-masonry-grid"
                columnClassName="my-masonry-grid_column">
               {breweryCards}
            </Masonry>
        </div>
        
    )
}

export default Breweries;
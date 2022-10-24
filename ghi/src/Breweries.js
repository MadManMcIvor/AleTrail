import Masonry from 'react-masonry-css'
import BreweryCard from './BreweryCard';
import React, { useEffect, useState } from 'react';

function Breweries() {
  const [breweries, setBreweries] = useState([])

  async function addFavsToBreweries(brew, favData) {
    // creates a list of all brewery_ids in Favorite breweries
    let favs = [];
    for(let i = 0; i < favData.length; i++){
      if(!(favData[i]["brewery_id"] in favs)){
        favs.push(favData[i]["brewery_id"]);
      };
      console.log("FAVS", favs)
    };
    // compares brewery id to list of brew. ids from favorites and add true or false to object depending if in list or not
    for(let i = 0; i < brew.length; i++){
      if(favs.includes(brew[i]["brewery_id"])){
        brew[i]["fav"] = 1;
      }else{
        brew[i]["fav"] = 0;
      };
    };
    setBreweries(brew);
  };

  // add breweries to state
  useEffect(() => {

    async function getBreweries() {
      let favData = [];
      const favUrl = `${process.env.REACT_APP_BREWERIES_AND_BEERS_API_HOST}/favorites/breweries`
      const favResponse = await fetch(favUrl, { method: "GET", credentials: "include" });
      if (favResponse.ok) {
        const data = await favResponse.json();
        favData = Array.from(data);
      };
      const url = `${process.env.REACT_APP_BREWERIES_AND_BEERS_API_HOST}/breweries`
      const response = await fetch(url);
      if (response.ok) {
        const data = await response.json();
        let formattedData = [];
        data.breweries.map((obj) => {
          return formattedData.push(obj);
        });
        addFavsToBreweries(formattedData, favData);
        };
    };

    getBreweries();
  }, []);
  
  console.log("BREWERIES", breweries);
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
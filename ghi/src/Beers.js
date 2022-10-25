import Masonry from 'react-masonry-css'
import BeerCard from './BeerCard';
import React, { useEffect, useState } from 'react';

function Beers() {
    const [beers, setBeers] = useState([])

    async function addFavsToBeers(brew, favData) {
      // creates a list of all brewery_ids in Favorite breweries
      if(favData.length > 0){
        let favs = [];
        const user_id = favData[0]["user_id"]
        for(let i = 0; i < favData.length; i++){
          if(!(favs.includes(favData[i]["beer_id"]))){
            favs.push(favData[i]["beer_id"]);
          };
        };
        // compares brewery id to list of brew. ids from favorites and add true or false to object depending if in list or not
        for(let i = 0; i < brew.length; i++){
          if(favs.includes(brew[i]["beer_id"])){
            brew[i]["fav"] = 1;
            brew[i]["user_id"] = user_id;
          }else{
            brew[i]["fav"] = 0;
            brew[i]["user_id"] = user_id;
          };
        };
        setBeers(brew);
      }else{
        setBeers(brew);
      };
    };

  useEffect(() => {
    async function getBeers() {
      let favData = [];
      const favUrl = `${process.env.REACT_APP_BREWERIES_AND_BEERS_API_HOST}/favorites/beers`
      const favResponse = await fetch(favUrl, { method: "GET", credentials: "include" });
      if (favResponse.ok) {
        const data = await favResponse.json();
        favData = Array.from(data);
        
      };
      const url = `${process.env.REACT_APP_BREWERIES_AND_BEERS_API_HOST}/beers`
      const response = await fetch(url);
      let formattedData = [];
      if (response.ok) {
        const data = await response.json();
        data.beers.map((obj) => {
          return formattedData.push(obj);
        });
        addFavsToBeers(formattedData, favData);
      }else{
        setBeers(formattedData);
      };
    };

    getBeers();
  }, [])

  let beerCards = beers.map(function(beer) {
    return <div key={beer.beer_id}>
        <BeerCard 
        beer_id = {beer.beer_id}
        name = {beer.name}
        description = {beer.description}
        type = {beer.type}
        ibu = {beer.ibu}
        abv = {beer.abv}
        brewery = {beer.brewery}
        image_url = {beer.image_url}
        category = {beer.category}
        vegetarian_friendly = {beer.vegetarian_friendly}
        fav = {beer.fav}
        user_id = {beer.user_id}

        />
        </div>
  });
  
  const breakpointColumnsObj = {
    default: 4,
    1100: 3,
    700: 2,
    500: 1
  };
    
    return (
      <div>
          <h1 className="display-1">Beers!</h1>
          <Masonry
              breakpointCols={breakpointColumnsObj}
              className="my-masonry-grid"
              columnClassName="my-masonry-grid_column">
             {beerCards}
          </Masonry>
      </div>
      
  )
}
export default Beers;

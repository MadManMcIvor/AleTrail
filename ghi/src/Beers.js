import Masonry from 'react-masonry-css'
import BeerCard from './BeerCard';
import React, { useEffect, useState } from 'react';

function Beers() {
    const [beers, setBeers] = useState([])



  useEffect(() => {
    async function getBeers() {
      const url = `${process.env.REACT_APP_BREWERIES_AND_BEERS_API_HOST}/beers`
      const response = await fetch(url);
      if (response.ok) {
        const data = await response.json();
        let formattedData = [];
        data.beers.map((obj) => {
          return formattedData.push(obj);
        });
        setBeers(formattedData);
      }
    }
    getBeers();
  }, [])

  let beerCards = beers.map(function(beer) {
    return <div>
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

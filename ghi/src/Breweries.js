import Masonry from 'react-masonry-css'
import BreweryCard from './BreweryCard';
import React, { useEffect, useState } from 'react';

function Breweries() {
  const [breweries, setBreweries] = useState([])

  // add breweries to state
  useEffect(() => {
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
    getBreweries();
  }, [])

      // Convert breweries in state to brewery cards
      let breweryCards = breweries.map(function(brewery) {
        return <div>
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
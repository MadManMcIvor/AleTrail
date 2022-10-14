import Masonry from 'react-masonry-css'
import BreweryCard from './BreweryCard';
import React, { useEffect, useState } from 'react';

function Breweries() {
  const [breweries, setBreweries] = useState([])

  useEffect(() => {
    async function getBreweries() {
      const url = '${process.env.REACT_APP_API}/breweries'
      const response = await fetch(url);
      if (response.ok) {
        const data = await response.json();
        setBreweries(data);
      }
    }
    getBreweries();
  }, [])

      // Convert array to JSX items
      // breweries = breweries.map(function(brewery) {
      //   return <div>
      //       <BreweryCard 
      //       brewery_id = {brewery.brewery_id}
      //       name = {brewery.name}
      //       street = {brewery.street}
      //       city = {brewery.city}
      //       state = {brewery.state}
      //       zip_code = {brewery.zip_code}
      //       phone = {brewery.phone}
      //       image_url = {brewery.image_url}
      //       description = {brewery.description}
      //       website = {brewery.website}
      //       />
      //       </div>
      // });

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
                {breweries}
            </Masonry>
        </div>
        
    )
}

export default Breweries;
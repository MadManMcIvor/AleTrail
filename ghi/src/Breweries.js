import Masonry from 'react-masonry-css'
import BreweryCard from './BreweryCard';
import React, { useEffect, useState } from 'react';
import { useToken } from './LoginToken';

function Breweries() {
  const [breweries, setBreweries] = useState([])
  const [token] = useToken()

  async function addFavsToBreweries(brew, favData) {
    let user_id = null;
    const url = `${process.env.REACT_APP_USERS_AND_FAVORITES_API_HOST}/token`;
    try {
        const response = await fetch(url, {
            credentials: "include",
        });
        if (response.ok) {
            const data = await response.json();
            user_id = data.user.id;
        };
    }catch(error){
        console.log(error)
    }
    if(favData.length > 0){
      let favs = [];
      const user_id = favData[0]["user_id"]
      for(let i = 0; i < favData.length; i++){
        if(!(favs.includes(favData[i]["brewery_id"]))){
          favs.push(favData[i]["brewery_id"]);
        };
      };
      // compares brewery id to list of brew. ids from favorites and add true or false to object depending if in list or not
      for(let i = 0; i < brew.length; i++){
        if(favs.includes(brew[i]["brewery_id"])){
          brew[i]["fav"] = 1;
          brew[i]["user_id"] = user_id;
        }else{
          brew[i]["fav"] = 0;
          brew[i]["user_id"] = user_id;
        };
      };
      setBreweries(brew);
    }else{
      for(let i = 0; i < brew.length; i++){
        brew[i]["fav"] = 0;
        brew[i]["user_id"] = user_id;
      }
      setBreweries(brew);
    };
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
      let formattedData = [];
      if (response.ok) {
        const data = await response.json();
        data.breweries.map((obj) => {
          return formattedData.push(obj);
        });
        addFavsToBreweries(formattedData, favData);
      };
    };
    getBreweries();
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
            user_id = {brewery.user_id}
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
        <>
          <div className={token ? 'd-none' : 'alert alert-warning'} role="alert">
            Please log-in to favorite breweries
          </div>
          <div>
            <h1 className="display-1">Breweries!</h1>
            <Masonry
                breakpointCols={breakpointColumnsObj}
                className="my-masonry-grid"
                columnClassName="my-masonry-grid_column">
              {breweryCards}
            </Masonry>
          </div>
        </>
    )
}

export default Breweries;
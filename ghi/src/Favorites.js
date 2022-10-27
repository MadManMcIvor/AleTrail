import Carousel from "react-multi-carousel";
import "react-multi-carousel/lib/styles.css";
import BeerCard from './BeerCard';
import BreweryCard from './BreweryCard';
import React, { useEffect, useState } from 'react';
import { useToken } from './LoginToken';


function Favorites() {
    const [breweries, setBreweries] = useState([]);
    const [beers, setBeers] = useState([]);
    const [token] = useToken()

    useEffect(() => {
      async function getBreweries() {
        const url = `${process.env.REACT_APP_BREWERIES_AND_BEERS_API_HOST}/favorites/breweries`
        const response = await fetch(url, { method: "GET", headers: { Authorization: `Bearer ${token}` }});
        if (response.ok) {
          const data = await response.json();
          let formattedData = [];
          data.map((obj) => {
            return formattedData.push(obj);
          });
          setBreweries(formattedData);
        }
      }

        async function getBeers() {
            const url = `${process.env.REACT_APP_BREWERIES_AND_BEERS_API_HOST}/favorites/beers`
            const response = await fetch(url, { method: "GET", credentials: "include" });
            if (response.ok) {
              const data = await response.json();
              let formattedData = [];
              data.map((obj) => {
                return formattedData.push(obj);
              });
              setBeers(formattedData);
            }
          }     

        getBeers();
        getBreweries();
      }, [token])

    // Convert array to JSX items
    let beerCards = beers.map(function(beer) {
        return <div key={beer.beer_id}>
            <BeerCard 
            beer_id = {beer.beer_id}
            name = {beer.name}
            image_url = {beer.image_url}
            description = {beer.description}
            ibu = {beer.ibu}
            abv = {beer.abv}
            />
            </div>
    });

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
    
    
    const responsive = {
    desktop: {
        breakpoint: { max: 3000, min: 1024 },
        items: 3,
        slidesToSlide: 1 // optional, default to 1.
    },
    tablet: {
        breakpoint: { max: 1024, min: 464 },
        items: 2,
        slidesToSlide: 1 // optional, default to 1.
    },
    mobile: {
        breakpoint: { max: 464, min: 0 },
        items: 1,
        slidesToSlide: 1 // optional, default to 1.
    }
    };

    return(
        <>
            <h1>Favorites Beers!</h1>
            <div className='my-own-custom-container'>
                <Carousel
                swipeable={true}
                draggable={true}
                showDots={true}
                responsive={responsive}
                ssr={true} // means to render carousel on server-side.
                infinite={true}
                autoPlay={false}
                autoPlaySpeed={1000}
                keyBoardControl={true}
                customTransition="all .5"
                transitionDuration={500}
                containerClass="carousel-container"
                removeArrowOnDeviceType={["tablet", "mobile"]}
                dotListClass="custom-dot-list-style"
                itemClass="carousel-item-padding-40-px"
                >
                {beerCards}
                </Carousel>
            </div>
            <h1>Favorites Breweries!</h1>
            <div className='my-own-custom-container'>
                <Carousel
                swipeable={true}
                draggable={true}
                showDots={true}
                responsive={responsive}
                ssr={true} // means to render carousel on server-side.
                infinite={true}
                autoPlay={false}
                autoPlaySpeed={1000}
                keyBoardControl={true}
                customTransition="all .5"
                transitionDuration={500}
                containerClass="carousel-container"
                removeArrowOnDeviceType={["tablet", "mobile"]}
                dotListClass="custom-dot-list-style"
                itemClass="carousel-item-padding-40-px"
                >
                {breweryCards}
                </Carousel>
            </div>
        </>
    );
} 

export default Favorites;
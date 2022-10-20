import Carousel from "react-multi-carousel";
import "react-multi-carousel/lib/styles.css";
import BeerCard from './BeerCard';
import BreweryCard from './BreweryCard';
import React, { useEffect, useState } from 'react';
import { useToken } from './LoginToken';

function Favorites() {
    const [breweries, setBreweries] = useState([]);
    const token = useToken()[0];

    let beers = [
        {beer_id: 1, name:'Batman Stout', desciption: 'A stout as dark as the dark knight himself!', type: 'Stout', ibu: 70, abv: 5.11, brewery: 1, image_url: 'https://images.pexels.com/photos/5659755/pexels-photo-5659755.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'},
        {beer_id: 2, name:'805 Pale Ale', desciption: 'Our flagship beer, perfectly balanced mix of malty and hoppy', type: 'Pale Ale', ibu: 80, abv: 5.21, brewery: 1, image_url: 'https://images.pexels.com/photos/5530264/pexels-photo-5530264.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'},
        {beer_id: 3, name:'Orange Dream Sour', desciption: 'A farmhouse sour with hints of local oranges', type: 'Sour', ibu: 19, abv: 6.50, brewery: 1, image_url: 'https://images.pexels.com/photos/1269025/pexels-photo-1269025.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'},
        {beer_id: 4, name:'Batman Stout', desciption: 'A stout as dark as the dark knight himself!', type: 'Stout', ibu: 70, abv: 5.11, brewery: 2, image_url: 'https://images.pexels.com/photos/5659755/pexels-photo-5659755.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'},
        {beer_id: 5, name:'805 Pale Ale', desciption: 'Our flagship beer, perfectly balanced mix of malty and hoppy', type: 'Pale Ale', ibu: 80, abv: 5.21, brewery: 2, image_url: 'https://images.pexels.com/photos/5530264/pexels-photo-5530264.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'},
        {beer_id: 6, name:'Orange Dream Sour', desciption: 'A farmhouse sour with hints of local oranges', type: 'Sour', ibu: 19, abv: 6.50, brewery: 2, image_url: 'https://images.pexels.com/photos/1269025/pexels-photo-1269025.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'}
    ]

    useEffect(() => {
        async function getBreweries() {
          const url = `${process.env.REACT_APP_BREWERIES_AND_BEERS_API_HOST}/favorites/breweries`
          const response = await fetch(url);
          if (response.ok) {
            const data = await response.json();
            console.log(data)
            let formattedData = [];
            data.breweries.map((obj) => {
              return formattedData.push(obj);
            });
            setBreweries(formattedData);
          }
        }
        getBreweries();
        console.log(token)
      }, [])

    // Convert array to JSX items
    beers = beers.map(function(beer) {
        return <div>
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
                {beers}
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
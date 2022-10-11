import React, { useState, useEffect} from 'react'
import BeerCard from './BeerCard';

function Beers() {
    var beers = [
        {beer_id: 1, name: 'My First Item', image_url: 'https://images.pexels.com/photos/5858163/pexels-photo-5858163.jpeg?auto=compress&cs=tinysrgb&w=1600', description: 'Just a cool spot to come and drink some beers!'},
        {beer_id: 2, name: 'Another item', image_url: 'https://images.pexels.com/photos/5864290/pexels-photo-5864290.jpeg?auto=compress&cs=tinysrgb&w=1600', description: 'Just a cool spot to come and drink some beers!' },
        {beer_id: 3, name: 'Third Item', image_url: 'https://images.pexels.com/photos/1089930/pexels-photo-1089930.jpeg?auto=compress&cs=tinysrgb&w=1600', description: 'Just a cool spot to come and drink some beers!' },
        {beer_id: 4, name: 'Here is the Fourth', image_url: 'https://images.pexels.com/photos/1269025/pexels-photo-1269025.jpeg?auto=compress&cs=tinysrgb&w=1600', description: 'Just a cool spot to come and drink some beers!' },
        {beer_id: 5, name: 'High Five', image_url: 'https://images.pexels.com/photos/1267696/pexels-photo-1267696.jpeg?auto=compress&cs=tinysrgb&w=1600', description: 'Just a cool spot to come and drink some beers!' },
      ];

      // Convert array to JSX items
      beers = beers.map(function(beer) {
        return <div>
            <BeerCard 
            brewery_id = {beer.brewery_id}
            name = {beer.name}
            street = {beer.street}
            city = {beer.city}
            state = {beer.state}
            zip_code = {beer.zip_code}
            phone = {beer.phone}
            image_url = {beer.image_url}
            description = {beer.description}
            website = {beer.website}
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
            <h1>Beers!</h1>
            <div className="card-deck">
                {beers}
            </div>
        </div>
        
    )
}
export default Beers;
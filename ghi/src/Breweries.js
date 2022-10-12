import Masonry from 'react-masonry-css'
import BreweryCard from './BreweryCard';

function Breweries() {
    var breweries = [
        {brewery_id: 1, name: 'My First Item', image_url: 'https://images.pexels.com/photos/5858163/pexels-photo-5858163.jpeg?auto=compress&cs=tinysrgb&w=1600', description: 'Just a cool spot to come and drink some beers!'},
        {brewery_id: 2, name: 'Another item', image_url: 'https://images.pexels.com/photos/5864290/pexels-photo-5864290.jpeg?auto=compress&cs=tinysrgb&w=1600', description: 'Just a cool spot to come and drink some beers!' },
        {brewery_id: 3, name: 'Third Item', image_url: 'https://images.pexels.com/photos/1089930/pexels-photo-1089930.jpeg?auto=compress&cs=tinysrgb&w=1600', description: 'Just a cool spot to come and drink some beers!' },
        {brewery_id: 4, name: 'Here is the Fourth', image_url: 'https://images.pexels.com/photos/1269025/pexels-photo-1269025.jpeg?auto=compress&cs=tinysrgb&w=1600', description: 'Just a cool spot to come and drink some beers!' },
        {brewery_id: 5, name: 'High Five', image_url: 'https://images.pexels.com/photos/1267696/pexels-photo-1267696.jpeg?auto=compress&cs=tinysrgb&w=1600', description: 'Just a cool spot to come and drink some beers!' },
      ];

      // Convert array to JSX items
      breweries = breweries.map(function(brewery) {
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

      const breakpointColumnsObj = {
        default: 4,
        1100: 3,
        700: 2,
        500: 1
      };

      return (
        <div>
            <h1>Breweries!</h1>
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
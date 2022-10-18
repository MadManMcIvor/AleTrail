import BeerCardCarousel from './BeerCardCarousel';


function Beers() {
    let breweriesList = [
        {brewery_id: 1, name: 'BikeDog Brewery', image_url: 'https://images.pexels.com/photos/5858163/pexels-photo-5858163.jpeg?auto=compress&cs=tinysrgb&w=1600', description: 'Just a cool spot to come and drink some beers!'},
        {brewery_id: 2, name: 'Twisted Manzanita', image_url: 'https://images.pexels.com/photos/5864290/pexels-photo-5864290.jpeg?auto=compress&cs=tinysrgb&w=1600', description: 'Just a cool spot to come and drink some beers!' },
        {brewery_id: 3, name: 'Track 7', image_url: 'https://images.pexels.com/photos/1089930/pexels-photo-1089930.jpeg?auto=compress&cs=tinysrgb&w=1600', description: 'Just a cool spot to come and drink some beers!' },
        {brewery_id: 4, name: "Drake's Brewery", image_url: 'https://images.pexels.com/photos/1269025/pexels-photo-1269025.jpeg?auto=compress&cs=tinysrgb&w=1600', description: 'Just a cool spot to come and drink some beers!' },
        {brewery_id: 5, name: 'Hangar 24', image_url: 'https://images.pexels.com/photos/1267696/pexels-photo-1267696.jpeg?auto=compress&cs=tinysrgb&w=1600', description: 'Just a cool spot to come and drink some beers!' },
      ];
    
    
    breweriesList = breweriesList.map(function(brewery) {
        return <div>
                <h2>{brewery.name}</h2>
                <BeerCardCarousel
                brewery_id = {brewery.brewery_id}
                />
            </div>
    });
    
    console.log(breweriesList);
      return (
        <div>
            <h1>Beers!</h1>
            {breweriesList}
        </div>
        
    )
}
export default Beers;

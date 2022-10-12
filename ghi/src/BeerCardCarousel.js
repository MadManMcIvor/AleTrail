import Carousel from "react-multi-carousel";
import "react-multi-carousel/lib/styles.css";
import BeerCard from './BeerCard';

function BeerCardCarousel() {
    var beers = [
        {beer_id: 1, name: 'My First Item', image_url: 'https://images.pexels.com/photos/5858163/pexels-photo-5858163.jpeg?auto=compress&cs=tinysrgb&w=1600', description: 'Just a cool spot to come and drink some beers!'},
        {beer_id: 2, name: 'Another item', image_url: 'https://images.pexels.com/photos/5864290/pexels-photo-5864290.jpeg?auto=compress&cs=tinysrgb&w=1600', description: 'Just a cool spot to come and drink some beers!' },
        {beer_id: 3, name: 'Third Item', image_url: 'https://images.pexels.com/photos/1718384/pexels-photo-1718384.jpeg?auto=compress&cs=tinysrgb&w=1600', description: 'Just a cool spot to come and drink some beers!' },
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
    );
} 

export default BeerCardCarousel;
import { useState } from 'react';
import Button from 'react-bootstrap/Button';
import BreweryCardModal from './BreweryCardModal';

function BreweryCard(props) {
    
    const [modalShow, setModalShow] = useState(false);
    // console.log(props)

    return (
        <div key={props.brewery_id}>
            <div className="card">
                <img className="card-img-top" src={props.image_url} alt={props.name}/>
                <div className="card-body">
                    <h5 className="card-title">{props.name}</h5>
                    <p className="card-text">{props.description}</p>
                    <Button variant="primary" onClick={() => setModalShow(true)}>See more</Button>
                </div>
            </div>  
            <BreweryCardModal
                show={modalShow}
                onHide={() => setModalShow(false)}
                brewery_id = {props.brewery_id}
                name = {props.name}
                street = {props.street}
                city = {props.city}
                state = {props.state}
                zip_code = {props.zip_code}
                phone = {props.phone}
                image_url = {props.image_url}
                description = {props.description}
                website = {props.website}
                fav = {props.fav}
                user_id = {props.user_id}
            />
        </div>
        
    )
}

export default BreweryCard;
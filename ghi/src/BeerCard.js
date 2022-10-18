import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import { useState } from 'react';
import BeerCardModal from './BeerCardModal';

function BeerCard(props) {
  
  const [modalShow, setModalShow] = useState(false);

  return (
      <>
        <Card key={props.beer_id} style={{ width: '18rem' }}>
          <Card.Img variant="top" src={props.image_url} />
          <Card.Body>
            <Card.Title>{props.name}</Card.Title>
            <Card.Text>
              {props.description}
            </Card.Text>
            <Button variant="primary" onClick={() => setModalShow(true)}>See more</Button>
          </Card.Body>
        </Card>
        <BeerCardModal
           show={modalShow}
           onHide={() => setModalShow(false)}
           beer_id = {props.beer_id}
           name = {props.name}
           image_url = {props.image_url}
           description = {props.description}
           ibu = {props.ibu}
           abv = {props.abv}
        />
      </>
    );
  }

export default BeerCard;




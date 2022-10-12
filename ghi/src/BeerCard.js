import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';

function BeerCard(props) {
    return (
        <Card key={props.beer_id} style={{ width: '18rem' }}>
          <Card.Img variant="top" src={props.image_url} />
          <Card.Body>
            <Card.Title>{props.name}</Card.Title>
            <Card.Text>
              {props.description}
            </Card.Text>
            <Button variant="primary">See more</Button>
          </Card.Body>
        </Card>
      );
    }

export default BeerCard;




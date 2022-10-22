import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import Image from 'react-bootstrap/Image';
import FavoriteIcon from './FavoriteIcon';

function BeerCardModal(props) {
  return (
    <Modal
      {...props}
      size="lg"
      aria-labelledby="contained-modal-title-vcenter"
      centered
    >
      <Modal.Header closeButton>
        <Modal.Title id="contained-modal-title-vcenter">
        <h1>{props.name}</h1>
        </Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <Image fluid={true} src={props.image_url}/>
        <h4>Description</h4>
        <p>
            {props.description}
        </p>
        <h5>IBU: {props.ibu}</h5>
        <h5>Abv: {props.abv}</h5>
      </Modal.Body>
      <Modal.Footer>
        <FavoriteIcon true></FavoriteIcon>
        <Button onClick={props.onHide}>Close</Button>
      </Modal.Footer>
    </Modal>
  );
}

export default BeerCardModal;
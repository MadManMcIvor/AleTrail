import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import Image from 'react-bootstrap/Image';
import FavoriteIcon from './FavoriteIcon';

function BreweryCardModal(props) {

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
        <h4>Address: {props.street}, {props.city}, {props.state} {props.zip_code}</h4>
        <h4>Description</h4>
        <p>
            {props.description}
        </p>
      </Modal.Body>
      <Modal.Footer>
        <FavoriteIcon fav={props.fav}
        brewery_id={props.brewery_id}
        user_id = {props.user_id} />
        <Button onClick={props.onHide}>Close</Button>
      </Modal.Footer>
    </Modal>
  );
}

export default BreweryCardModal;
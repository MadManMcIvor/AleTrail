import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';

function LogoutModal(props) {
  return (
    <Modal
    {...props}
      size="lg"
      aria-labelledby="contained-modal-title-vcenter"
      centered
    >
      <Modal.Header closeButton>
        <Modal.Title id="contained-modal-title-vcenter">
        <h1>Logout</h1>
        </Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <h4>Are you sure?</h4>
        <Button onClick={props.onHide}>Logout!</Button>
      </Modal.Body>
      <Modal.Footer>
        <Button onClick={props.onHide}>Close</Button>
      </Modal.Footer>
    </Modal>
  );
}

export default LogoutModal;
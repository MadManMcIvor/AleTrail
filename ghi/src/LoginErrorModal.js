import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';

function LoginErrorModal(props) {
  return (
    <Modal
      {...props}
      size="lg"
      aria-labelledby="contained-modal-title-vcenter"
      centered
    >
      <Modal.Header closeButton>
        <Modal.Title id="contained-modal-title-vcenter">
          <h1>Error</h1>
        </Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <h4>Wrong email or password. Please try again.</h4>
      </Modal.Body>
      <Modal.Footer>
        <Button onClick={props.onHide}>Close</Button>
      </Modal.Footer>
    </Modal>
  );
}

export default LoginErrorModal;
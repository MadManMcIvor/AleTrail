import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import { useToken } from './LoginToken';

function LogoutModal(props) {
    const token = useToken()[0];
    const logout = useToken()[2];

    const handleSubmit = async (e) => {
        e.preventDefault();
        console.log(token);
        try {
        await logout();
        props.onHide();
        } catch(error){
          console.log(error);
          console.log("There was an error logging out.");
        }}

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
        <Button onClick={handleSubmit}>Logout!</Button>
      </Modal.Body>
      <Modal.Footer>
        <Button onClick={props.onHide}>Close</Button>
      </Modal.Footer>
    </Modal>
  );
}

export default LogoutModal;
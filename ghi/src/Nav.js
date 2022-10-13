import { NavLink } from 'react-router-dom';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';

function OurNav() {
  return (
    <>
      <Navbar bg="warning" variant="light" expand="md">
        <Container>
          <Navbar.Brand href="/breweries">AleTrail</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
              <Nav className="me-auto">
                <NavLink className="nav-link" to="/breweries">Breweries</NavLink>
                <NavLink className="nav-link" to="/beers">Beers</NavLink>
                <NavLink className="nav-link" to="/favorites">Favorites</NavLink>
              </Nav>
              <Nav>
                <NavLink className="nav-link" to="/settings">Settings</NavLink>
                <NavLink className="nav-link" to="/login">Sign Up</NavLink>
                <NavLink className="nav-link" to="/login">Login</NavLink>
                <NavLink className="nav-link" to="/login">Logout</NavLink>
              </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
    </>
  );
}

export default OurNav;
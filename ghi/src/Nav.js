import { NavLink } from 'react-router-dom';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';

function OurNav() {
  return (
    <>
      <Navbar bg="white" variant="light" expand="md">
        <NavLink className="nav-link" to="/breweries">
          <img
                  src={require('./images/logo.png')}
                  width="120"
                  height="100"
                  className="d-inline-block align-top"
                  alt="AleTrail logo"
                />
          </NavLink>
          <Container>
            <Navbar.Brand href="/breweries">
            </Navbar.Brand>
              <Navbar.Toggle aria-controls="basic-navbar-nav" />
              <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="me-auto">
                  <NavLink className="nav-link" to="/breweries"><h3>Breweries</h3></NavLink>
                  <NavLink className="nav-link" to="/beers"><h3>Beers</h3></NavLink>
                  <NavLink className="nav-link" to="/favorites"><h3>Favorites</h3></NavLink>
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
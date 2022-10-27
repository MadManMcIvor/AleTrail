//import { useEffect, useState } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import OurNav from './Nav';
import Breweries from './Breweries';
import Beers from './Beers';
import Favorites from './Favorites';
import SignupForm from './Signup';
import LoginPage from './Login';
import { AuthProvider, useToken } from './LoginToken';
import PrivateRoute from './PrivateRoute';

const domain = /https:\/\/[^/]+/;
const basename = process.env.PUBLIC_URL.replace(domain, '');

function GetToken() {
  // Get token from JWT cookie (if already logged in)
  useToken();
  return null
}


function App() {
  return (
   
    <BrowserRouter basename={basename}>
      <AuthProvider>
      <GetToken />
          <OurNav />
          <div className="container">
            <Routes>
            <Route path="/" element={<Breweries/>} />
            <Route path="breweries" >
              <Route path="" element={<Breweries/>} />
            </Route>
            <Route path="beers" >
              <Route path="" element={<Beers/>} />
            </Route>
            <Route path="favorites" >
              <Route path="" element={
                <PrivateRoute>
                  <Favorites/>
                </PrivateRoute>
                } />
            </Route>
            <Route path="signup" element={<SignupForm />} /> 
            <Route path="login" element={<LoginPage />} />
            </Routes>
          </div>
          </AuthProvider>
      </BrowserRouter>
  );
}

export default App;


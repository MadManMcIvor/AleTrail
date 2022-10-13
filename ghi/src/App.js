//import { useEffect, useState } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import OurNav from './Nav';
import Breweries from './Breweries';
import Beers from './Beers';
import Favorites from './Favorites';
import Settings from './Settings';

function App() {
  return (
    <BrowserRouter>
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
          <Route path="" element={<Favorites/>} />
        </Route>
        <Route path="settings" >
          <Route path="" element={<Settings/>} />
        </Route>
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;

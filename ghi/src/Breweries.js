import React, { useState, useEffect} from 'react'
import Masonry from 'react-masonry-css'

function Breweries() {
    var items = [
        {id: 1, name: 'My First Item'},
        {id: 2, name: 'Another item'},
        {id: 3, name: 'Third Item'},
        {id: 4, name: 'Here is the Fourth'},
        {id: 5, name: 'High Five'},
        {id: 6, name: 'High Five'},
        {id: 7, name: 'High Five'},
      ];
      
      const breakpointColumnsObj = {
        default: 4,
        1100: 3,
        700: 2,
        500: 1
      };

      // Convert array to JSX items
      items = items.map(function(item) {
        return <div key={item.id}>
                {item.name}
                    <div className="card">
                    <img className="card-img-top" src="https://images.pexels.com/photos/5858163/pexels-photo-5858163.jpeg?auto=compress&cs=tinysrgb&w=1600" alt="Card image cap"/>
                    <div className="card-body">
                    <h5 className="card-title">Card title that wraps to a new line</h5>
                    <p className="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                    </div>
            </div>
        </div>
      });
      console.log(items)
    return (
        <div>
            <h1>Breweries!</h1>
            <Masonry
                breakpointCols={breakpointColumnsObj}
                className="my-masonry-grid"
                columnClassName="my-masonry-grid_column">
                {items}
            </Masonry>
        </div>
        
    )
}

export default Breweries;
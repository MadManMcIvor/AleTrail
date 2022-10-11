import React, { useState, useEffect} from 'react'

function BeerCard(props) {

    return (
        <div className="w-25 p-3" key={props.beer_id}>
            <div className="card">
                <img className="card-img-top" src={props.image_url} alt="Card image cap"/>
                <div className="card-body">
                    <h5 className="card-title">{props.name}</h5>
                    <p className="card-text">{props.description}</p>
                </div>
            </div>  
        </div>
        
    )
}

export default BeerCard;




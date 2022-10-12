
function BreweryCard(props) {

    return (
        <div key={props.brewery_id}>
            <div className="card">
                <img className="card-img-top" src={props.image_url} alt={props.name}/>
                <div className="card-body">
                    <h5 className="card-title">{props.name}</h5>
                    <p className="card-text">{props.description}</p>
                </div>
            </div>  
        </div>
        
    )
}

export default BreweryCard;
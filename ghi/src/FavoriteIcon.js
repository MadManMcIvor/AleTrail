import React, { useState } from 'react';

function FavoriteIcon(props) {

    const [fav, setFav] = useState(props.fav);

    function RenderStar () {
        if(fav === 0){
            return (
                <img src="/empty-star-icon.png" alt="Not a favorite"width="50"></img>
            );
        }else{
            return(
                <img src="/star-icon.png" alt="Is a favorite" width="50"></img>
            );
        };
    };

    async function updateFav(){
        const bodyData = JSON.stringify({
            'user_id': props.user_id,
            'brewery_id': props.brewery_id
        })
        if(fav === 0){
            const favUrl = `${process.env.REACT_APP_BREWERIES_AND_BEERS_API_HOST}/favorites/breweries`
            const favResponse = await fetch(favUrl, {
                method: 'POST',
                headers: {
                    'accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: bodyData
            });
            if (favResponse.ok) {
                setFav(1);
            };
        }else{
            const url = `${process.env.REACT_APP_BREWERIES_AND_BEERS_API_HOST}/favorites/breweries`
            const response = await fetch(url, { method: "GET", credentials: "include" });
            if (response.ok) {
                const data = await response.json();
                for(let i=0; i < data.length; i++){
                    if(data[i]["brewery_id"] == props.brewery_id){
                        const fav_id = data[i]["brewery_favorite_id"];
                        const url = `${process.env.REACT_APP_BREWERIES_AND_BEERS_API_HOST}/favorites/breweries/${fav_id}`
                        const response = await fetch(url, { method: "DELETE", headers: {
                            'accept': 'application/json'
                        }});
                        if(response.ok){
                            setFav(0);
                        };
                    };
                };
            };
        };
    };

  return (
    <div className='favorite' onClick={updateFav}>
        <RenderStar />
    </div>
  );
};

export default FavoriteIcon;
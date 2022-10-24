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
        console.log(fav)
        if(fav === 0){
            const favUrl = `${process.env.REACT_APP_BREWERIES_AND_BEERS_API_HOST}/favorites/breweries`
            const favResponse = await fetch(favUrl, { method: "POST", credentials: "include" });
            if (favResponse.ok) {
                const data = await favResponse.json();
                favData = Array.from(data);
                setFav(1);
            };
        }else{
            const favUrl = `${process.env.REACT_APP_BREWERIES_AND_BEERS_API_HOST}/favorites/breweries`
            const favResponse = await fetch(favUrl, { method: "DELETE", credentials: "include" });
            if (favResponse.ok) {
                const data = await favResponse.json();
                favData = Array.from(data);
                setFav(0);
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
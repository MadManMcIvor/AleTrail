import React, { useState } from 'react';

function FavoriteIcon(props) {

    const [fav, setFav] = useState(false)

    function RenderStar () {
        if(fav === false){
            return (
                <img src="/empty-star-icon.png" width="50"></img>
            )
        }else{
            return(
                <img src="/star-icon.png" width="50"></img>
            )
        }
    }

    function updateFav(boolean){
        if(fav === false){
            setFav(true)
        }else{
            setFav(false)
        }
    }

  return (
    <div className='favorite' onClick={updateFav}>
        <RenderStar></RenderStar>
    </div>
  );
}

export default FavoriteIcon;
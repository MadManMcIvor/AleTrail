import React, { useState } from 'react';

function FavoriteIcon(props) {

    const [fav, setFav] = useState(props.fav)

    function RenderStar () {
        if(fav === 0){
            return (
                <img src="/empty-star-icon.png" alt="Not a favorite"width="50"></img>
            )
        }else{
            return(
                <img src="/star-icon.png" alt="Is a favorite" width="50"></img>
            )
        }
    }

    function updateFav(boolean){
        if(boolean === 0){
            setFav(true)
        }else{
            setFav(false)
        }
    }

  return (
    <div className='favorite' onClick={updateFav}>
        <RenderStar />
    </div>
  );
}

export default FavoriteIcon;
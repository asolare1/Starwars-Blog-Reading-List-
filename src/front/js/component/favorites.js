import React, { useContext, useEffect} from "react";
import { Context } from "../store/appContext";
import "../../styles/home.css";


export const Favorites = () =>{
const {store, actions} = useContext(Context)

    useEffect(() => {

        actions.getPeople()

    }, [])
    console.log(store.favorites)

    // let arr = [1, 2, 3, 4, 5];
    // for (let i = 0; i < arr.length; i++) {
    //   console.log(arr[i]);
    // }

    return (

<div class="dropdown">
  <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
    Favorites<p>{store.favorites.length}</p>
  </button>
  <ul class="dropdown-menu">
    {
      store.favorites.map((item, index) => {
        return <li key={index}><a class="dropdown-item" href="#">{item}<button onClick={() =>{actions.removeFavorites(item)}}>X</button></a></li>
      })
    }
  </ul>
</div>)


}
import React, { useContext, useEffect} from "react";
import { Context } from "../store/appContext";
import "../../styles/home.css";


export const Favorites = (people) =>{
const {store, actions} = useContext(Context)

    useEffect(() => {

        actions.getPeople()

    }, [])



    return (

<div class="card">
  {people.name}
</div>)


}
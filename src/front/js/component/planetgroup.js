import React, { useContext, useEffect } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.css";
import {Card} from "./card.js";

const Planetgroup = (props) => {

    const {store, actions} = useContext(Context)

    useEffect(() => {

        actions.getPlanets()

    }, [])


    return(
        <div class="scrolling-wrapper row flex-row flex-nowrap mt-4 pb-4 pt-2">
        
        {store.planets.map((planet, index) => {
        
        return <Card
            key={index}

            title={planet.name}
            link={"/planetdesc/" + index}
            text={`${planet.name} is a planet with a rotational period of ${planet.rotation_period} and a diameter of ${planet.diameter}.`}
        
        />
    
        }) 
    }
    </div>
    
    )
    

};
export {Planetgroup}
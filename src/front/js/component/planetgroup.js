import React, { useContext, useEffect } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.css";
import {Card} from "./card.js";
import { Link } from "react-router-dom";

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
            link={<Link 
                to={"/planetdesc/" + index}>
                <span class="btn btn-primary">Learn More!</span>
                </Link>}
            text={`${planet.name} is a planet with a rotational period of ${planet.rotation_period} and a diameter of ${planet.diameter}.`}
            img="https://images.immediate.co.uk/production/volatile/sites/4/2018/08/eso0603a-b364432.jpg?quality=90&resize=700,466"
            button={<button>Add to favorites</button>}
            >
                
        </Card>
    
    
        }) 
    }
    </div>
    
    )
    

};
export {Planetgroup}
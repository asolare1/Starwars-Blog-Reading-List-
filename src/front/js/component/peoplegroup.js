import React, { useContext,useEffect } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.css";
import {Card} from "./card.js";
import { Planetgroup } from "./planetgroup";
import { Link } from "react-router-dom";
import { Desc } from "../pages/peopledesc.js";

const Peoplegroup = (props) => {

    const {store, actions} = useContext(Context)

    useEffect(() => {

        actions.getPeople()

    }, [])

    return(
        <div class="scrolling-wrapper row flex-row flex-nowrap mt-4 pb-4 pt-2">
        
        {store.people.map((people, index) => {
       
        return <Card
            key={index}
            title={people.name}
            link={<Link 
                to={"/peopledesc/" + index}>
                <span class="btn btn-primary">Learn More!</span>
                </Link>}
            text={`Gender: ${people.gender} Eye-color: ${people.eye_color} Hair-color: ${people.hair_color}`}
            
            >
        
            </Card>
            

       
    
        }) 
    }
    </div>
    
    )
};

export {Peoplegroup}
import React, { } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.css";
import Card from "./card.js";

const Peoplegroup = (props) => {

fetch("https://www.swapi.tech/api/people/1")
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(err => console.error(err))


return(
<div class="scrolling-wrapper row flex-row flex-nowrap mt-4 pb-4 pt-2">
<Card name = "Luke Skywalker" img="https://lumiere-a.akamaihd.net/v1/images/luke-skywalker-main_fb34a1ff.jpeg?region=131%2C0%2C951%2C536"/>
<Card />
<Card />
<Card />
<Card />
<Card />
</div>

)
};
export default Peoplegroup
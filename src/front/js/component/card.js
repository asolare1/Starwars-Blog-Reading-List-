import React, { } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.css";

const Card = (props) => (
	<div class="col-5 cardsize" >
<div class="card-block card px-4">
  <img src={props.img} class="card-img-top" alt="..."></img>
    <div>
        <h5 class="card-title">{props.name}</h5>
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
    <a href="#" class="btn btn-primary">Learn more</a>
    <a href="#" class="btn btn-primary heart">♡</a>
  </div>
</div>
</div>

);
export default Card
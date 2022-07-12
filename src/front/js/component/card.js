import React, { } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.css";

const Card = (props) => (
	
<div class="card">
  <img src="https://picsum.photos/50/50" class="card-img-top" alt="..."></img>
  <div class="card-body">
        <h5 class="card-title">{props.name}</h5>
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
</div>


);
export default Card
import React, { } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.css";

const Card = ({img, text, title, link, link_text}) => (
	<div class="col-5 cardsize" >
<div class="card-block card px-4">
  <img src={img ? img : "https://lumiere-a.akamaihd.net/v1/images/luke-skywalker-main_fb34a1ff.jpeg?region=131%2C0%2C951%2C536"} class="card-img-top" alt="..."></img>
    <div>
        <h5 class="card-title">{title ? title : "Name" }</h5>
    <p class="card-text">{text ? text:"Description"}</p>
    {link}
    <a href="#" class="btn btn-primary heart">♡</a>
  </div>
</div>
</div>

);
export {Card}
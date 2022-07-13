
import React, { } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.css";

const Jumbotron = (props) =>{

return(
      <div class="container-fluid jumbotron">
        <h1 class="display-5 fw-bold">{props.title}</h1>
       
			{props.cards}

      </div>

   ) };
   export default Jumbotron
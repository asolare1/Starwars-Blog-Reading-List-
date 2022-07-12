
import React, { } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.css";

const Jumbotron = (props) =>{

return(
<div class="p-5 mb-4 rounded-3">
      <div class="container-fluid py-5">
        <h1 class="display-5 fw-bold">{props.title}</h1>
        <div class="row row-cols-1 row-cols-md-3 g-4 p-4">
			{props.cards}
		</div>
      </div>
    </div>
   ) };
   export default Jumbotron
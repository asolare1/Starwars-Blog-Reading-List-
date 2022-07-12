import React, { } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.css";
import Card from "./card.js";

const Cardgroup = (props) => {

return(
<div class="row row-cols-1 row-cols-md-2 g-4">
<Card />
<Card />
<Card />
<Card />
<Card />
<Card />
</div>
)
};
export default Cardgroup
import React, { useState, useEffect, useContext } from "react";
import { Link, useParams } from "react-router-dom";

import { Context } from "../store/appContext";

export const Planetdesc = () => {
	const { store, actions } = useContext(Context);
  const params = useParams();
  



	return (
		<div class="container">
		<div class="card mb-3">
  <div class="row g-0">
    <div class="col-md-4">
      <img src="https://lumiere-a.akamaihd.net/v1/images/luke-skywalker-main_fb34a1ff.jpeg?region=131%2C0%2C951%2C536" class="img-fluid rounded-start" alt="..."></img>
    </div>
    <div class="col-md-8">
      <div class="card-body">
        <h5 class="card-title"></h5>
        <p class="card-text">{`${store.planets[params.theid].name} is a planet in the Star Wars universe`}</p>
        <p class="card-text"></p>
      </div>
	  </div>
    </div>
  </div>
  <div class="container">
	Name: {store.planets[params.theid].name}   Climate: {store.planets[params.theid].climate}    Gravity: {store.planets[params.theid].gravity}    Terrain: {store.planets[params.theid].terrain}    
	
 </div>
</div>
	);
};

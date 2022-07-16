import React, { useState, useEffect, useContext } from "react";
import { Link, useParams } from "react-router-dom";

import { Context } from "../store/appContext";

export const Peopledesc = () => {
	const { store, actions } = useContext(Context);
  const params = useParams();
 
  useEffect(() => {

    actions.getPeople()

}, [])


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
        <p class="card-text">{`${store.people[params.theid].name} is a person from the Star Wars universe`}</p>
        <p class="card-text"></p>
      </div>
	  </div>
    </div>
  </div>
  <div class="container">
	Name:   {store.people[params.theid].name} Birthyear:   {store.people[params.theid].birth_year} Gender:  {store.people[params.theid].gender} Height:   {store.people[params.theid].height}   Skin color: {store.people[params.theid].skin_color}   Eye color: {store.people[params.theid].eye_color}
	
 </div>
</div>
	);
};

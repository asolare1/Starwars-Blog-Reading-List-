import React, { useState, useEffect, useContext } from "react";
import { Link } from "react-router-dom";

import { Context } from "../store/appContext";

export const Planetdesc = ({title, text}) => {
	const { store, actions } = useContext(Context);

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
        <p class="card-text">{title}</p>
        <p class="card-text">{text}</p>
      </div>
	  </div>
    </div>
  </div>
  <div class="container">
	Name:
	
 </div>
</div>
	);
};

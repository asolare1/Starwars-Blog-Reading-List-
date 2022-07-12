import React, { useContext } from "react";
import { Context } from "../store/appContext";
import Card from "../component/card.js";
import Jumbotron from "../component/jumbotron.js";
import "../../styles/home.css";
import Cardgroup from "../component/cardgroup.js";

export const Home = () => {
	const { store, actions } = useContext(Context);


	return (
		<div>
		<Jumbotron title="Character" cards={<Cardgroup />} />
		<Jumbotron title="Planets" cards={<Cardgroup />} />
		</div>
	);
};

import React, { useContext } from "react";
import { Context } from "../store/appContext";
import Card from "../component/card.js";
import Jumbotron from "../component/jumbotron.js";
import "../../styles/home.css";
import {Peoplegroup} from "../component/peoplegroup.js";
import {Planetgroup} from "../component/planetgroup.js";

export const Home = () => {
	const { store, actions } = useContext(Context);


	return (
		<div>
		<Jumbotron title="Character" cards={<Peoplegroup />} />
		<Jumbotron title="Planets" cards={<Planetgroup />} />
		</div>
	);
};

import axios from "axios";
import { wineListDataURL } from "../api";

export default function loadActionAsync (start,qty) {
    return async (dispatch) => {
        const wine = await axios.get(wineListDataURL(start, qty))
        dispatch(loadAction(wine));
    }
}

const loadAction = (wines) => {
    return {
        type:"DATA",
        payload: wines.data.results
        
    }
}
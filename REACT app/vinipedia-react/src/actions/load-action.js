import axios from "axios";
import { accessToken, wineListDataURL } from "../api";

axios.interceptors.request.use(
  (config) => {
    config.headers.authorization = `Token ${accessToken}`;
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default function loadActionAsync(start, qty) {
  return async (dispatch) => {
    const wine = await axios.get(wineListDataURL(start, qty));
    dispatch(loadAction(wine));
  };
}

const loadAction = (wines) => {
  return {
    type: "DATA",
    payload: wines.data.results,
  };
};

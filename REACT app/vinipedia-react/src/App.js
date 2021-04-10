import { Route, Switch } from "react-router";
import Nav from "./components/Nav";
import axios from "axios";
import {useEffect} from 'react';
import { useDispatch, useSelector } from "react-redux";
import loadActionAsync from './actions/load-action';
import WineList from './components/WineList';
import SearchBar from "./components/SearchBar";
import Homepage from "./pages/Homepage";

function App() {

  const dispatch = useDispatch()

  const wineData = useSelector(state => state.load.wines)
  console.log("winedata",wineData)

  useEffect(() =>{
    dispatch(loadActionAsync());
  },[dispatch])

  return (
    <div className="App">
      <Switch>
        <Route path="/" exact>
          <Nav />
          <SearchBar />
          <Homepage />
          <WineList wineData={wineData} />
        </Route>
      </Switch>
    </div>
  );
}

export default App;

import React from "react";
import ReactDOM from "react-dom";
import { component, useState } from "react"
import LoadingBar from 'react-top-loading-bar'
import LoginPage from "./loginPage";
import Homepage from "./homepage";
import { BrowserRouter as Router,Switch,Route } from "react-router-dom";

export default function App() {

  const[progress,setProgress]=useState(0);
  const[data,setData]=useState();

  return (
    <>
    <LoadingBar color='#c8ff93' shadow={true} height={3} progress={progress} onLoaderFinished={() => setProgress(0)}/>
    <Router>
      <Switch>
        <Route exact path="/" render={props => <LoginPage setData={setData} setProgress={setProgress} />} />
        <Route path="/getstudentdetails" render={props => <Homepage setData={setData} data={data} setProgress={setProgress} />}  />
        <Route> <h1> 404 Not Found. </h1></Route>
      </Switch>
    </Router>
    </>
  );
}
const app = document.getElementById("app");
ReactDOM.render(<App />, app);
import React, { useEffect,useState } from 'react';
import { useHistory, useRouteMatch } from "react-router";
import jQuery from './jQuery'
import { Link,Switch,Route } from "react-router-dom";

import Header from './Header'
import Dashboard from './Dashboard'
import ChangePassword from './ChangePassword'

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }
var csrftoken = getCookie('csrftoken');


export default function Homepage(props) {
    const history=useHistory();
    const match=useRouteMatch();
    const data = props.data
    

    const logout=(e)=>{
      logoutbysession()
    }

    async function logoutbysession(){
      const requestoptions={
        method:"POST",
        headers:{'Content-Type':'application/json',
                    'X-CSRFToken': csrftoken
                    },
        body:JSON.stringify({
        }),
      };
      props.setProgress(10)      
      let response = await fetch("/api/logoutbysession",requestoptions)
      props.setProgress(50)
      if(response.status == 200){
        props.setProgress(100)
        history.push({
          pathname:'/',
        })
        props.setData(null)
      }
      else{
        history.push({
          pathname:'/',
        })
        props.setData(null)
        props.setProgress(100)
      }
    }

    async function fetchDetailsBySession(){
        const requestoptions={
          method:"POST",
          headers:{'Content-Type':'application/json',
                      'X-CSRFToken': csrftoken
                      },
          body:JSON.stringify({
          }),
        };
        props.setProgress(10)      
        let response = await fetch("/api/sessionverify",requestoptions)
        props.setProgress(50)
        if(response.status == 200){
          props.setProgress(100)
          let data =  await response.json()
          history.push({
            pathname:'/getstudentdetails',
          })
          props.setData(data)
        }
        else{
          props.setProgress(100)
          history.push({
            pathname: "/"
          })
        }
    }
    useEffect(() => {
      fetchDetailsBySession();
    }
    , []);
    if(props.data){
      console.log(props.data)
      document.title="HomePage | "+props.data.Name ;
      return (
        <div className="homepage">
            {/* <h1>Hello{locationgrab.state.Name}</h1> */}
            <Header data={data} logout={logout} csrftoken={csrftoken}></Header> 
            <Route exact path={`${match.url}`}  render={props => <Dashboard data={data} />}  />
            <Route exact path={`${match.url}/changepassword`}  render={props => <ChangePassword data={data} />}  />
            {/* <button onClick={logout}>LogOut</button> */}
        </div>
      )
    }
    else{
      return(<><h1>You are not logged In.</h1><button onClick={logout}>LogOut</button></>)
    }
}

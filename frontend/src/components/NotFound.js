import React from "react";
import "./error.css";
import {Link} from "react-router-dom";

function NotFound() {
    return (
        <div id="notfound">
            <div className="notfound">
                <div className="notfound-404">
                    <h3>Oops!</h3>
                    <h1><span>#</span><span>4</span><span>0</span><span>4</span></h1>
                </div>
                <h2>We are sorry, the page you requested was not found.</h2>
                <p>Go back to HBTU <Link className="errgobackbutn"  to="/">Student Login</Link></p>
            </div>
        </div>
    );
}
export default NotFound;

import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import notice_app from './notice_app';
import Home from './home';
import student_app from './student_app';
const Webpages = () => {
    return(
        <Router>
            <Route exact path="" component= {Home} />
            <Route path = "/notice_app" component = {notice_app} />
            <Route path = "/student_app" component = {student_app} />
        </Router>
    );
};
export default Webpages;
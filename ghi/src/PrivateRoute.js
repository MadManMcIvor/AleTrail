import React from "react";
import { useToken } from './LoginToken';
import { Navigate } from "react-router-dom";

const PrivateRoute = ({ children }) => {
    const [token] = useToken();
    return token ? children : <Navigate to="/login" />;
};



export default PrivateRoute;

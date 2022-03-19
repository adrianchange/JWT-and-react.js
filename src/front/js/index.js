// Import react into the bundle
import React from "react";
import ReactDOM from "react-dom";

// Include styles into the bundle
import "../style/index.css";

// Import components
import AppRouter from "./AppRouter.jsx";

// Render react application
ReactDOM.render(<AppRouter />, document.querySelector("#app"));

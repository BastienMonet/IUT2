import _ from 'lodash';
import "./app.js";

function component() {
  const element = document.createElement("div");

  // Lodash, currently included via a script, is required for this line to work
  element.innerHTML = _.join(["Hello", "webpack"], " ");
  element.style.display = "None";

  return element;
}

document.body.appendChild(component());
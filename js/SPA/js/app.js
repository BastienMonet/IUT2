import { data, getArticle} from "./service/articleProvider.js";
import {Home} from "./views/home.js";
import {Router} from "./service/router.js"; 

// const home = new Home();
// home.renderHome();


// initial rendering of the home page
const router = new Router();
router.activate();
// we are trying to create a mini router with the navigation api


console.log("Data loaded:");
console.log(data);
console.log(getArticle("Article 1"));
import {Home} from "../views/home.js";
import {Article} from "../views/article.js";

// we are trying to create a mini router with the navigation api

class Router {

    constructor() { 
        this.handlehash(['_', 'home']);
        Home.render();
    }

    handlehash(splitedUrl) {
        // console.log(split);
        if(splitedUrl.length == 2) {
            const href=splitedUrl[1];
            // we use jquery cuz i need it for my internship
            let allpage = $('.page');
            console.log(allpage);
            for (let page of allpage) {
                page.style.display = "none";
            }
            $('#' + href).css("display", "block");
        }
    }

    getId() {
        const id = localStorage.getItem('id');
        localStorage.removeItem('id');
        return id;
    }

    activate() {

        window.navigation.addEventListener('navigate', (event) => {
                const url = new URL(event.destination.url);
                const split = url.href.split("#");
                if(split.length == 2) {
                    const actualPage = split[1];
                    console.log("Current page: " + actualPage);
                    this.handlehash(split);
                    switch (actualPage) {
                        case "home":
                            Home.render();
                            break;
                        case "article":
                            const id = this.getId();
                            console.log("id: " + id);
                            if (id != null) {
                                const article = new Article(id);
                                article.render();
                            } else {
                                console.log("here")
                                this.handlehash(['_', 'not-found']);
                            }
                            break;
                        case "not-found":
                            // stop infinite looping when the user tries to access a non existing page
                            break;
                        default:
                            this.handlehash(['_', 'not-found']);
                            Home.render();
                            console.log("Page not found");  
                            break;
                }
                } else {
                    this.handlehash(['_', 'home']);
                    Home.render();
                    console.log("Page not found");
                }
                
            }
        );
    }


}


export {Router}






import {data, getArticleByIndex} from "../service/articleProvider.js";

class Home {

    static showListArticles = () => {
        const container = $('.articles-container')
        
        container.text('');

        let ul = document.createElement('ul');
        for (let i in data['articles']) {
            const li = document.createElement('li');
            li.innerHTML = data['articles'][i].title;
            let btn = document.createElement('button');  
            btn.textContent = " (Read more)";
            btn.addEventListener('click', () => {
                const index = data['articles'][i].index;
                console.log("Index: " + index);
                if (index != null) {
                    localStorage.setItem('id',  index);
                }
                window.location.href = "#article";
                
            });
            li.appendChild(btn);
            ul.appendChild(li);
        }
        container.append(ul);
        console.log("List of articles displayed");
        return;
    }

    static showMajorInfo() {
        $('#titre-json').text(data['title']);
        $('#intro').text(data['introduction']);
    }

    static render() {
        Home.showMajorInfo();
        Home.showListArticles();
    }


}

export {Home};
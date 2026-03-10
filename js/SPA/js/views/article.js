import {data, getArticleByIndex} from "../service/articleProvider.js";


class Article {
    
    constructor(index) {
        this.article = getArticleByIndex(index);
    }

    render() {
        $('#titre-article').text(this.article["title"]);
        if ("text" in this.article) {
            $('#text').text(this.article["text"]);
        } else {
            $('#text').text("No text available for this article");
        }
        $('#see-more').attr( 'href', this.article["see_more"]);
        $('#modified-by').attr('href',this.article["modified_by"]);
    } 
}

export {Article}
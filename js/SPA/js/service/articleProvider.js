
export async function getData() {
    const result = await fetch('https://geoffroycochard.github.io/iuto.but2.js/resources/app_spa/constitution.json');
    if (result.ok) {
        const dataFetched = await result.json();
        return dataFetched;
    } else {
        alert("erreur chargement fichier");
    }
}

export const data = await getData();

export function getArticle(title) {
    // find function allows to return first element that match condition in it's callback
    return data["articles"].find(article => article.title === title);
}

export function getArticleByIndex(index) {
    // find function allows to return first element that match condition in it's callback
    return data["articles"].find(article => article.index === index);
}



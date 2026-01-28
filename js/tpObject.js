
class Event {
    type = '';
    date = '';
    constructor(date) {
        this.date = date;
    }



    get type() {
        return this.type;
    }

    set type(type) {
        this.type = type;
    }

    get date() {
        return this.date;
    }

    set date(date) {
        this.date = date;
    }

}

class Sport extends Event {
    
    sport = '';
    teamA = '';
    teamB = '';
    date = '';
    
    constructor(sport, teamA, teamB, date) {
        super(date);
        this.type = 'Football';
        this.sport = sport;
        this.teamA = teamA;
        this.teamB = teamB;
    }

    toString() {
        return 'Rencontre de ' + this.sport + " entre " + this.teamA + " et " + this.teamB; 
    }

}

class Concert extends Event {
    
    
    constructor(theme, date) {
        super(date);
        this.theme = theme;
    }

    toString() {
        return 'Concert de ' + this.theme + ' le ' + this.date; 
    }
}

class Factory {

    static createEvent(type, ...args) {
    try {
        switch(type) {
            case 'Football':
                return new Sport(...args);
            case 'Concert':
                return new Concert(...args);
        }
    } catch (e) {
        console.error(e)
    }

    }
}

const tennis = Factory.createEvent('Football', "a", "b", new Date("2022-03-25"))
console.log(tennis.toString());

const concert = Factory.createEvent('Concert', "Rock", new Date("2022-04-10"))
console.log(concert.toString());

const listEvent = [tennis, concert];

class Render {
    static renderInP(listEvent){
        const ul = document.createElement("ul");
        for (const event of listEvent) {
            const li = document.createElement("li");
            li.textContent = event.toString();
            ul.appendChild(li);
        }
        document.body.appendChild(ul);
    }
}

Render.renderInP(listEvent);











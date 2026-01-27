


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
        return 'Concert de ' + this.theme; 
    }
}

class Factory {

    createEvent(type, ...args) {
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

let factory = new Factory();

const tennis = factory.createEvent('Football', "a", "b", new Date("2022-03-25"))
console.log(tennis.toString());
function getRndStatus(){
    const rndNum = Math.random();
    if(rndNum > 0.5) return false
    else if(rndNum > 0.1) return true
    else return "broken"
}

const PEOPLE_PER_SLIDE = 5;

function generateColorForPerson(index){
    const maxColors = 360;
    return `hsla(${(maxColors / PEOPLE_PER_SLIDE) * index}, 100%, 25%, 1)`
}

function chunk(array, chunkSize){
    let chunks = [];

    for(var i = 0; i < Math.ceil(array.length/chunkSize); i++){
        chunks.push(array.slice(i * chunkSize, (i + 1) * chunkSize))
    }

    return chunks;
}

function range(to){
    return [...Array(to).keys()]
}

let people = ([...Array(10).keys()]).map(x => ({
    name: "Tom Hickman " + x,
    picture: "http://127.0.0.1:8000/static/images/expanded_photo_tkh.jpg",
    username: "thickman" + x 
}))

function parseStatus(status){
    if(status){
        return "free"
    }
    else{
        return "taken"
    }
}

let peopleGroups = chunk(people, PEOPLE_PER_SLIDE);

function getTakenExtraHTML(object){
    return (
            !object.status ? `
            data-toggle="popover" data-trigger="hover"
            data-content=${object.owner}`:""
        ) + " " + 
        (
            !object.status?
            `data-owner="${object.owner}"`:""
        )
}

function setCurrentKitchenStatus(status){
    document.querySelector(".hobs").innerHTML = chunk(status.hobs, 2).map(
        hobGroup => /*html*/`
        <div class="hob-group">
        ${
            chunk(hobGroup, 2).map(
                hobLine => /*html*/`
                <div class="hob-line">
                    ${hobLine.map(
                        hob => /*html*/`
                        <div
                        ${getTakenExtraHTML(hob)}
                        class="hob ${parseStatus(hob.status)}">
                            <div>
                                ${hob.name}
                            </div>
                        </div>
                        `
                    ).join("\n")}
                </div>
                `
            ).join("\n")
        }
        </div>
        `
    ).join("\n");

    document.querySelector(".fridges").innerHTML = status.fridges.map(
        fridge => /*html*/`
        <div class="fridge">
            <h7>${fridge.name}</h7>
            <div class="fridge-content">
                ${fridge.contents.map(
                    fridgeRow => /*html*/`
                    <div class="fridge-row">
                        ${
                            fridgeRow.map(fridgeSlot => 
                                /*html*/`
                                <div class="fridge-slot ${parseStatus(fridgeSlot.status)}"
                                    ${getTakenExtraHTML(fridgeSlot)}>&nbsp;</div>
                                     
                                `
                            ).join("\n")
                        }
                    </div>
                    `
                ).join("\n")}
            </div>
        </div>
        `
    ).join("\n");

    document.querySelector(".ovens").innerHTML = status.ovens.map(
        oven => /*html*/`
        <div ${getTakenExtraHTML(oven)} class="oven ${parseStatus(oven.status)}">
            <div>
            ${oven.name}
            </div>
        </div>
        `
    ).join("\n");

    document.querySelector(".infobox").innerHTML = /*html*/`
        <div>
            <b>Members:</b> <span>${people.length}</span>,
            <b>Fridges:</b> <span>${status.fridges.length}</span>
        </div>
        <div>
            <b>Hobs:</b> <span>${status.hobs.length}</span>,
            <b>Ovens:</b> <span>${status.ovens.length}</span>
        </div>
    `
}

async function populateCurrentKitchenStatus(){
    setCurrentKitchenStatus(
        (await (await fetch("http://127.0.0.1:8000/main/kitchen/the-ultimate-kitchen")).json())
    )
}

function onCarouselNext(newSlide){
    document.querySelectorAll(`*[data-owner]`).forEach(x => {
        x.style["border-color"] = "";
        x.style["box-shadow"] = "";
    });

    peopleGroups[newSlide].map((person, i) => {
        const color = generateColorForPerson(i);

        const ownedItems = document.querySelectorAll(`*[data-owner=${person.username}]`);
        ownedItems.forEach(x => {
            x.style["border-color"] = color;
            x.style["box-shadow"] = `inset ${color} 0px 0px 5px 1px`;
        });
    })
}

function setPeople(peopleChunks){
    document.querySelector(".carousel-inner").innerHTML = peopleChunks.map(
        (group, groupI) => 
        /*html*/`
        <div class="carousel-item ${groupI == 0?"active":""}">
            <div class="people-slide">
                ${group.map(
                    (person, personIndex) => {
                        return /*html*/`
                        <div class="profile" style="border-color: ${generateColorForPerson(personIndex)}">
                            <div class="profile-pic" style="background-image: url(${person.picture})">
                                &nbsp;
                            </div>
                            ${person.name}
                        </div>
                        `
                    }
                ).join("\n")}
            </div>
        </div>`
    ).join("\n");

    document.querySelector(".carousel-indicators").innerHTML = range(peopleGroups.length).map(
        i => /*html*/`
            <li data-target="#people-carousel" data-slide-to="${i}" class="${i == 0?"active":""}"></li>
        `
    ).join("\n")
}


$(() => {
    populateCurrentKitchenStatus();
    setInterval(1000, () => {
        populateCurrentKitchenStatus();
    })
    /*setCurrentKitchenStatus({
        hobs: [
            [{
                name: "my Hob",
                status: true
            }, {
                name: "another Hob",
                status: false,
                owner: "thickman1"
            },
            {
                name: "yet another Hob",
                status: true
            }],
            [{
                name: "single Hob",
                status: true
            }]
        ],
        fridges: [{
            name: "my fridge", 
            contents: [
                [{status: false, owner: "thickman1"}, {status: true}],
                [{status: true}, {status: false, owner: "thickman2"}],
                [{status: true}, {status: true}],
                [{status: false, owner: "thickman3"}, {status: true}],
                [{status: true}, {status: false, owner: "thickman10"}],
                [{status: false, owner: "thickman7"}, {status: true}],
                [{status: true}, {status: false, owner: "thickman9"}]
            ]
        }],
        ovens: [{
            name: "my oven",
            status: false,
            owner: "thickman1"
        },
        {
            name: "another oven",
            status: true
        }]
    })*/

    setPeople(peopleGroups);

    $('#people-carousel').on('slid.bs.carousel', (ev) => {
        onCarouselNext(ev.to);
    })

    onCarouselNext(0);

    $(function () {
        $('[data-toggle="popover"]').popover()
      })
})


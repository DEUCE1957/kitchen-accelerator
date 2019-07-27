function getRndStatus(){
    const rndNum = Math.random();
    if(rndNum > 0.5) return "taken"
    else if(rndNum > 0.1) return "free"
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
    picture: "images/expanded_photo_tkh.jpg",
    username: "thickman" + x 
}))

let peopleGroups = chunk(people, PEOPLE_PER_SLIDE);

function setCurrentKitchenStatus(status){
    function hobInfoToHTML(info){
        return /*html*/`
            <div class="hob ${info.status}">
                <div>
                    ${info.name}
                </div>
            </div>
        `
    }

    document.querySelector(".hobs").innerHTML = status.hobs.map(
        hobGroup => /*html*/`
        <div class="hob-group">
        ${
            (hobGroup.length >= 3)?
                /*html*/`
                <div class="hob-line">
                    ${hobGroup.slice(0, 2).map(hobInfoToHTML).join("\n")}
                </div>
                <div class="hob-line">
                    ${hobGroup.slice(2).map(hobInfoToHTML).join("\n")}
                </div>
                `:
                /*html*/`
                <div class="hob-line">
                    ${hobGroup.map(hobInfoToHTML).join("\n")}
                </div>
                `
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
                                <div ${fridgeSlot.status == "taken"?`data-owner="${fridgeSlot.owner}"`:""}
                                     class="fridge-slot ${fridgeSlot.status}"
                                     ${
                                        fridgeSlot.status == "taken" ? `
                                        data-toggle="popover" data-trigger="hover"
                                        data-content=${fridgeSlot.owner}
                                        `:""
                                     }>&nbsp;</div>
                                     
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
        <div class="oven ${oven.status}">
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
    setCurrentKitchenStatus({
        hobs: [
            [{
                name: "my Hob",
                status: "free"
            }, {
                name: "another Hob",
                status: "taken"
            },
            {
                name: "yet another Hob",
                status: "free"
            }],
            [{
                name: "single Hob",
                status: "free"
            }]
        ],
        fridges: [{
            name: "my fridge", 
            contents: [
                [{status: "taken", owner: "thickman1"}, {status: "free"}],
                [{status: "free"}, {status: "taken", owner: "thickman2"}],
                [{status: "free"}, {status: "free"}],
                [{status: "taken", owner: "thickman3"}, {status: "free"}],
                [{status: "free"}, {status: "taken", owner: "thickman10"}],
                [{status: "taken", owner: "thickman7"}, {status: "free"}],
                [{status: "free"}, {status: "taken", owner: "thickman9"}]
            ]
        }],
        ovens: [{
            name: "my oven",
            status: "free"
        },
        {
            name: "another oven",
            status: "free"
        }]
    })

    setPeople(peopleGroups);

    $('#people-carousel').on('slid.bs.carousel', (ev) => {
        onCarouselNext(ev.to);
    })

    onCarouselNext(0);

    $(function () {
        $('[data-toggle="popover"]').popover()
      })
})


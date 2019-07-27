function getRndStatus(){
    const rndNum = Math.random();
    if(rndNum > 0.5) return "taken"
    else if(rndNum > 0.1) return "free"
    else return "broken"
}

function generateNewColor(){
    return "purple";
}

let people = ([...Array(100).keys()]).map(x => ({
    name: "Tom Hickman " + x,
    picture: "images/expanded_photo_tkh.jpg",
    username: "thickman" + x 
}))

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
                            fridgeRow.map(fridge => 
                                /*html*/`<div class="fridge-slot ${fridge.status}">&nbsp;</div>`
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

    $('#people-carousel').on('slid.bs.carousel', (ev) => {
        console.log(ev.to)
    })

    // document.querySelector(".people").innerHTML = status.people.map(
    //     person => /*html*/`
    //     <div class="profile" style="border-color: ${generateNewColor()}">
    //         <div class="profile-pic" style="background-image: url(${person.picture})">
    //             &nbsp;
    //         </div>
    //         ${person.name}
    //     </div>
    //     `
    // ).join("\n");
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
                [{status: "free"}, {status: "taken", owner: "thickman2"}]
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
})


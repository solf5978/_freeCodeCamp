const cardObjectDefinitions = [
    {id:1, imagePath:"./images/card-KingHearts.png"},
    {id:2, imagePath:"./images/card-JackClubs.png"},
    {id:3, imagePath:"./images/card-QueenDiamonds.png"},
    {id:4, imagePath:"./images/card-AceSpades.png"}
]

let cards = []
const cardBackImgPath = "./images/card-back-blue.png"
const playGameButtonElem = document.getElementById("playGame")
const cardContainerElem = document.querySelector(".card-container")
const collapseGridAreaTemplate = '"a a" "a a"'
const cardCollectionCellClass = ".card-pos-a"

loadGame()

function loadGame() {
    createCards()

    cards = document.querySelectorAll(".card")
    playGameButtonElem.addEventListener("click", () => startGame())


}

function startGame() {
    initializeNewGame()
    startRound()
}

function initializeNewGame() {

}

function startRound() {
    initializeNewRound()
    collectnCards()
}

function initializeNewRound() {

}

function collectnCards() {
    transformGridArea(collapseGridAreaTemplate)
    addCardsToGridAreaCell(cardCollectionCellClass)
}

function transformGridArea(areas) {
    cardContainerElem.style.gridTemplateAreas = areas
}

function addCardsToGridAreaCell(cellPositionClassName) {
    const cellPositionElem = document.querySelector(cellPositionClassName)

    cards.forEach((card, index) => {
        addChildElement(cellPositionElem, card)
    })
}

function createCards() {
    cardObjectDefinitions.forEach((cardItem) => {
        createCard(cardItem)
    })
}


function createCard(cardItem) {

    // Create Card Elements 
    const cardElem = createElement("div")
    const cardInnerElem = createElement("div")
    const cardFrontElem = createElement("div")
    const cardBackElem = createElement("div")
    const cardFrontImg = createElement("img")
    const cardBackImg = createElement("img")

    addClassToElement(cardElem, "card")
    addIdToElement(cardElem, cardItem.id)

    addClassToElement(cardInnerElem, "card-inner")
    addClassToElement(cardFrontElem, "card-front")
    addClassToElement(cardBackElem, "card-back")
    addSrcToImageElem(cardBackImg, cardItem.imagePath)
    addSrcToImageElem(cardFrontImg, cardItem.imagePath)

    addClassToElement(cardBackElem, "card-img")
    addClassToElement(cardFrontElem, "card-img")

    addChildElement(cardBackElem, cardBackImg)
    addChildElement(cardFrontElem, cardFrontImg)
    addChildElement(cardInnerElem, cardBackElem)
    addChildElement(cardInnerElem, cardFrontElem)
    addChildElement(cardElem, cardInnerElem)

    addCardToGridCell(cardElem)

}

function createElement(elemType) {
    return document.createElement(elemType)
}

function addClassToElement(elem, className) {
    elem.classList.add(className)
}

function addIdToElement(elem, id) {
    elem.id = id
}

function addSrcToImageElem(imgElem, src) {
    imgElem.src = src
}

function addChildElement(parentElem, childElement) {
    parentElem.appendChild(childElement)
}

function addCardToGridCell(card) {
    const cardPositionClassName = mapCardIdToGridCell(card)
    const cardPosElem = document.querySelector(cardPositionClassName)
    addChildElement(cardPosElem, card)
}

function mapCardIdToGridCell(card) {
    if(card.id == 1){
        return ".card-pos-a"
    }
    else if(card.id == 2){
        return ".card-pos-b"
    }
    else if(card.id == 3){
        return ".card-pos-c"
    }
    // Case D
    else {
        return ".card-pos-d"
    }
}
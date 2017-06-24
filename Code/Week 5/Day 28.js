//Today I refactored my jQuery down to vanilla JA to try and trouble shoot the methodology in my pairs game:

//     Global variables:
//----------------------------------

//Setup vars:
var iconList = [
  "ruby",
  "python",
  "java",
  "php",
  "javascript",
  "nodejs",
  "rails",
  "react",
  "angularjs",
  "jquery",
  "typescript",
  "dot-net",
  "vuejs",
  "html5",
  "sass",
  "css3", 
]
const death = ["ie10"];
const life = ["git"];
const playBoard = document.getElementById("tile-container");
const iconStart = "<i class='tile devicon-";
const iconEnd = "-plain clickable facedown'></i>";
let cardList = []
let lives = 2;
let guessed = false;
let specialCards = 4;
let firstGuess = true;
let secondGuess = false;
let cards;



//     Global functions:
//----------------------------------


//  Construct functions:
//------------------------------

const buildArray = () => {
  cardList = cardList.concat(death, iconList, death, life, iconList, death);
}

const shuffleCards = arr => {
  let temp;
  let randi;
  for (let i = arr.length -1; i >= 0; i--) {
    randi = Math.floor(Math.random() * i + 1);
    temp = arr[i];
    arr[i] = arr[randi];
    arr[randi] = temp;
  }
}

const dealCards = (cardArr, dest) => {
  for( let i = 0; i < cardArr.length; i++) {
    let element = `${iconStart}${cardArr[i]}${iconEnd}`;
    dest.insertAdjacentHTML("beforeend", element);
  }
  cards = document.querySelectorAll(".clickable");
  
}

const buildEventHandlers = nodeList => {
  for (let i = 0; i < nodeList.length; i++) {
    nodeList[i].addEventListener("click", cardClickedEvent, false);
  }
}

// Logic functions:
//------------------------------


const endTurn = () => {
  //end turn logic
}

const endGame = () => {
  //end game logic
}

const evalCard = card => {
  card["icon"] = card.classList[1].split("-")[1];
  if (card.icon === "ie10") {
    lives -= 1;
    if (lives === 0) {
      endGame();
    } else {
      endTurn();
      return false;
    }
  } else if (card.icon === "git") {
    lives += 1;
    score += 50;
    endTurn();
    return false;
  } else {
    return true;
  }
}

const flipCard = card => {   
    card.classList.toggle("facedown");
}

const cardClickedEvent = event => {
  const card = event.srcElement;
  card.removeEventListener("click", cardClickedEvent);
    evalCard(card);
    
  } 
}



//     Run Game:
//----------------------------------

// Setup:
//------------------------------
buildArray();
shuffleCards(cardList);
dealCards(cardList, playBoard);
buildEventHandlers(cards);


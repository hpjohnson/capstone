/**
 * run on page load
 */
document.addEventListener("DOMContentLoaded", function () {
    
    viewQuestion()

})

/**
 * add event listeners and functionality to all buttons
 */
function viewQuestion() {

    const questionButtons = document.getElementsByClassName("question-view-button");

    for (let questionButton of questionButtons) {
        
        questionButton.addEventListener("click", function () {
            
            // get the question card
            const questionCard = this.parentElement.parentElement.parentElement;
            
            // get the content from the card
            // const questionTitle = questionCard.getElementsByClassName("question-title")[0].textContent;
            // const questionSubtitle = questionCard.getElementsByClassName("question-subtitle")[0].textContent;
            // const questionSummary = questionCard.getElementsByClassName("question-summary")[0].textContent;
            // const questionContent = questionCard.getElementsByClassName("question-content")[0].textContent;
            // const questionDifficulty = questionCard.getElementsByClassName("difficulty")[0].textContent;
            const questionTitle = questionCard.querySelector(".question-title").textContent;
            const questionSubtitle = questionCard.querySelector(".question-subtitle").textContent;
            const questionContent = questionCard.querySelector(".question-content").textContent;
            const questionDifficulty = questionCard.querySelector(".question-difficulty").textContent;

            // get the content from the data attributes
            const questionDateCreated = questionCard.getAttribute("data-created-on");
            const questionDateUpdated = questionCard.getAttribute("data-last-updated");
            const questionUpdateCount = questionCard.getAttribute("data-update-count");

            // set data in the modal
            document.querySelector(".question-view-title").innerHTML = questionTitle;
            document.querySelector(".question-view-subtitle").innerHTML = questionSubtitle;
            document.querySelector(".question-view-difficulty").innerHTML = questionDifficulty
            document.querySelector(".question-view-content").innerHTML = questionContent;
            document.querySelector(".question-view-date-created").innerHTML = `Date Posted: ${questionDateCreated}`;
            document.querySelector(".question-view-date-updated").innerHTML = `Last Update: ${questionDateUpdated}`;
            document.querySelector(".question-view-update-count").innerHTML = `Update Count: ${questionUpdateCount}`;

            // set the correct class for the difficulty
            const questionDifficultyElement = document.querySelector(".question-view-difficulty");

            // list of classes
            const DIFFICULTYCLASSLIST = ["question-easy", "question-medium", "question-hard", "question-insane", "question-none"];

            // remove the class
            for (difficulty of DIFFICULTYCLASSLIST) {
                questionDifficultyElement.classList.remove(`${difficulty}`);
            }

            // add the correct class
            switch (questionCard.getAttribute("data-difficulty")) {
                case "-1":
                    questionDifficultyElement.classList.add(`question-none`);
                    break;
                case "0":
                    questionDifficultyElement.classList.add(`question-easy`);
                    break;
                case "1":
                    questionDifficultyElement.classList.add(`question-medium`);
                    break;
                case "2":
                    questionDifficultyElement.classList.add(`question-hard`);
                    break;
                case "3":
                    questionDifficultyElement.classList.add(`question-insane`);
                    break;
            }         

        })

    }

}
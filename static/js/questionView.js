/**
 * run on page load
 */
document.addEventListener("DOMContentLoaded", function() {
    
    viewQuestion()

})

/**
 * add event listeners and functionality to all view buttons
 */
function viewQuestion() {

    const questionButtons = document.getElementsByClassName("question-view-button");

    for (let questionButton of questionButtons) {
        
        questionButton.addEventListener("click", function() {
            
            // get the question card
            const questionCard = this.parentElement.parentElement.parentElement;
            
            // get the content from the card
            const questionTitle = questionCard.querySelector(".question-title").textContent;
            const questionSubtitle = questionCard.querySelector(".question-subtitle").textContent;
            const questionContent = questionCard.querySelector(".question-content").textContent;
            const questionDifficulty = questionCard.querySelector(".question-difficulty").textContent;
            const questionSummary = questionCard.querySelector(".question-summary").textContent;

            // get the content from the data attributes
            const questionID = questionCard.getAttribute("data-id");
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
            document.querySelector(".question-view-id").setAttribute("data-id", questionID)
            document.querySelector(".question-view-summary").innerHTML = questionSummary;

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
            
            // stop the edit window being clickable until a question is clicked
            setEditData()

        })
    }
}


/**
 * add event listener to the edit buttons, and set the data in the form
 * this goes inside the function for viewing a question, incase the user somehow clicks on the edit button without first choosing a question to edit
 */
function setEditData() {

    const editButton = document.querySelector(".question-edit-button");

    editButton.addEventListener("click", function () {

        // get data from the question
        // not all of this is used for now, but it will be when a preview is added.
        const questionTitle = document.querySelector(".question-view-title").textContent;
        const questionSubtitle = document.querySelector(".question-view-subtitle").textContent;
        const questionContent = document.querySelector(".question-view-content").textContent;
        const questionDifficulty = document.querySelector(".question-view-difficulty").textContent.trim();
        const questionDateCreated = document.querySelector(".question-view-date-created").textContent;
        const questionDateUpdated = document.querySelector(".question-view-date-updated").textContent;
        const questionUpdateCount = document.querySelector(".question-view-update-count").textContent;
        const questionID = document.querySelector(".question-view-id").getAttribute("data-id");
        const questionSummary = document.querySelector(".question-view-summary").textContent;

        // set the text in the question

        // first get the correct form
        questionEditModal = document.getElementById("question-edit-modal");

        // set data
        questionEditModal.querySelector(".question-edit-title").setAttribute("value", questionTitle);
        questionEditModal.querySelector(".question-edit-summary").setAttribute("value", questionSummary);
        questionEditModal.querySelector(".question-edit-content").textContent = questionContent;

        switch(questionDifficulty) {
            case "Easy":
                questionEditModal.querySelector(".question-edit-difficulty [value='0']").selected = true;
                break;
            case "Medium":
                questionEditModal.querySelector(".question-edit-difficulty [value='1']").selected = true;
                break;
            case "Hard":
                questionEditModal.querySelector(".question-edit-difficulty [value='2']").selected = true;
                break;
            case "Insane":
                questionEditModal.querySelector(".question-edit-difficulty [value='3']").selected = true;
                break;
        }

    })

}
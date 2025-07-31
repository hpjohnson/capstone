// html for the modal
const MODALHTML = `
                <div class="modal-header">
                    <h2 id="question-view-modal-label" class="display-6 modal-title">{TITLE}</h2>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="close"></button>
                </div>
                <div class="modal-body">
                    <p>{CREATEDBY}</p>
                    <p>{DIFFICULTY}</p>
                    <p>{CONTENT}</p>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-primary" data-bs-dismiss="modal">Close</button>
                </div>`;


/**
 * only run on page load
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
            const questionCard = this.parentElement.parentElement;
            // get the content from the card
            const questionTitle = questionCard.getElementsByClassName("question-title")[0].textContent;
            const questionSubtitle = questionCard.getElementsByClassName("question-subtitle")[0].textContent;
            const questionSummary = questionCard.getElementsByClassName("question-summary")[0].textContent;
            const questionContent = questionCard.getElementsByClassName("question-content")[0].textContent;
            let questionDifficulty = questionCard.getElementsByClassName("question-difficulty")[0].textContent;
            switch (questionDifficulty) {
                case "-1":
                    questionDifficulty = "None Specified";
                case "0":
                    questionDifficulty = "Easy";
                case "1":
                    questionDifficulty = "Medium";
                case "2":
                    questionDifficulty = "Hard";
                case "3":
                    questionDifficulty = "Insane"; 
            }
            const questionCreatedOn = questionCard.getElementsByClassName("question-created-on")[0].textContent;
            const questionUpdatedOn = questionCard.getElementsByClassName("question-updated-on")[0].textContent;
            const questionUpdateCount = questionCard.getElementsByClassName("question-updated-on")[0].textContent;
            const questionID = questionCard.getAttribute("data-id");

            // get the modal
            const questionModal = document.getElementById("question-view-modal-content");
            // set and replace the content
            questionModal.innerHTML = MODALHTML.replace("{TITLE}", questionTitle).replace("{CREATEDBY}", questionSubtitle).replace("{DIFFICULTY}", questionDifficulty).replace("{CONTENT}", questionContent);
            

            //console.log(questionTitle);

        })

    }

}
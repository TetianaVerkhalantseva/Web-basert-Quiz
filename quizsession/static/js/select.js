function selectQuestion(questionId) {

    var questionNumbers = document.getElementById("question-numbers").children;

    for (var i = 0; i < questionNumbers.length; i++) {
        questionNumbers[i].classList.remove("selected");
    }

    var questionNumberElement = document.getElementById("question-" + questionId);
    questionNumberElement.classList.add("selected");

    var questionContainers = document.getElementsByClassName("question-container");

    for (var i = 0; i < questionContainers.length; i++) {
        questionContainers[i].style.display = "none";
    }

    var questionContainer = document.getElementById("question-container-" + questionId);
    questionContainer.style.display = "block";

}

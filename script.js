// Function to send POST requests
async function postData(url = "", data = {}) {
    const response = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    });
    return response.json();
}

// Adding event listener for the send button
document.addEventListener("DOMContentLoaded", () => {
    const sendButton = document.getElementById("sendButton");
    const questionInput = document.getElementById("question");
    const right1 = document.querySelector(".right1");
    const right2 = document.querySelector(".right2");
    const question1 = document.getElementById("question1");
    const question2 = document.getElementById("question2");
    const solution = document.getElementById("solution");
    
    sendButton.addEventListener("click", async () => {
    const questionText = questionInput.value.trim();
    
    if (questionText === "") {
    alert("Please enter a message Maharaj.");
    return;
    }
    
    // Clear input and show loading state
    questionInput.value = "";
    right1.style.display = "none";
    right2.style.display = "block";
    question1.innerHTML = "Loading...";
    question2.innerHTML = "Loading...";
    solution.innerHTML = "Thinking...";
    
    // Populate the question
    question1.innerHTML = questionText;
    question2.innerHTML = questionText;
    
    
    let result = await postData("/api", {"question": questionInput})
    solution.innerHTML = result.answer
    
    
    });
    });
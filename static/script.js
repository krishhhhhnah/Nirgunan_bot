const welcomeScreen =
    document.getElementById("welcome-screen");

const chatScreen =
    document.getElementById("chat-screen");

const meetButton =
    document.getElementById("meet-button");

const chatForm =
    document.getElementById("chat-form");

const userInput =
    document.getElementById("user-input");

const chatMessages =
    document.getElementById("chat-messages");

const randomButton =
    document.getElementById("random-button");

const clearButton =
    document.getElementById("clear-button");

const modeButton =
    document.getElementById("mode-button");

const modePanel =
    document.getElementById("mode-panel");

const modeOptions =
    document.querySelectorAll(".mode-option");


let currentMode = "USELESS";


/* =====================================================
   MEET NIRGUNAN
===================================================== */

meetButton.addEventListener("click", () => {

    welcomeScreen.style.opacity = "0";

    welcomeScreen.style.transform =
        "scale(1.04)";

    setTimeout(() => {

        welcomeScreen.classList.add("hidden");

        chatScreen.classList.remove("hidden");

        chatScreen.style.opacity = "0";

        requestAnimationFrame(() => {

            chatScreen.style.opacity = "1";

            userInput.focus();

        });

    }, 1000);

});


/* =====================================================
   MODE
===================================================== */

modeButton.addEventListener("click", (event) => {

    event.stopPropagation();

    modePanel.classList.toggle("hidden");

});


modeOptions.forEach(option => {

    option.addEventListener("click", () => {

        modeOptions.forEach(item => {

            item.classList.remove("active");

        });

        option.classList.add("active");

        currentMode =
            option.dataset.mode;

        modePanel.classList.add("hidden");

    });

});


document.addEventListener("click", () => {

    modePanel.classList.add("hidden");

});


/* =====================================================
   ADD MESSAGE
===================================================== */

function addMessage(sender, text) {

    const message =
        document.createElement("div");

    message.classList.add("message");


    if (sender === "user") {

        message.classList.add("user");

        message.innerHTML = `

            <div class="label">
                YOU
            </div>

            <div class="text">
                ${escapeHTML(text)}
            </div>

        `;

    } else {

        message.classList.add("nirgunan");

        message.innerHTML = `

            <div class="label">
                NIRGUNAN
            </div>

            <div class="text">
                ${escapeHTML(text)}
            </div>

        `;

    }


    chatMessages.appendChild(message);

    chatMessages.scrollTop =
        chatMessages.scrollHeight;

}


/* =====================================================
   TYPING
===================================================== */

function showTyping() {

    const typing =
        document.createElement("div");

    typing.id =
        "typing-indicator";

    typing.className =
        "message nirgunan";

    typing.innerHTML = `

        <div class="label">
            NIRGUNAN
        </div>

        <div class="text">
            <span class="typing-dots">
                · · ·
            </span>
        </div>

    `;

    chatMessages.appendChild(typing);

    chatMessages.scrollTop =
        chatMessages.scrollHeight;

}


function removeTyping() {

    const typing =
        document.getElementById(
            "typing-indicator"
        );

    if (typing) {

        typing.remove();

    }

}


/* =====================================================
   CHAT
===================================================== */

chatForm.addEventListener(
    "submit",
    async (event) => {

        event.preventDefault();


        const question =
            userInput.value.trim();


        if (!question) {

            return;

        }


        addMessage(
            "user",
            question
        );


        userInput.value = "";


        showTyping();


        try {

            const response =
                await fetch(
                    "/chat",
                    {

                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({

                            message: question,

                            mode:
                                currentMode

                        })

                    }
                );


            const data =
                await response.json();


            removeTyping();


            addMessage(
                "nirgunan",
                data.response ||
                "Nirgunan has forgotten how to be useless."
            );


        } catch (error) {

            console.error(error);

            removeTyping();


            addMessage(
                "nirgunan",
                "My brain has disappeared. Check whether Ollama is running."
            );

        }

    }
);


/* =====================================================
   ENTER KEY
===================================================== */

userInput.addEventListener(
    "keydown",
    (event) => {

        if (
            event.key === "Enter" &&
            !event.shiftKey
        ) {

            event.preventDefault();

            chatForm.requestSubmit();

        }

    }
);


/* =====================================================
   CLEAR
===================================================== */

clearButton.addEventListener(
    "click",
    () => {

        chatMessages.innerHTML = "";

        addMessage(
            "nirgunan",
            "Conversation deleted. A historic moment of absolutely no importance."
        );

    }
);


/* =====================================================
   RANDOM QUESTIONS
===================================================== */

const randomQuestions = [

    "What is the meaning of life?",

    "Why am I always tired?",

    "Why does Monday exist?",

    "Can a potato become an engineer?",

    "Why do socks disappear?",

    "What should I do with my life?",

    "Is water actually wet?",

    "Why do humans need money?",

    "Can I become successful by doing nothing?",

    "Who invented homework?",

    "Why is my WiFi slow?",

    "What is your greatest achievement?",

    "Why do I procrastinate?"

];


randomButton.addEventListener(
    "click",
    () => {

        const index =
            Math.floor(
                Math.random() *
                randomQuestions.length
            );


        userInput.value =
            randomQuestions[index];


        userInput.focus();

    }
);


/* =====================================================
   SECURITY
===================================================== */

function escapeHTML(text) {

    const element =
        document.createElement("div");

    element.textContent = text;

    return element.innerHTML;

}
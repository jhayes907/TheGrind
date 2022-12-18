const usernameField = document.querySelector("#usernameField");
const feedBackArea = document.querySelector(".invalid-feedback");
const emailField = document.querySelector("#emailField");
const emailFeedBackArea = document.querySelector(".emailFeedBackArea");
const passwordField = document.querySelector("#passwordField");
const usernameSuccessOutput = document.querySelector(".usernameSuccessOutput");
const showPasswordToggle = document.querySelector(".showPasswordToggle");
const submitBtn = document.querySelector(".submitBtn")

const handleToggleInput = (e) => {
  if (showPasswordToggle.textContent === "SHOW") {
    showPasswordToggle.textContent = "HIDE";
    passwordField.setAttribute("type", "text");
  } else {
    showPasswordToggle.textContent = "SHOW";
    passwordField.setAttribute("type", "password");
  }
};

showPasswordToggle.addEventListener('click', handleToggleInput);

usernameField.addEventListener("keyup", (e) => {
  const usernameVal = e.target.value;
  usernameSuccessOutput.textContent = `Checking ${usernameVal}`;
  usernameSuccessOutput.style.display = "block";
  usernameField.classList.remove("is-valid");
  feedBackArea.style.display = "none";
  
  if (usernameVal.length > 0) {
    fetch("/authentication/validate-username/", {
      body: JSON.stringify({ username: usernameVal }),
      method: "POST",
    })
    .then((res) => res.json())
    .catch((err) => {
      console.log("error", err);
    })
    .then((data) => {
      console.log("data", data);
      usernameSuccessOutput.style.display = "none";
      if(data.username_error) {
        usernameField.classList.add("is-invalid");
        feedBackArea.style.display="block";
        feedBackArea.innerHTML=`<p>${data.username_error}</p>`;
        submitBtn.disabled=true;
      } else {
        submitBtn.removeAttribute("disabled");
      }
    });
  }
});

emailField.addEventListener("keyup", (e) => {
  const emailVal = e.target.value;
  
  emailField.classList.remove("is-valid");
  emailFeedBackArea.style.display = "none";
  
  if (emailVal.length > 0) {
    fetch("/authentication/validate-email/", {
      body: JSON.stringify({ email: emailVal }),
      method: "POST",
    })
    .then((res) => res.json())
    .catch((err) => {
      console.log("error", err);
    })
    .then((data) => {
      console.log("data", data);
      if(data.email_error) {
        submitBtn.disabled=true;
        emailField.classList.add("is-invalid");
        emailFeedBackArea.style.display="block";
        emailFeedBackArea.innerHTML=`<p>${data.email_error}</p>`;
      } else {
        submitBtn.removeAttribute("disabled");
      }
    });
  }
});


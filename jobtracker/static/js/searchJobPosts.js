const searchField=document.querySelector('#searchField');

searchField.addEventListener('keyup', () => {
    const searchValue = e.target.value;

    if(searchValue.length > 0) {
        console.log('object', object)

        fetch("jobs/search-jobs/", {
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
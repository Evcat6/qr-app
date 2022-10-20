let button = document.getElementById("btn");
let notificator = document.getElementById("message")


window.addEventListener("resize", function(){
    window.resizeTo(400, 300);
    });



button.addEventListener("click", async() => { 
    content = document.getElementById("input").value;
    console.log(document.getElementById("input").value);
    eel.message_returner(content)((value) => {
        if(value === "Qr code saved successfully!") {
            notificator.style.color = "green";
        } else if (value === "Please type something to input!") {
            notificator.style.color = "red";
        }
        notificator.innerHTML = value;
    })
    eel.get_element(content);
})
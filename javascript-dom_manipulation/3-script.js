let header = document.querySelector("header");
const toggle_header = document.getElementById("toggle_header");

toggle_header.addEventListener("click", () => {
    if (header.classList.toggle("green")) {
        header.classList.add("red");
    } else {
        header.classList.add("red");
    }
})

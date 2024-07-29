let header = document.querySelector("header");

let update_header = document.getElementById("update_header");

update_header.addEventListener("click", () => {
    header.innerHTML = "New Header!!!";
})

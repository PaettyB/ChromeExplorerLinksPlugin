let url = window.location.href;

let parentDiv = document.getElementById("parentDirLinkBox");

let btn = document.createElement("button");
btn.addEventListener("click", () => window.location.href = "custom"+url);

btn.innerText = "Open in Explorer"

btn.style.height = "100%";
btn.style.marginLeft = "20px";
btn.style.backgroundColor = "#162570";

parentDiv.appendChild(btn);

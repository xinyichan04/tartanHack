links = document.querySelectorAll(".menu > div");

links[1].addEventListener("click", () => {
	if (links[1].classList.contains("selected")) return;
	window.location.href = "meditate";
});

links[2].addEventListener("click", () => {
	if (links[2].classList.contains("selected")) return;
	window.location.href = "about-us";
});

links[3].addEventListener("click", () => {
	if (links[3].classList.contains("selected")) return;
	window.location.href = "faq";
});

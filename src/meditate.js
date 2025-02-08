const env = document.getElementsByClassName("environment")[0];
const goal = document.getElementsByClassName("goal")[0];
const gender = document.getElementsByClassName("gender")[0];
function clickHandler(el, e) {
	if (e.target === el) return;
	let target = e.target;
	while (target.parentNode !== el) target = target.parentNode;
	el.querySelector(".selected").classList.remove("selected");
	target.classList.add("selected");
}

env.addEventListener("click", clickHandler.bind(null, env));
goal.addEventListener("click", clickHandler.bind(null, goal));
gender.addEventListener("click", clickHandler.bind(null, gender));

document.getElementsByClassName("start")[0].addEventListener("click", () => {
	fetch("/api/text/submit-preferences", {
		method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
		body: JSON.stringify({
			environment: env
				.querySelector(".selected")
				.className.split("selected")
				.filter((el) => el.trim() !== "")[0],
			goal: goal
				.querySelector(".selected")
				.className.split("selected")
				.filter((el) => el.trim() !== "")[0],
			gender: gender
				.querySelector(".selected")
				.className.split("selected")
				.filter((el) => el.trim() !== "")[0],
		}),
	});
});

document.addEventListener("DOMContentLoaded", () => {
	const questions = document.querySelectorAll(".faq-question");

	for (const question of questions) {
		question.addEventListener("click", () => {
			const answer = question.nextElementSibling;
			answer.style.display =
				answer.style.display === "block" ? "none" : "block";
		});
	}
});

document.addEventListener("DOMContentLoaded", () => {
	const questions = document.querySelectorAll(".faq-question");

	// biome-ignore lint/complexity/noForEach: <explanation>
	for (const question of questions) {
		question.addEventListener("click", () => {
			const answer = question.nextElementSibling;
			answer.style.display =
				answer.style.display === "block" ? "none" : "block";
		});
	}
});

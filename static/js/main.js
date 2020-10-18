document.querySelectorAll('.alert').forEach(msg => {
	if (msg.classList.contains('field-error')) {
		msg.nextElementSibling.addEventListener('keydown', () => {
			msg.style.display = 'none'
		})
	} else {
		setTimeout(() => {
				msg.style.display = 'none'
		}, 3000)
	}
})


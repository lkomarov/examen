document.getElementById('signup').addEventListener('submit', function(event) {
    event.preventDefault();
    const name = document.getElementById('name').value;
    const lastName = document.getElementById('last-name').value;
    const email = document.getElementById('new-email').value;
    const password = document.getElementById('new-password').value;
    // Validar que se ingresen valores para todos los campos obligatorios
    if (!name || !lastName || !email || !password) {
        alert('Por favor, completa todos los campos.');
        return;
    }

    const data = { name: name, lastName: lastName, email: email, password: password };

    fetch('/api/signup', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Registro exitoso');
            window.location.href = '/login.html';
        } else {
            alert('Error en el registro: ' + data.message);
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
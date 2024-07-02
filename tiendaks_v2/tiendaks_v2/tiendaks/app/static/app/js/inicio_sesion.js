document.getElementById('login').addEventListener('submit', function(event) {
    event.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    // Validar que se ingresen valores para correo electrónico y contraseña
    if (!email || !password) {
        alert('Por favor, ingresa tu correo electrónico y contraseña.');
        return;
    }

    const data = { email: email, password: password };

    fetch('/api/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Inicio de sesión exitoso');
            window.location.href = '/dashboard.html';
        } else {
            alert('Error en el inicio de sesión: ' + data.message);
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
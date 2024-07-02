function agregarProducto(nombreProducto) {
    if (nombreProducto.trim() === "") {
        alert("Por favor, ingresa un nombre válido para el producto.");
        return; // Salir de la función si el nombre del producto no es válido
    }

    var carrito = document.getElementById('carrito');
    var nuevoElemento = document.createElement('li');
    nuevoElemento.textContent = nombreProducto;
    nuevoElemento.innerHTML += ' <button onclick="eliminarProducto(this)">Eliminar</button>';
    carrito.appendChild(nuevoElemento);
}
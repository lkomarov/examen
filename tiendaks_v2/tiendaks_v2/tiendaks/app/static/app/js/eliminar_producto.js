function eliminarProducto(botonEliminar) { if (botonEliminar.parentElement && botonEliminar.parentElement.parentElement &&
    botonEliminar.parentElement.parentElement.id === 'carrito') {
    var itemEliminar = botonEliminar.parentElement;
    itemEliminar.parentElement.removeChild(itemEliminar);
} else {
    console.error("El elemento a eliminar no pertenece al carrito.");
}
}
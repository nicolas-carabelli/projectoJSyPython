// Obtener el elemento canvas
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

// Variables para la pintura
let lastX, lastY;
let drawing = false;

// Evento de movimiento del cursor
canvas.addEventListener('mousemove', (event) => {
  // Obtener las coordenadas del cursor
  const x = event.clientX;
  const y = event.clientY;

  // Si el usuario está dibujando
  if (drawing) {
    // Dibujar un punto en la posición actual del cursor
    ctx.beginPath();
    ctx.arc(x, y, 5, 0, 2 * Math.PI);
    ctx.fillStyle = 'black';
    ctx.fill();
  }

  // Actualizar las coordenadas del cursor
  lastX = x;
  lastY = y;
});

// Evento de click para iniciar la pintura
canvas.addEventListener('mousedown', () => {
  drawing = true;
});

// Evento de liberación del botón para detener la pintura
canvas.addEventListener('mouseup', () => {
  drawing = false;
});

// Evento de liberación del botón para detener la pintura
canvas.addEventListener('mouseout', () => {
  drawing = false;
});

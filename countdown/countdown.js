// Establece la fecha de lanzamiento del álbum
const releaseDate = new Date('April 19, 2024 00:00:00').getTime();

// Actualiza la cuenta regresiva cada segundo
const interval = setInterval(function() {
    // Obtiene la fecha y hora actual
    const now = new Date().getTime();

    // Encuentra la distancia entre ahora y la fecha de lanzamiento
    const distance = releaseDate - now;

    // Cálculos de tiempo para días, horas, minutos y segundos
    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    // Muestra el resultado en los elementos con id="days", "hours", "minutes" y "seconds"
    document.getElementById('days').innerText = days;
    document.getElementById('hours').innerText = hours;
    document.getElementById('minutes').innerText = minutes;
    document.getElementById('seconds').innerText = seconds;

    // Si la cuenta regresiva termina, escribe algún texto
    if (distance < 0) {
        clearInterval(interval);
        document.getElementById('countdown').innerHTML = "¡El álbum ha sido lanzado!";
    }
}, 1000);
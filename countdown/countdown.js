/**
 * Establece la fecha de lanzamiento del álbum y actualiza la cuenta regresiva cada segundo.
 * Muestra el tiempo restante en días, horas, minutos y segundos en los elementos HTML correspondientes.
 * Cuando la cuenta regresiva termina, muestra un mensaje indicando que el álbum ha sido lanzado.
 */
const releaseDate = new Date('April 19, 2024 00:00:00').getTime(); // Fecha de lanzamiento del álbum


const interval = setInterval(function() { // Inicia un intervalo que se ejecuta cada segundo
    const now = new Date().getTime(); // Obtiene la fecha y hora actual

    const distance = releaseDate - now;  // Calcula la distancia entre la fecha actual y la de lanzamiento

    // Cálculos de tiempo para días, horas, minutos y segundos
    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    // Actualiza los elementos HTML con los valores calculados
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
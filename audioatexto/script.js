/**
 * Una aplicación para tomar el audio del micrófono y convertilo en texto
 * Cuenta con dos botones para comenzar a capturar el audio y detener la captura.
 * Preparado para funcionar en navegador Chrome
 */
var startButton = document.getElementById('start');
var stopButton = document.getElementById('stop');
var resultElement = document.getElementById('result');

// Utilizamos API de reconocimiento de voz para Chrome
var recognition = new webkitSpeechRecognition();
// Configuramos que el lenguaje de renocimiento sea el mismo que el del navegador
recognition.lang = window.navigator.language;
recognition.interimResults = true;

// Manejadores para los botones de comenzar y detener
startButton.addEventListener('click', () => { recognition.start(); });
stopButton.addEventListener('click', () => { recognition.stop(); });

// Manejador de eventoz cuando se reconoce la voz y procesa lo hablado
recognition.addEventListener('result', (event) => {
    const result = event.results[event.results.length - 1][0].transcript;
    resultElement.textContent = result;
});
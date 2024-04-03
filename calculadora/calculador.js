function calcularIngresos() {
    var salarioBase = document.getElementById('salarioBase').value;
    var comisiones = document.getElementById('comisiones').value;

    // Convertir a números
    salarioBase = parseFloat(salarioBase);
    comisiones = parseFloat(comisiones);

    // Calcular ingresos totales
    var ingresosTotales = salarioBase + comisiones;

    // Mostrar el resultado
    document.getElementById('ingresosTotales').value = ingresosTotales.toFixed(2);
}
function limpiar() {
    document.getElementById("formulario").reset();
    document.getElementById("rut").focus();
}

function enviarDatos() {
    let rut = document.getElementById("rut").value;
    let nombre = document.getElementById("nom").value;
    let apellidoPaterno = document.getElementById("ap").value;
    let apellidoMaterno = document.getElementById("am").value;
    let correo = document.getElementById("correo").value;
    let celular = document.getElementById("celu").value;
    let fechaNacimiento = document.getElementById("fecha").value;
    let genero = document.getElementById("genero").value;
    let comuna = document.getElementById("comuna").value;
    let licenciaConducir = document.querySelector('input[name="vehi"]:checked');

    if (rut && nombre && apellidoPaterno && apellidoMaterno && correo && celular && fechaNacimiento && genero && comuna && licenciaConducir) {
 
        if (!/^[0-9]{9}$/.test(rut)) {
            alert("El RUT debe contener exactamente 9 números.");
            return;
        }
        if (!/^[a-zA-Z\s]+$/.test(nombre)) {
            alert("El nombre no puede contener números.");
            return;
        }
        if (!/^[a-zA-Z\s]+$/.test(apellidoPaterno)) {
            alert("El apellido paterno no puede contener números.");
            return;
        }
        if (!/^[a-zA-Z\s]+$/.test(apellidoMaterno)) {
            alert("El apellido materno no puede contener números.");
            return;
        }
        if (!/^[0-9]{9}$/.test(celular)) {
            alert("El número celular debe contener exactamente 9 números.");
            return;
        }
        if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(correo)) {
            alert("El correo NO es valido");
            return;
        }

        let hoy = new Date();
        let fechaNacimientoDate = new Date(fechaNacimiento);
        let edad = hoy.getFullYear() - fechaNacimientoDate.getFullYear();
        let mes = hoy.getMonth() - fechaNacimientoDate.getMonth();
        if (mes < 0 || (mes === 0 && hoy.getDate() < fechaNacimientoDate.getDate())) {
            edad--;
        }

        if (edad < 18) {
            alert("Debes ser mayor de edad para postular.");
        } else {
            alert("Datos enviados correctamente.");
        }
    } else {
        alert("Por favor complete todos los campos del formulario.");
    }
}

function mostrarPrecios(){
    let url='http://localhost:3300/galones';
    fetch(url)
    .then(response => response.json())
    .then(data => mostrarPreciosData(data))
    .catch(error => console.log(error))

    const mostrarPreciosData = (data) => {
        console.log(data)
        let texto = ""
        for (var i = 0; i < data.length; i++) {
            texto += `<tr>
                <td>${data[i].id}</td>
                <td>${data[i].kg}</td>
                <td>${data[i].marca}</td>
                <td>${data[i].precio}</td>
            </tr>`
        }
        document.getElementById('galones').innerHTML = texto;
    }
}

function buscarMarca(){
    let url='http://localhost:3300/galones';
    let tipo = document.getElementById('marca').value;
    fetch(url)
    .then(response => response.json())
    .then(data => buscarMarcaData(data))
    .catch(error => console.log(error))

    const buscarMarcaData = (data) => {
        console.log(data)
        let texto = ""
        if (document.getElementById('marca').selectedIndex == 0){
            mostrarPrecios();
        } else {
            for (var i = 0; i < data.length; i++) {
                if (tipo == data[i].marca) {
                    texto += `<tr>
                        <td>${data[i].id}</td>
                        <td>${data[i].kg}</td>
                        <td>${data[i].marca}</td>
                        <td>${data[i].precio}</td>
                    </tr>`
                }
            }
            document.getElementById('galones').innerHTML = texto;
        }
    }
}

document.addEventListener("DOMContentLoaded", function() {
    const preguntaEjemplo = {
        id: 1,
        question: "¿Cuál es tu marca de gas preferida?",
        options: ["Abastible", "Gasco", "Lipigas", "Otra"]
    };

    mostrarPregunta(preguntaEjemplo);

    function mostrarPregunta(pregunta) {
        document.getElementById('pregunta').innerHTML = `<p>${pregunta.question}</p>`;
        
        const respuestas = document.getElementById('respuestas');
        respuestas.innerHTML = ''; 

        pregunta.options.forEach((opcion, index) => {
            respuestas.innerHTML += `
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="respuesta" id="respuesta${index}" value="${opcion}">
                    <label class="form-check-label" for="respuesta${index}">
                        ${opcion}
                    </label>
                </div>
            `;
        });
    }

    document.getElementById('enviarRespuesta').addEventListener('click', enviarRespuesta);
});

function enviarRespuesta() {
    const respuesta = document.querySelector('input[name="respuesta"]:checked');
    if (respuesta) {
        alert(`¡Gracias por tu respuesta!\nHas seleccionado: ${respuesta.value}`);
    } else {
        alert('Por favor selecciona una respuesta antes de enviar.');
    }
}
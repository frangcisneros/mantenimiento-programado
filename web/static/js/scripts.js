// const apiBaseUrl = "http://localhost:8000/api";

// // Crear máquina
// document
// 	.getElementById("create-machine-form")
// 	.addEventListener("submit", async (e) => {
// 		e.preventDefault();
// 		const tipoMaquina = document.getElementById("tipoMaquina").value;

// 		const response = await fetch(`${apiBaseUrl}/maquinas/`, {
// 			method: "POST",
// 			headers: {
// 				"Content-Type": "application/json",
// 			},
// 			body: JSON.stringify({ tipoMaquina }),
// 		});

// 		if (response.ok) {
// 			alert("Máquina creada exitosamente");
// 			cargarPiezas(); // Cargar piezas después de crear la máquina
// 		} else {
// 			alert("Error al crear la máquina");
// 		}
// 	});

// // Cargar piezas
// async function cargarPiezas() {
// 	const response = await fetch(`${apiBaseUrl}/piezas/`);
// 	const piezas = await response.json();

// 	const piezasContainer = document.getElementById("piezas-container");
// 	piezasContainer.innerHTML = "";

// 	piezas.forEach((pieza) => {
// 		const piezaElement = document.createElement("div");
// 		piezaElement.textContent = `ID: ${pieza.idPieza}, Tipo: ${pieza.tipoPieza}`;
// 		piezasContainer.appendChild(piezaElement);
// 	});
// }

// // Agregar nueva pieza
// document
// 	.getElementById("add-piece-button")
// 	.addEventListener("click", async () => {
// 		const tipoPieza = prompt("Ingrese el tipo de pieza:");
// 		if (!tipoPieza) return;

// 		const response = await fetch(`${apiBaseUrl}/piezas/`, {
// 			method: "POST",
// 			headers: {
// 				"Content-Type": "application/json",
// 			},
// 			body: JSON.stringify({ tipoPieza }),
// 		});

// 		if (response.ok) {
// 			alert("Pieza creada exitosamente");
// 			cargarPiezas();
// 		} else {
// 			alert("Error al crear la pieza");
// 		}
// 	});

// // Inicializar
// cargarPiezas();

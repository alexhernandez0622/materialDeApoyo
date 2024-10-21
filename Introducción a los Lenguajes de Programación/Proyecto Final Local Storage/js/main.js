$(document).ready(function () {
    // Inicializar almacenamiento local para paquetes turísticos, reservas y clientes
    const initLocalStorage = (key) => {
        if (!localStorage.getItem(key)) {
            localStorage.setItem(key, JSON.stringify([]));
        }
    };
    initLocalStorage('packages');
    initLocalStorage('reservations');
    initLocalStorage('customers');

    // Datos predefinidos
    const hotels = ['Hotel Plaza', 'Hotel Luxury', 'Hotel Boutique'];
    const services = ['Desayuno', 'WiFi', 'Transporte', 'Guía Turístico' , 'Todo Incluído'];
    const packageTypes = ['Todo Incluido', 'Solo Alojamiento', 'Aventura', 'Cultural'];

    // Función para generar opciones de select
    const generateOptions = (items) => items.map(item => `<option value="${item}">${item}</option>`).join('');

    // Función para mostrar alertas de SweetAlert2
    const showAlert = (title, text, icon = 'info') => {
        Swal.fire({ title, text, icon });
    };

    // Función para crear un paquete turístico
    $('#btn-create-package').click(() => {
        Swal.fire({
            title: 'Crear Paquete Turístico',
            html: `
                <input type="text" id="package-name" class="swal2-input" placeholder="Nombre del Paquete">
                <input type="text" id="package-destination" class="swal2-input" placeholder="Destino">
                <select id="package-type" class="swal2-select">
                    <option value="" disabled selected>Selecciona el Tipo de Paquete</option>
                    ${generateOptions(packageTypes)}
                </select>
                <select id="package-hotel" class="swal2-select">
                    <option value="" disabled selected>Selecciona el Hotel</option>
                    ${generateOptions(hotels)}
                </select>
                <select id="package-services" class="swal2-select" multiple>
                    <option value="" disabled>Selecciona los Servicios Incluidos</option>
                    ${generateOptions(services)}
                </select>
                <input type="number" id="package-price" class="swal2-input" placeholder="Precio">
                <input type="text" id="package-stay" class="swal2-input" placeholder="Estadía (días)">
            `,
            confirmButtonText: 'Guardar',
            preConfirm: () => {
                const name = $('#package-name').val();
                const destination = $('#package-destination').val();
                const type = $('#package-type').val();
                const hotel = $('#package-hotel').val();
                const services = $('#package-services').val(); // Devuelve un array de servicios seleccionados
                const price = $('#package-price').val();
                const stay = $('#package-stay').val();
    
                if (!name || !destination || !type || !hotel || !price || !stay) {
                    Swal.showValidationMessage('Todos los campos son requeridos');
                    return false;
                }
    
                const packages = JSON.parse(localStorage.getItem('packages')) || [];
                packages.push({ name, destination, type, hotel, services, price, stay });
                localStorage.setItem('packages', JSON.stringify(packages));
                return { name, destination, type, hotel, services, price, stay };
            }
        }).then((result) => {
            if (result.isConfirmed) {
                showAlert('Paquete Creado', `Paquete ${result.value.name} creado exitosamente!`);
                updateTable('packages');
            }
        });
    });
    
    
    // Función para buscar un paquete turístico
    $('#btn-search-package').click(() => {
        Swal.fire({
            title: 'Buscar Paquete Turístico',
            input: 'text',
            inputPlaceholder: 'Ingrese el nombre del paquete',
            showCancelButton: true,
            confirmButtonText: 'Buscar',
        }).then((result) => {
            if (result.isConfirmed) {
                const packages = JSON.parse(localStorage.getItem('packages'));
                const foundPackage = packages.find(pkg => pkg.name.toLowerCase() === result.value.toLowerCase());

                if (foundPackage) {
                    showAlert('Paquete Encontrado', `Paquete: ${foundPackage.name}, Destino: ${foundPackage.destination}, Precio: $${foundPackage.price}`, 'success');
                } else {
                    showAlert('Error', 'No se encontró ningún paquete con ese nombre', 'error');
                }
            }
        });
    });


    $('#btn-create-reservation').click(() => {
        Swal.fire({
            title: 'Crear Reserva',
            html: `
                <input type="text" id="reservation-customer" class="swal2-input" placeholder="Nombre del Cliente">
                <input type="number" id="reservation-users" class="swal2-input" placeholder="Número de Usuarios">
                <input type="text" id="reservation-package" class="swal2-input" placeholder="Nombre del Paquete">
                <textarea id="reservation-names" class="swal2-textarea" placeholder="Nombres de las Personas (separados por coma)"></textarea>
                <input type="checkbox" id="reservation-children"> <label for="reservation-children">¿Viajan niños?</label><br>
                <input type="date" id="reservation-departure" class="swal2-input" placeholder="Fecha de Salida">
                <input type="date" id="reservation-return" class="swal2-input" placeholder="Fecha de Regreso">
            `,
            confirmButtonText: 'Guardar',
            preConfirm: () => {
                const customer = $('#reservation-customer').val();
                const users = $('#reservation-users').val();
                const package = $('#reservation-package').val();
                const names = $('#reservation-names').val().split(',').map(name => name.trim());
                const children = $('#reservation-children').is(':checked');
                const departure = $('#reservation-departure').val();
                const returnDate = $('#reservation-return').val();

                if (!customer || !users || !package || !names.length || !departure || !returnDate) {
                    Swal.showValidationMessage('Todos los campos son requeridos');
                    return false;
                }

                const reservations = getLocalStorageData('reservations');
                reservations.push({ customer, users, package, names, children, departure, returnDate });
                updateLocalStorage('reservations', reservations);
                return { customer, users, package, names, children, departure, returnDate };
            }
        }).then((result) => {
            if (result.isConfirmed) {
                showAlert('Reserva Creada', `Reserva creada para ${result.value.customer} exitosamente!`);
                updateTable('reservations');
            }
        });
    });

    $('#btn-manage-customers').click(() => {
        Swal.fire({
            title: 'Agregar Cliente',
            html: `
                <input type="text" id="customer-name" class="swal2-input" placeholder="Nombre del Cliente">
                <input type="email" id="customer-email" class="swal2-input" placeholder="Email">
                <input type="text" id="customer-phone" class="swal2-input" placeholder="Teléfono">
            `,
            confirmButtonText: 'Guardar',
            preConfirm: () => {
                const name = $('#customer-name').val();
                const email = $('#customer-email').val();
                const phone = $('#customer-phone').val();

                if (!name || !email || !phone) {
                    Swal.showValidationMessage('Todos los campos son requeridos');
                    return false;
                }

                const customers = getLocalStorageData('customers');
                customers.push({ name, email, phone });
                updateLocalStorage('customers', customers);
                return { name, email, phone };
            }
        }).then((result) => {
            if (result.isConfirmed) {
                showAlert('Cliente Agregado', `Cliente ${result.value.name} agregado exitosamente!`);
                updateTable('customers');
            }
        });
    });

    function updateTable(type) {
        const data = getLocalStorageData(type);
        let tableContent = '';

                data.forEach(item => {
                    tableContent += `<tr>${Object.values(item).map(value => `<td>${Array.isArray(value) ? value.join(', ') : value}</td>`).join('')}</tr>`;
                });

                const tableHeaders = {
                    packages: '<th>Nombre del Paquete</th><th>Destino</th><th>Tipo</th><th>Servicios</th><th>Precio</th><th>Hotel</th><th>Estadía</th>',
                    reservations: '<th>Cliente</th><th>Número de Usuarios</th><th>Paquete</th><th>Personas</th><th>Niños</th><th>Fecha de Salida</th><th>Fecha de Regreso</th>',
                    customers: '<th>Nombre</th><th>Email</th><th>Teléfono</th>',
                };

                $('#main-content').html(`
                    <table class="styled-table">
                        <thead><tr>${tableHeaders[type]}</tr></thead>
                        <tbody>${tableContent}</tbody>
                    </table>
                `);
            }

            // Mostrar inicialmente la tabla de paquetes
            updateTable('packages');
        });

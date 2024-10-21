const express = require('express');
const { Pool } = require('pg');
const cors = require('cors');
const app = express();

// Configuración de CORS
app.use(cors());

const PORT = 3000; // Puerto específico

// Configurar la conexión a la base de datos PostgreSQL
const pool = new Pool({
  user: 'admin',
  host: 'dpg-co5idpsf7o1s73a2h0hg-a',
  database: 'deploy_render_0qjh_tsli',
  password: 'Tpki9Wco0FC6F6nSEFDdJEEKc9e12A6S',
  port: 5432, // Puerto predeterminado de PostgreSQL
});

// Middleware para parsear JSON
app.use(express.json());

// Ruta para obtener los datos de personas desde la base de datos
app.get('/CRUDRepo/ConsultarPersonas', (req, res) => {
  // Realizar consulta SQL para obtener los datos de las personas
  pool.query('SELECT * FROM humano', (err, results) => {
    if (err) {
      console.error('Error al ejecutar la consulta:', err);
      res.status(500).json({ error: 'Error interno del servidor' });
      return;
    }
    // Enviar los resultados como respuesta en formato JSON
    res.json(results.rows);
  });
});

// Ruta para agregar una nueva persona
app.post('/CRUDRepo/AgregarPersona', (req, res) => {
  const { nombre, apellido, email, edad} = req.body;
  pool.query('INSERT INTO humano (nombre, apellido, email, edad) VALUES ($1, $2, $3, $4)', [nombre, apellido, email, edad], (err, results) => {
    if (err) {
      console.error('Error al agregar la persona:', err);
      res.status(500).json({ error: 'Error interno del servidor' });
      return;
    }
    res.status(201).json({ message: 'Persona agregada exitosamente' });
  });
});

// Ruta para actualizar los datos de una persona
app.put('/CRUDRepo/ActualizarPersona/:id', (req, res) => {
  const { id } = req.params;
  const { nombre, edad } = req.body;
  pool.query('UPDATE humano SET nombre = $1, edad = $2 WHERE id = $3', [nombre, edad, id], (err, results) => {
    if (err) {
      console.error('Error al actualizar la persona:', err);
      res.status(500).json({ error: 'Error interno del servidor' });
      return;
    }
    res.json({ message: 'Datos de la persona actualizados exitosamente' });
  });
});

// Ruta para eliminar una persona
app.delete('/CRUDRepo/EliminarPersona/:id', (req, res) => {
  const { id } = req.params;
  pool.query('DELETE FROM humano WHERE id = $1', [id], (err, results) => {
    if (err) {
      console.error('Error al eliminar la persona:', err);
      res.status(500).json({ error: 'Error interno del servidor' });
      return;
    }
    res.json({ message: 'Persona eliminada exitosamente' });
  });
});

// Manejo de errores para rutas no encontradas
app.use((req, res, next) => {
  res.status(404).json({ error: 'Ruta no encontrada' });
});

// Manejador de errores genérico
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Error interno del servidor' });
});

// Iniciar el servidor en el puerto específico
app.listen(PORT, () => {
  console.log(`Servidor escuchando en el puerto ${PORT}`);
});

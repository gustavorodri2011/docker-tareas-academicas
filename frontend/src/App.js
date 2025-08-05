import React, { useEffect, useState } from "react";

function App() {
  const [tareas, setTareas] = useState([]);
  const [texto, setTexto] = useState("");

  const cargar = () =>
    fetch("/api/tareas")
      .then((r) => r.json())
      .then(setTareas);

  const agregar = () =>
    fetch("/api/tareas", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ texto }),
    })
      .then(() => {
        setTexto("");
        cargar();
      });

  useEffect(() => cargar(), []);

  return (
    <div style={{ padding: 30 }}>
      <h1>Mis Tareas Académicas</h1>
      <input value={texto} onChange={(e) => setTexto(e.target.value)} />
      <button onClick={agregar}>Agregar</button>
      <ul>
        {tareas.map((t) => (
          <li key={t.id}>{t.texto}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;

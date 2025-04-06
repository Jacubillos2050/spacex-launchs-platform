import React, { useEffect, useState } from "react";
import { Container, Table, Spinner, Alert } from "react-bootstrap";
import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
} from "chart.js";

import 'bootstrap/dist/css/bootstrap.min.css';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

function App() {
  const [launches, setLaunches] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch("https://fqt3vp3zx3.execute-api.us-east-1.amazonaws.com/dev/launches") 
      .then((res) => {
        if (!res.ok) throw new Error("Error al obtener lanzamientos");
        return res.json();
      })
      .then(setLaunches)
      .catch(setError)
      .finally(() => setLoading(false));
  }, []);

  const chartData = {
    labels: launches.map((l) =>
      new Date(l.launch_date).toLocaleDateString()
    ),
    datasets: [
      {
        label: "Éxito del Lanzamiento",
        data: launches.map((l) => (l.status === "success" ? 1 : 0)),
        borderColor: "#198754",
        backgroundColor: "rgba(25,135,84,0.2)",
      },
    ],
  };

  return (
    <Container className="my-4">
      <h1 className="mb-4">🚀 SpaceX Launch Dashboard</h1>

      {loading && <Spinner animation="border" />}
      {error && <Alert variant="danger">{error.message}</Alert>}

      {!loading && !error && (
        <>
          <div className="mb-4">
            <Line data={chartData} />
          </div>

          <Table striped bordered hover responsive>
            <thead>
              <tr>
                <th>Misión</th>
                <th>Fecha</th>
                <th>Cohete</th>
                <th>Estado</th>
              </tr>
            </thead>
            <tbody>
              {launches.map((launch) => (
                <tr key={launch.id}>
                  <td>{launch.mission_name}</td>
                  <td>{new Date(launch.launch_date).toLocaleString()}</td>
                  <td>{launch.rocket_name}</td>
                  <td>{launch.status}</td>
                </tr>
              ))}
            </tbody>
          </Table>
        </>
      )}
    </Container>
  );
}

export default App;

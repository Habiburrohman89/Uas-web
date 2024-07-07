import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import './content.css';

function Content() {
  const [data, setData] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/tugas/')
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => setData(data))
      .catch(error => {
        console.error('Error fetching data:', error);
        setError(error.toString());
      });
  }, []);

  if (error) {
    return <div>Error: {error}</div>;
  }

  if (data.length === 0) {
    return <div>Loading...</div>;
  }

  return (
    <div className="container">
      <div className="row">
        {data.map(task => (
          <div className="col-lg-4" key={task.id}>
            <div className="card card-margin">
              <div className="card-header no-border">
                <h5 className="card-title">{task.judul}</h5>
              </div>
              <div className="card-body pt-0">
                <div className="widget-49">
                  <div className="widget-49-title-wrapper">
                    <div className="widget-49-date-primary">
                      <span className="widget-49-date-day">{new Date(task.tanggal_dibuat).getDate()}</span>
                      <span className="widget-49-date-month">{new Date(task.tanggal_dibuat).toLocaleString('default', { month: 'short' })}</span>
                    </div>
                    <div className="widget-49-meeting-info">
                      <span className="widget-49-pro-title">{task.deskripsi}</span>
                      <span className="widget-49-meeting-time">{`Batas waktu: ${task.batas_waktu}`}</span>
                    </div>
                  </div>
                  <div className="widget-49-meeting-action">
                    <Link to={`/task/${task.id}`} className="btn btn-sm btn-flash-border-primary">View All</Link>
                  </div>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Content;

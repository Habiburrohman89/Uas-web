import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import './content.css';

function TaskDetail() {
  const { id } = useParams();
  const [task, setTask] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/tugas/${id}/`)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => setTask(data))
      .catch(error => {
        console.error('Error fetching data:', error);
        setError(error.toString());
      });
  }, [id]);

  if (error) {
    return <div>Error: {error}</div>;
  }

  if (!task) {
    return <div>Loading...</div>;
  }

  return (
    <div className="container">
      <div className="row">
        <div className="col-lg-12">
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
                <ol className="widget-49-meeting-points">
                  <li className="widget-49-meeting-item"><span>Pembuat: {task.pembuat}</span></li>
                  <li className="widget-49-meeting-item"><span>Assigned to: {task.assigned_to}</span></li>
                </ol>
                <div className="widget-49-meeting-action">
                  <a href="/" className="btn btn-sm btn-flash-border-primary">Back to List</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default TaskDetail;

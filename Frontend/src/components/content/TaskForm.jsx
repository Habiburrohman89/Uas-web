import React, { useState } from 'react';

function FormTugas({ onSubmit }) {
    const [judul, setJudul] = useState('');
    const [deskripsi, setDeskripsi] = useState('');
    const [assignedTo, setAssignedTo] = useState('');
    const [batasWaktu, setBatasWaktu] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        const data = {
            judul: judul,
            deskripsi: deskripsi,
            assigned_to: parseInt(assignedTo), // pastikan ini sesuai dengan serializer Django
            batas_waktu: batasWaktu
        };
        onSubmit(data);
    };

    return (
        <div className='container'>
            <div className='card'>
                <div className='card-body'>
                    <form onSubmit={handleSubmit}>
                        <div className="mb-3">
                            <label htmlFor="judul" className="form-label">Judul</label>
                            <input type="text" className="form-control" id="judul" value={judul} onChange={(e) => setJudul(e.target.value)} required />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="deskripsi" className="form-label">Deskripsi</label>
                            <textarea className="form-control" id="deskripsi" rows="3" value={deskripsi} onChange={(e) => setDeskripsi(e.target.value)} required></textarea>
                        </div>
                        <div className="mb-3">
                            <label htmlFor="assignedTo" className="form-label">Assigned To</label>
                            <input type="number" className="form-control" id="assignedTo" value={assignedTo} onChange={(e) => setAssignedTo(e.target.value)} required />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="batasWaktu" className="form-label">Batas Waktu</label>
                            <input type="datetime-local" className="form-control" id="batasWaktu" value={batasWaktu} onChange={(e) => setBatasWaktu(e.target.value)} required />
                        </div>
                        <button type="submit" className="btn btn-primary">Submit</button>
                    </form>
                </div>
            </div>
        </div>
    );
}

export default FormTugas;

import React, { useState } from 'react';
// import './App.css';

export default function Test() { 
  const [data, setData] = useState([1,2,3,4,5]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
let token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ"
let user = "James.Beagle"
    const fetchData = async (e) => {

      // Prevent default form submission behavior
      e.preventDefault();
      
     
        
        const response = await fetch('http://127.0.0.1:5000/heartbeat', {
        method: 'POST',
        body: JSON.stringify({CDSID: user}),
        headers: {
            "Authorization": `Bearer ${token}`,
            'Content-Type': 'application/json',}        })
        
        
        const data = await response.json();
        console.log("data",data)
        // const response = await fetch('http://127.0.0.1:5000/heartbeat', { method: 'GET' });
               
        // const result = await response.json();
        // setData(result);
        // setLoading(false);
     
    };


  return (
    <div >
      <header className="App-header">
       <button onClick={fetchData}>Click me</button>
       {data}
      </header>
    </div>
  );
}
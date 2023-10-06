import logo from './logo.svg';
import './App.css';
import Table from './components/Table'
import axios from 'axios'
import React, { useState, useEffect } from 'react';

const App = () => {

  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  // const response = axios.get('http://127.0.0.1:5000/allTrains').then((result) => {
  //   console.log("Response: ", result.data);
  //   setData(response.data);
  //       console.log("Response: ", data);
  //       setLoading(false);
  // }).catch((error) => {
  //   // Handle errors here
  //   console.error('Error fetching data:', error);
  //   setLoading(false);
  // });

  

  useEffect(() => {
    // Define the API URL you want to fetch data from
    const response = axios.get('http://127.0.0.1:5000/allTrains').then((result) => {
      setData(result.data);
        // console.log("Response: ", result.data);
        setLoading(false);
    })
      .catch((error) => {
        // Handle errors here
        console.error('Error fetching data:', error);
        setLoading(false);
      });
  }, []); 

  return (
    <>
    {loading ? (
        <p>Loading...</p>
      ) : (
        <>
        {/* {console.log("Data: ", data)} */}
        <Table data={data} />
        </>
      )}
    </>
  );
}

export default App;
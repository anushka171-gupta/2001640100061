import React from 'react';

const Table = (props) => {

  console.log(" Props: ", props);
  console.log(typeof(props.data));
  const data = Object.entries(props.data);

  console.log("\n\n Data: ", data[0][1], "\n\n");

  return (
    <div className="table-responsive">
      <table className="table table-striped table-bordered">
        <thead>
          <tr>
            <th>Train Name</th>
            <th>Train Number</th>
            <th>Seats Available - AC</th>
            <th>Seats Available - Sleeper</th>
            <th>Price - AC</th>
            <th>Price - Sleeper</th>
            <th>Departure Time</th>
            <th>Delayed By</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item, index) => (
            <>
            <tr key = {item["1"].trainNumber}>
            <td>{item["1"].trainName}</td>
            <td>{item["1"].trainNumber}</td>
            <td>{item["1"].seatsAvailable.AC}</td>
            <td>{item["1"].seatsAvailable.sleeper}</td>
            <td>{item["1"].price.AC}</td>
            <td>{item["1"].price.sleeper}</td>
            <td>{item["1"].departureTime.Hours + ":" + item["1"].departureTime.Minutes +":" +item["1"].departureTime.Seconds}</td>
            <td>{item["1"].delayedBy}</td>
            </tr>
            </>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Table;
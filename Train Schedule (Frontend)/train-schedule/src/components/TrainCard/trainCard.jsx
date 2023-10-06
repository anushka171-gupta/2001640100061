import React from 'react';
// import {useState} from 'react';
// import TripItem from './TripItem';
// import axios from 'axios';

import React from 'react';

const trainCard = (props) => {
  return (
    <div className="card">
      {/* <img src={props.imageUrl} className="card-img-top" alt={props.title} /> */}
      <div className="card-body">
        <h5 className="card-title">{props.trainName}</h5>
        <p className="card-text">{props.trainNumber}</p>
        <p className="card-text">{props.departureTime}</p>
        <p className="card-text">{props.price}</p>
        <p className="card-text">{props.seatsAvailable}</p>
        {/* <p className="card-text">{props.trainNumber}</p> */}
      </div>
    </div>
  );
};

export default trainCard;
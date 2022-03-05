async function flightsInfo() {
    const airportsResponse = await fetch('https://think.cs.vt.edu/corgis/datasets/json/airlines/airlines.json');
    const airportsData = await airportsResponse.json();
  
    airportsData.map((airport) => {
      const output = airport.Statistics.Flights;
      const sum =
        airport.Statistics.Flights.Cancelled +
        airport.Statistics.Flights.Delayed +
        airport.Statistics.Flights.Diverted +
        airport.Statistics.Flights["On Time"];
  
      output["isSumEqualToTotal"] = false;
      if (sum === airport.Statistics.Flights.Total)
        output["isSumEqualToTotal"] = true;
  
      console.log(output);
    });
  }
  
  flightsInfo();
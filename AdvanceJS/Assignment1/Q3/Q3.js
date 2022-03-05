async function nobelPrize() {
    const response = await fetch("http://api.nobelprize.org/v1/prize.json");
    const myData = await response.json();
  
    const data = myData.prizes.filter((prize) => {
      return prize.year >= 2000 && prize.year <= 2019 && prize.category == "chemistry"
    });
    return data;
  }
  
  nobelPrize().then(
      function(value) {console.log(value)}
  );
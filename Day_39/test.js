let url = 'https://api.sheety.co/c89a9d5d328a3154f47d77e619fd9674/flightDeals/prices';
fetch(url)
.then((response) => response.json())
.then(json => {
  console.log(json.prices);
});
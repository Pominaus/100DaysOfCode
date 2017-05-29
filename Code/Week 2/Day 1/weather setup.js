$(function(){
  console.log("setup sript loaded");
  var darkSkyOverride = "https://cors-anywhere.herokuapp.com/"
  var weatherStr =
    "https://api.darksky.net/forecast/15b0160607d46384859d0fafec93b26c/";
  var weatherExclude = "?exclude=minutely,hourly,daily,alerts";
  var location = [27.9878, 86.9250];
  var weather = {};
  
  
  //call API
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(pos) {
      location = [pos.coords.latitude, pos.coords.longitude];
      weatherStr += location[0] + "," + location[1] + weatherExclude;
      //console.log(weatherStr);
      $.getJSON(darkSkyOverride + weatherStr, function(apiData) {
        weather.fahrenheit = apiData.currently.temperature;
        weather.celcius = (weather.fahrenheit -32) * (5/9);
        weather.summary = apiData.currently.icon;
        weather.windMph = apiData.currently.windSpeed;
        weather.windKph = weather.windMph * 1.60934;
        weather.windDir = apiData.currently.windBearing;
        weather.feelsLikeF = apiData.currently.apparentTemperature;
        weather.feelsLikeC = (weather.feelsLikeF -32) *5/9;
        weather.humidity = apiData.currently.humidity;
        weather.rainProb = apiData.currently.precipProbability;
        console.log(weather);
        
      });
    });
  }
});

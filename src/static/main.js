// Function to get parameters by name from config file
function getParameterByName(name, defaults, location) {
  location = location || window.location.href;
  name = name.replace(/[\[]/,'\\\[').replace(/[\]]/,'\\\]');
  var result = new RegExp('[\\?&]' + name + '=([^&#]*)').exec(location);
  return result === null ? defaults : decodeURIComponent(result[1].replace(/\+/g, ' '));
}

// Get the config file "env.json" and extract the values
function getConfig() {
  // if you pass ?dev=true to your url address default config that will be used is `config-development`
  // otherwise - `config-production`
  var configName = getParameterByName('dev', false) ? 'env' : 'env';

  window._config || (window._config = {});

  // for production version you should concat your config with main script or put it above main script
  // inside global `_config` variable for example
  if (window._config[configName]) return window._config[configName];

  // for development version you can just make an ajax call to get the config
  $.ajax({
    url : '/static/' + configName + '.json',
    async : false,
    success : function(response) {
      window._config[configName] = response;
    }
  });
  return window._config[configName];
}

// Get configuration
var conf = getConfig();

// Send request when spacebar
function onKeyDown(e) {
    if (e.keyCode === 32) {
        sendRequest()
    }
    if (e.keyCode === 9) {
        e.preventDefault();
        sendRequest()
    }

    if (e.keyCode === 229) {
        sendRequest()
    }
}

// Colorize boxes
function displayPrediction(textGenerated) {
    // TODO
}

// Function to autogenerate
function autoGenerate(){
    // TODO
}

console.log(conf.APP_URL + conf.ROUTE)
// Function to send request to model
function sendRequest(input) {
    // Check if argument input passed
    if (input !== undefined) {
        // pass
    } else {
        // In case input no passed, we get the text from textarea
        // TODO
    }

    if (input.length>1)
    {
        // TODO
    }
}

document.getElementById("textarea").addEventListener("keydown", onKeyDown);

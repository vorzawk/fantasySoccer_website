function processForm(e) {

  if (e.preventDefault) e.preventDefault();

  /* read the element returned from the database */
  var numPlayers = document.getElementById('dataFromDB').rows.length;
  for (i=1; i<numPlayers; i++) {
    var player = document.getElementById('dataFromDB').rows[i].cells;
    var playerName = player[0].innerHTML;
    var playerPosition = player[2].innerHTML;

    if (playerPosition == "Forward") {
      var forwards = document.getElementById('forwards');
      var row = forwards.insertRow();
    }
    if (playerPosition == "Midfielder") {
      var forwards = document.getElementById('midfielders');
      var row = forwards.insertRow();
    }
    if (playerPosition == "Defender") {
      var forwards = document.getElementById('defenders');
      var row = forwards.insertRow();
    }
    if (playerPosition == "Goal Keeper") {
      var forwards = document.getElementById('goalkeeper');
      var row = forwards.insertRow();
    }
    var cell = row.insertCell();
    cell.innerHTML = playerName;
  }
  // You must return false to prevent the default form behavior
  return false;
}

function dontProcessForm(e) {
  if (e.preventDefault) e.preventDefault();
  return false;
}

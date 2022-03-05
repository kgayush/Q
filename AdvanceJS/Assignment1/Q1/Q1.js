const myRequest = new XMLHttpRequest();
myRequest.open('GET', 'battles.json');
myRequest.onload = () => {

    const mostActive = {};
    const attackerKing = [];
    const defenderKing = [];
    const region = [];
    const name = [];

    const attackerOutcome = { win: 0, loss: 0 };

    const battleType = [];

    const defenderSize = {};

    const size = [];
    const output = {};

    const battles = JSON.parse(myRequest.responseText);
    battles.map((battle) => {
        attackerKing.push(battle.attacker_king);
        defenderKing.push(battle.defender_king);
        region.push(battle.region);
        name.push(battle.name);
        if (!battleType.includes(battle.battle_type) && battle.battle_type != "") {
          battleType.push(battle.battle_type);
        }
      
        if (battle.attacker_outcome == "win") {
          attackerOutcome.win = attackerOutcome.win + 1;
        } else {
          attackerOutcome.loss = attackerOutcome.loss + 1;
        }
      
        if (battle.defender_size != null) {
          size.push(battle.defender_size);
        }
      });
      
      mostActive.attacker_king = findMostActive(attackerKing);
      mostActive.defender_king = findMostActive(defenderKing);
      mostActive.region = findMostActive(region);
      mostActive.name = findMostActive(name);
      const sum = size.reduce((partialSum, a) => partialSum + a, 0);
      defenderSize.average = Math.round(sum / size.length);
      defenderSize.min = Math.min.apply(Math, size);
      defenderSize.max = Math.max.apply(Math, size);
      output.most_active = mostActive;
      output.attacker_outcome = attackerOutcome;
      output.battle_type = battleType;
      output.defender_size = defenderSize;

      console.log(output);
};
myRequest.send();

function findMostActive(array) {
  if (array.length == 0)
    return null;
  var _map = {};
  var mostActive = array[0];
  var maxCount = 1;
  for (var i = 0; i < array.length; i++) {
    var item = array[i];
    if (_map[item] == null) 
      _map[item] = 1;
    else 
      _map[item]++;
    if (_map[item] > maxCount) {
      mostActive = item;
      maxCount = _map[item];
    }
  }
  return mostActive;
}



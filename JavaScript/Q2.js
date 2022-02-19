teams = { aaiec: 400,
   aaiwc: 60,
   qai: 200, 
   poc: 100, 
   gtm: 50, 
   hr: 10 
  };

var sortArr = [];
let team;

for (team in teams) {
  sortArr.push([team, teams[team]]);
}

sortArr.sort(function (a, b) {
  return b[1] - a[1];
});

let i;
for (i = 0; i < sortArr.length; i++) {
  console.log(sortArr[i][0]);
}

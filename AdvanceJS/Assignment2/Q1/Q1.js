fetch("https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json")
    .then(function (response) {
      return response.json();
    })
    .then(function (myData) {
      actors = [];
      genres = [];
      temp = {};
      output = {};
      for (let i = 0; i < myData.length; i++) {
        for (let j = 0; j < myData[i].cast.length; j++) {
          temp["Actor"] = myData[i].cast[j];
          temp["Movies"] = myData[i].title;
          actors.push(Object.assign({}, temp));
        }
        for (let j = 0; j < myData[i].genres.length; j++) {
          temp["Type"] = myData[i].genres[j];
          temp["Movies"] = myData[i].title;
          genres.push(Object.assign({}, temp));
        }
      }
  
      var actorsOutput = actors.reduce(function (old, _new) {
        var occurs = old.reduce(function (n, item, i) {
          return item.Actor === _new.Actor ? i : n;
        }, -1);
        if (occurs >= 0) {
          old[occurs].Movies = old[occurs].Movies.concat(_new.Movies);
        } else {
          var obj = {
            Actor: _new.Actor,
            Movies: [_new.Movies],
          };
          old = old.concat([obj]);
        }
  
        return old;
      }, []);
  
      var genersOutput = genres.reduce(function (old, _new) {
        var occurs = old.reduce(function (n, item, i) {
          return item.Type === _new.Type ? i : n;
        }, -1);
        if (occurs >= 0) {
          old[occurs].Movies = old[occurs].Movies.concat(_new.Movies);
        } else {
          var obj = {
            Type: _new.Type,
            Movies: [_new.Movies],
          };
          old = old.concat([obj]);
        }
        return old;
      }, []);
  
      output["Actors"] = actorsOutput;
      output["Genres"] = genersOutput;
      console.log(output);
    })
    .catch(function (error) {
      console.log(error);
    });
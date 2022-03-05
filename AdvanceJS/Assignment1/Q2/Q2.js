async function getInfo(name) {
    const apiResponse = await fetch(`https://api.github.com/search/repositories?q=${name}`);  
    const myData = await apiResponse.json();  
    myData.items.map((value) => output(value));
  }
  
  async function output(repo) {
    const ownerResponse = await fetch(repo.owner.url);
    const ownersData = await ownerResponse.json();
  
    const branchResponse = await fetch(repo.branches_url.split("{")[0]);
    const branchData = await branchResponse.json();
  
    const output = {
      name: repo.name,
      full_name: repo.full_name,
      private: repo.private,
      owner: {
        login: ownersData.login,
        name: ownersData.name,
        followersCount: ownersData.followers,
        followingCount: ownersData.following,
      },
      licenseName: repo.license,
      score: repo.score,
      numberOfBranch: branchData.length,
    };
  
    console.log(output);
  }

getInfo("kgayush");
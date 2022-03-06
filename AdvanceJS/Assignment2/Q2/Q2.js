class QueenAttack {
    constructor(queen1Row, queen1Column, queen2Row, queen2Column) {
      this.queen1Row = queen1Row;
      this.queen1Column = queen1Column;
      this.queen2Row = queen2Row;
      this.queen2Column = queen2Column;
    }
  
    canAttack() {
      if (this.queen1Row == this.queen2Row)
        return true;
      if (this.queen1Column == this.queen2Column)
        return true;
      if (Math.abs(this.queen1Row - this.queen2Row) == Math.abs(this.queen1Column - this.queen2Column))
        return true;
  
      return false;
    }
  }
  let queen1Row = Math.floor(Math.random() * 8);
  let queen1Column = Math.floor(Math.random() * 8);
  let queen2Row = Math.floor(Math.random() * 8);
  let queen2Column = Math.floor(Math.random() * 8);

  console.log(`Queen 1 position: (${queen1Row}, ${queen1Column})`);
  console.log(`Queen 2 position: (${queen2Row}, ${queen2Column})`);

  let queens = new QueenAttack(queen1Row, queen1Column, queen2Row, queen2Column);
  
  if (queens.canAttack()) {
    console.log("Queens can attack each other");
  } else {
    console.log("Queens can not attack each other");
  }
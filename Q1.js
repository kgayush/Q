var str = `Thank you so much for contacting us. Dreamland guest relations. 
You're speaking with Ronaldo. May I have your name, please? Yes, sure. My name is robin soleimani. 
What is your phone number? It is 9876535362 as mentioned in the book Diary. 
Thank you so much for providing the info!`;

const sentenceArr = str.match(/(.*?(?:\.|\?|!))(?: |$)/g);

const ansArr = sentenceArr
  .map((sentence) => {
    sentence = sentence.replace(/(^\s*)|(\s*$)/gi, "");
    sentence = sentence.replace(/[ ]{2,}/gi, " ");
    sentence = sentence.replace(/\n /, "\n");
    size = sentence.split(" ").length;
    if (size > 3) {
      return sentence;
    }
  })
  .filter((elements) => elements != undefined);

const regex = /[0-9]/g;

const hideArr = ansArr.map((item) => {
  return item.replace(regex, "X");
});

let i;
for (i = 0; i < hideArr.length; i++) {
  const str1 = `${i + 1}. ${hideArr[i]}`;
  console.log(str1);
}

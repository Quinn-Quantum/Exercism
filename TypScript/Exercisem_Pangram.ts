export function isPangram(sentence:string) {
    let listSentenc = sentence.toUpperCase().split("")
    for (let beta = 65; beta < 91; beta++) {
      let gamma = String.fromCharCode(beta);
      if (listSentenc.includes(gamma)) {
        continue;
      } else {
        return false;
      }
    }
    return true;
    
  }
  
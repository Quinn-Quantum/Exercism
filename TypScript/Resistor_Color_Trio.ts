export function decodedResistorValue(listColors:string) {
    const COLORS = ['black','brown','red','orange','yellow','green','blue','violet','grey','white'];
    var num1:string = (listColors[0] != 'black') ? ''+COLORS.indexOf(listColors[0]) : ''
    var num2:string = (listColors[1] != 'black') ? ''+COLORS.indexOf(listColors[1]) : ''
    var stringOhm:string = `${num1}${num2}`
    if(stringOhm == ''){
      stringOhm = '0'
    }
  switch(listColors[2]) {
    case 'black':
      stringOhm = stringOhm + " ohms";
      break;
    case'brown':
      stringOhm = stringOhm + "0 ohms";
      break;
    case 'red':
      stringOhm = stringOhm + " kiloohms";
      break;
    case 'orange':
      stringOhm = stringOhm + " kiloohms";
      break;
    case 'yellow':
      stringOhm = stringOhm + "0 kiloohms";
      break;
    case 'green':
      stringOhm = stringOhm + "00 kiloohms";
      break;
    case 'blue':
      stringOhm = stringOhm + " megaohms";
      break;
    case 'violet':
      stringOhm = stringOhm + "0 megaohms"
      break;
    case 'grey':
      stringOhm = stringOhm + "00 megaohms"
      break;
    default:
      stringOhm = stringOhm + " gigaohms"
   }
   return stringOhm
  }
  
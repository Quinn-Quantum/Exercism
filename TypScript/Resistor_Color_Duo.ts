export function decodedValue(listColors:string) {
    var colors = ['black', 'brown', 'red', 'orange', 'yellow' ,'green' ,'blue' ,'violet' ,'grey' ,'white']
   return +((''+colors.indexOf(listColors[0])) + (''+colors.indexOf(listColors[1])))
  }
  
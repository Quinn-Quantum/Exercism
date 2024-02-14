export function age(planet: string, seconds: number): unknown {
    let earthYears = seconds / 31557600
     switch (planet) {
          case ('mercury'): 
           return parseFloat((earthYears/0.2408467).toFixed(2))
             break;
          case ('venus'): 
         return parseFloat((earthYears/ 0.61519726 ).toFixed(2))
             break;
          case ('mars'): 
         return parseFloat((earthYears/ 1.8808158 ).toFixed(2))
             break;
          case ('jupiter'): 
         return parseFloat((earthYears/11.862615).toFixed(2))
              break;
         case ('saturn'): 
         return parseFloat((earthYears/29.447498).toFixed(2))
             break;
         case ('uranus'):
         return parseFloat((earthYears/ 84.016846).toFixed(2))
             break;
         case ('neptune'): 
         return parseFloat((earthYears/164.79132 ).toFixed(2))
             break;
  
          default:
          return parseFloat(earthYears.toFixed(2))
           break;
     }
    
  }
  
export function hey(message: string): string {
    if(message.trim() === ""){
      return "Fine. Be that way!"
    }
     if(!/[a-z]/.test(message) && /[A-Z]/.test(message) && message.endsWith('?')){
        return "Calm down, I know what I'm doing!"
      }
     if (message.trim().endsWith('?')){
      return "Sure." 
    }
   
    if(!/[a-z]/.test(message) && /[A-Z]/.test(message)){
      return "Whoa, chill out!"
    } 
    else{
      return "Whatever." 
    }
  }
  
class Transcriptor {
    static readonly transcription: Map<string, string> = new Map(
           [
               ['A', 'U'],
               ['T', 'A'],
               ['C', 'G'],
               ['G', 'C']
           ]
       )
   
     static toRna(letters:string) {
           let newLetters: string = ""
           for (const letter of letters) {
               const rna = Transcriptor.transcription.get(letter)
               if (rna === undefined) {
                   return 'Invalid input DNA.'
               }
               newLetters += rna
           }
           return newLetters 
   }
   }
   export default Transcriptor
   
   export function toRna(letters:string) {
     
     let rna = Transcriptor.toRna(letters)
     if (rna === 'Invalid input DNA.'){
       throw rna
     }
     return rna
     
      
   }
   
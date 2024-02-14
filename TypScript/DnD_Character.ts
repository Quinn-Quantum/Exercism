const modifier = {
    3:-4,
    4:-3,
    5:-3,
    6:-2,
    7:-2,
    8:-1,
    9:-1,
    10:0,
    11:0,
    12:1,
    13:1,
    14:2,
    15:2,
    16:3,
    17:3,
    18:4
    
  }
export type Modifier = keyof typeof modifier;
export class DnDCharacter {
  strength:number
  dexterity:number
  constitution:any
  intelligence:number
  wisdom:number
  charisma:number
  hitpoints:number
  
   public constructor() {
   this.strength = DnDCharacter.generateAbilityScore();
  this.dexterity = DnDCharacter.generateAbilityScore();
  this.constitution = DnDCharacter.generateAbilityScore();
  this.intelligence = DnDCharacter.generateAbilityScore();
  this.wisdom = DnDCharacter.generateAbilityScore();
  this.charisma = DnDCharacter.generateAbilityScore();
    this.hitpoints = DnDCharacter.getModifierFor(this.constitution  ) + 10
   }
  
public static generateAbilityScore(): number {
    return Math.floor((Math.random() * 16)+3)
  }

  public static getModifierFor(abilityValue: Modifier): number {
    return modifier[abilityValue]
  }

 
}

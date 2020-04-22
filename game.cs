using System;

namespace Spaceman
{
class Game{
  public void Greet(){
    Console.WriteLine("Greetings, terrestrial being. \n Instructions: save your friend from alien abduction by guessing the letters in the codeword.");
  }
  string codeword;
  string currentWord;
  int maxGuess = 5;
  int wrongGuess = 0;
  private string[] codewords = new string[] {"words", "worlds", "wors", "wars", "lords"};
  
  
  
  public Game (){
    Random rand = new Random();
    codeword = codewords[rand.Next(codewords.Length)];
  for (int i = 0; i < codewords.Length; i++){
    currentWord += "_";
  }
  }
  
  public bool DidWin(){
   if( codeword.Equals(currentWord)) {
     return true;
   }else{
     return false;
   }
  }
  
  public bool DidLose(){
    if (wrongGuess > maxGuess){
      return true;
    }else{
      return false;
    }
  }
  public void Display(){
    ufo spaceship = new Ufo();
    Console.WriteLine(spaceship.Stringify());
    Console.WriteLine(currentWord);
    Console.WriteLine(maxGuess - wrongGuess);
  }
}
}

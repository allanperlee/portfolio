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
  str[] codewords = {"words", "worlds", "wors", "wars", "lords"};
  
  Ufo Game = new Ufo();
  }
  
  Random rand = new Random();
  int cIndex = rand.Next(codewords.Length);
  for (int i = 0; i < codeword.Length; i++){
    currentWord[i] = "_";
  }
  public bool DidWin(){
    codeword.Equals(currentWord);
  }
}
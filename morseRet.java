class morseRet{
  public static void main(String[] args) {
    String str = args[0];
    String morse = "";
    MorseCode mc = new MorseCode();

    for(int i = 0; i < str.length(); i++){
      char c;
      char d;
      String s;
      String tmp;
      String temp = "";

      c = str.charAt(i);
      tmp = mc.convertMorse(c);
      for(int j = 0; j <tmp.length(); j++) {
        d = tmp.charAt(j);

        if (d == '・') {
          s = ".";
        }
        else {
          s = "-";
        }
         temp += s;
      }
      morse += temp;
    }

    System.out.println(morse);
  }
}

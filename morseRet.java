import java.util.ArrayList;
class morseRet{
  public static void main(String[] args) {

    MorseCode mc = new MorseCode();

    String str = args[0];
    String sCut;
    String tmp;
    String s = "";
    char tmpChar;
    ArrayList<Character> morseList = new ArrayList<Character>();

    char[] cut = str.toCharArray();
    for(char c : cut) {
      morseList.add(' ');
      morseList.add(c);
    }
    morseList.remove(0);
    for(char c: morseList) {
      tmp = mc.convertMorse(c);
      for(int i = 0; i < tmp.length(); i++) {
        tmpChar = tmp.charAt(i);
        if(tmpChar == ' '||tmpChar == '　') s = "~";//文字と文字の間
        if(tmpChar == '・') s = ".";//とん
        if(tmpChar == '－') s = "-";//つー
        if(tmpChar == '_') s = "_";//単語の区切り
        else System.out.print("");
        System.out.println(s);
      }
    }
  }
}

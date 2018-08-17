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
    // System.out.println(cut);
    for(char c : cut) {
      morseList.add(c);
      morseList.add(' ');
    }
    morseList.remove((morseList.size())-1);
    // System.out.println(morseList);
    for(char c: morseList) {
      tmp = mc.convertMorse(c);
      for(int i = 0; i < tmp.length(); i++) {
        tmpChar = tmp.charAt(i);
        // System.out.println(tmpChar);
        if(tmpChar == ' '||tmpChar == '　') s = "~";//文字と文字の間
        if(tmpChar == '・') s = ".";//とん
        if(tmpChar == '－') s = "-";//つー
        if(tmpChar == '_') s = "_";//単語の区切り
        System.out.println(s);
        //なんじ_うんぬん_かんぬん_を_しる_だろ_う_、_くるっ_ぱ
      }
    }
  }
}

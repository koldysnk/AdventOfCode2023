import java.util.*;

public class Node implements Comparable<Node>{

   public char spot;
   public int x = 0;
   public int y = 0;
   public int distance = 0;
   public String key = "";
   public int numKey = 0;
   public ArrayList<Node> links = new ArrayList<Node>();

   public Node(String key, char spot, int x, int y){
      this.key = key;
      this.numKey = x*1000 + y;
      this.spot = spot;
      this.x = x;
      this.y = y;
   }
   
   public void setDistance(int gX, int gY){
      this.distance = Math.abs(this.x-gX) + Math.abs(this.y-gY);
   }
   
   public void addLink(Node other){
      links.add(other);
      links.sort((n1, n2) -> n1.compareTo(n2));
   }
   
   @Override
   public String toString(){
      return String.valueOf(this.spot) + key;
   }
   
   @Override
   public int compareTo(Node other) {
      return Integer.compare(this.distance, other.distance);
   }

}
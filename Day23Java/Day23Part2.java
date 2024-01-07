import java.io.*;
import java.util.*;

class Day23Part2{

   public static final String INPUT_FILE = "day23input.txt";
   public static Map<String,Node> grid = new HashMap<>();
   public static int maxDist = 0;
   


   public static void main(String[] args) throws Exception{
   
      Node start = buildGrid();
      boolean[] visited = new boolean[150000];
      visited[start.numKey] = true;
      int dist = 0;
      int depth = 0;
      
      exploreGrid(start, visited, dist);   
      System.out.println(maxDist);
   }
   
   public static void exploreGrid(Node current, boolean[] visited, int dist){
      Explorer start = new Explorer(current, visited, dist);
      ArrayList<Explorer> queue = new ArrayList<>();
      
      queue.add(start);
      
      while (queue.size() > 0){
         Explorer explorer = queue.remove(queue.size()-1);
         //System.out.println(explorer.current);
         
         if(explorer.current.distance == 0){
            maxDist = Math.max(explorer.dist,maxDist);
            System.out.println("Path found: "+explorer.dist+" -> "+maxDist);   
         }else{
            //Oportunity to make this faster by sorting the queue   
            for (Node node : explorer.current.links){
               if (explorer.visited[node.numKey]!=true){
                  //System.out.println(node.numKey);
                  queue.add(new Explorer(node,explorer.visited,explorer.dist+1));
               }
            }
         }
      }
   }
   
   public static void exploreGridRecursive(Node current, Set<Node> visited, int dist){
      //displayPos(current,dist);
      if (current.distance == 0){
         maxDist = Math.max(dist,maxDist);
         System.out.println("Path found: "+dist+" -> "+maxDist);
      }else{
         for (Node node : current.links){
            if (!visited.contains(node)){
               visited.add(node);
               exploreGridRecursive(node,visited,dist+1);
               visited.remove(node);
            }
         }
      }
      
   }
   
   public static void displayPos(Node current, int depth){
      for (int i = 0;i<depth;i++){
         System.out.print(" ");
      }
      System.out.println(current);
   }
   
   public static Node buildGrid() throws Exception{
      BufferedReader br = new BufferedReader(new FileReader(new File("day23input.txt")));
      
      String row;
      int x = 0;
      Node start = null;
      
      while ((row = br.readLine()) != null){
         row = row.replace("\n","");
         
         for (int y = 0; y < row.length(); y++){
            String key = getKey(x, y);

            Node current = new Node(key,row.charAt(y),x,y);
            
            if (row.charAt(y) != '#'){
               linkNodes(current, x-1,y);
               linkNodes(current, x,y-1);
               
               if (x == 0){
                  start = current;
               }
            }

            grid.put(key,current);
         }
         x++;
      }
      
      setGoal(x-1);
      
      return start;
   }
   
   public static void setGoal(int x){
      int y = 0;
      Node current = grid.get(getKey(x, y));
      
      while (current.spot != '.'){
         y++;
         current = grid.get(getKey(x, y));
      }
      
      for(Node node : grid.values()){
         node.setDistance(x,y);
      }
      
   }
   
   public static String getKey(int x, int y){
      return Integer.toString(x) + "-" + Integer.toString(y);
   }
   
   public static void linkNodes(Node current, int x, int y){
      if (x>=0 && y>=0){
         Node other = grid.get(Integer.toString(x) + "-" + Integer.toString(y));
         if (other.spot != '#'){
            current.addLink(other);
            other.addLink(current);
         }
      }
      
   }

}
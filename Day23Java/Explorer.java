import java.util.*;

public class Explorer{

   public Node current;
   public boolean[] visited;
   public int dist;

   public Explorer(Node current, boolean[] visited, int dist){
      this.current = current;
      this.visited = visited.clone();
      this.visited[this.current.numKey] = true;
      this.dist = dist;   
   }

}
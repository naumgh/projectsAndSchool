import java.util.*;

//
// An implementation of a binary search tree.
//
// This tree stores both keys and values associated with those keys.
//
// More information about binary search trees can be found here:
//
// http://en.wikipedia.org/wiki/Binary_search_tree
//
// Note: Wikipedia is using a different definition of
//       depth and height than we are using.  Be sure
//       to read the comments in this file for the
//	 	 height function.
//
public class BinarySearchTree <K extends Comparable<K>, V>  {

	public static final int BST_PREORDER  = 1;
	public static final int BST_POSTORDER = 2;
	public static final int BST_INORDER   = 3;

	// These are package friendly for the TreeView class
	BSTNode<K,V>	root;
	int		count;


	public BinarySearchTree () {
		root = null;
		count = 0;
	}


	//
	// Purpose:
	//
	// Insert a new Key:Value Entry into the tree.  If the Key
	// already exists in the tree, update the value stored at
	// that node with the new value.
	//
	// Pre-Conditions:
	// 	the tree is a valid binary search tree
	//
	
	public void insert(K key, V value) {
		 inhelp(root, key, value);
		return;

	}


	public void inhelp(BSTNode traverse, K key, V value){	
		if(root == null){
			root = new BSTNode(key, value);
			traverse = root;
			count += 1;
		}
		
		
		int comp = traverse.key.compareTo(key);
		//System.out.println(comp);
		
		
		if(comp > 0){

			if(traverse.left == null){
				 traverse.left = new BSTNode(key,value);
				 count += 1;
			}else{
				inhelp(traverse.left, key, value);
				
			}
			 
			
		}else if(comp < 0){

			if(traverse.right == null){
				traverse.right = new BSTNode(key,value);
				count += 1;
			}else{
				 inhelp(traverse.right, key ,value);
				
			}
		
		}else{
			if(comp == 0){
				traverse.value = value;
			}
		}

		}

		//return new_node;
	
		


	//
	// Purpose:
	//
	// Return the value stored at key.  Throw a KeyNotFoundException
	// if the key isn't in the tree.
	//
	// Pre-conditions:
	//	the tree is a valid binary search tree
	//
	// Returns:
	//	the value stored at key
	//
	// Throws:
	//	KeyNotFoundException if key isn't in the tree
	//
	public V find(K key) throws KeyNotFoundException{
		try{
			return findhelp(root, key);
		}catch(KeyNotFoundException e){
			throw new KeyNotFoundException();
		}
		
	}

	public V findhelp(BSTNode traverse, K key) throws KeyNotFoundException{
		if (key == null) {
      		throw new KeyNotFoundException();
   		}


   		if(traverse == null){
   			throw new KeyNotFoundException();
   		}
   
   		int comp = traverse.key.compareTo(key);
   		System.out.println(comp);
   		
   		if(comp == 0){
   			return (V)traverse.value;
   		}else if(comp > 0){
   			if(traverse.left == null){
   				throw new KeyNotFoundException();
   			}else{
   				return findhelp(traverse.left, key);
   			}
   		}else if(comp < 0){
   			if(traverse.right == null){
   				throw new KeyNotFoundException();
   			}else{
   				return findhelp(traverse.right, key);
   			}
   			
   		}
			
			throw new KeyNotFoundException();
   	}


   		/*
   		System.out.println(cmp);
   		if (cmp > 0) {
     		findhelp(traverse.left, key);
  		 
   		}else if (cmp < 0) {
      		findhelp(traverse.right, key);
   		
   		}else {
      	
      		return (V)traverse.value;
   		}
   		System.out.println(traverse.value);
   		traverse = root;
   		findhelp(traverse.right, key);
   		return null;
   		*/
	

	//
	// Purpose:
	//
	// Return the number of nodes in the tree.
	//
	// Returns:
	//	the number of nodes in the tree.
	public int size() {
		System.out.println("out of size" + count);
		//count = 100;
		return count;
	}

	//
	// Purpose:
	//	Remove all nodes from the tree.
	//
	public void clear() {
		count = 0;
		root = null;
		return;
	}

	//
	// Purpose:
	//
	// Return the height of the tree.  We define height
	// as being the number of nodes on the path from the root
	// to the deepest node.
	//
	// This means that a tree with one node has height 1.
	//
	// Examples:
	//	See the assignment PDF and the test program for
	//	examples of height.
	//
	
	public int height(){
		return height(root);
		
	}


	public int height(BSTNode h) {
		if(h == null){
			return 0;
		}else{
			int rheight = height(h.right);
			int lheight = height(h.left);
			
			if(lheight > rheight){
				return lheight + 1;
			}else{
				return rheight + 1;
			}

		}
		
	}

	//
	// Purpose:
	//
	// Return a list of all the key/value Entrys stored in the tree
	// The list will be constructed by performing a level-order
	// traversal of the tree.
    //
    // A level order traversal of a tree cannot be done without the help
    //  of a secondary data structure
    //
    // It is commonly implemented using a queue of nodes as the secondary
    //  data structure.
    //  You will still be adding the "visited" elements to l as you do in the other
    //  traversal methods but you will create an additional q to hold nodes still to visit
    //
    //  From wikipedia (they call it breadth-first), the algorithm for level order is:
    //
    //    levelorder()
    //        q = empty queue
    //        q.enqueue(root)
    //        while not q.empty do
    //            node := q.dequeue()
    //            visit(node)
    //            if node.left != null then
    //                  q.enqueue(node.left)
    //            if node.right != null then
    //                  q.enqueue(node.right)
    //
    // Note that you can use the Java LinkedList as a Queue
    //  and then use only the removeFirst() and addLast() methods on q
    //
	public List<Entry<K,V> >	entryList() {


		List<Entry<K,V> > l = new LinkedList<Entry<K,V> >(); //hold all ementes of traversal
		
		LinkedList<BSTNode<K,V> > q = new LinkedList<BSTNode<K,V>>();;

		q.addLast(this.root);

		//System.out.println(q.toString());

		System.out.println(q.size());

		while(!(q.size() == 0)){
			BSTNode<K,V> node = q.removeFirst();
			//visit(node)

			Entry<K,V> enter = new Entry<K,V>(node.key, node.value);

			//create new entry
			l.add(enter);

			if(node.left != null){
				q.addLast(node.left);
			}

			if(node.right != null){
				q.addLast(node.right);
			}

			//System.out.println(node.toString());
		}

		System.out.println(q.size());


		System.out.println(l.toString());
		return l;

		
	}

	//
	// Purpose:
	//
	// Return a list of all the key/value Entrys stored in the tree
	// The list will be constructed by performing a traversal
	// specified by the parameter which.
	//
	// If which is:
	//	BST_PREORDER	perform a pre-order traversal
	//	BST_POSTORDER	perform a post-order traversal
	//	BST_INORDER	perform an in-order traversal
	//
	


	public List<Entry<K,V> >	entryList (int which) {
		List<Entry<K,V> > l = new LinkedList<Entry<K,V> >();
		
		if(which == 1){
			dopre(root, l);
		}

		if(which == 2){
			dopost(root, l);
		}

		if(which == 3){
			doin(root, l);
		}


		return l;
	}


	public void dopost(BSTNode<K,V> x, List<Entry<K,V>> l){
		if(!(x == null)){
			Entry entry = new Entry(x.key, x.value);
			dopost(x.left, l);
			dopost(x.right, l);
			l.add(entry);
		}
	}


	public void dopre(BSTNode<K,V> x, List<Entry<K,V>> l){
		if(!(x == null)){
			Entry entry = new Entry(x.key, x.value);
			l.add(entry);
			dopre(x.left, l);
			dopre(x.right, l);
			
		}
	}


	public void doin(BSTNode<K,V> x, List<Entry<K,V>> l){
		if(!(x == null)){
			Entry entry = new Entry(x.key, x.value);
			doin(x.left, l);
			l.add(entry);
			doin(x.right, l);
			
		}
	}

	// Your instructor had the following private methods in their solution:
	// private void doInOrder (BSTNode<K,V> n, List <Entry<K,V> > l);
	// private void doPreOrder (BSTNode<K,V> n, List <Entry<K,V> > l);
	// private void doPostOrder (BSTNode<K,V> n, List <Entry<K,V> > l);
	// private int doHeight (BSTNode<K,V> t)
}

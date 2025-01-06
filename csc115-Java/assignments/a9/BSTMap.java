import java.util.*;

public class BSTMap<K extends Comparable<K>, V > implements  Map<K, V>  {

	private BinarySearchTree<K,V> bst;

	BSTNode<K,V>	root;
	int count;

	public BSTMap () {
		bst = new BinarySearchTree<K,V>();
		root = null;
		count = 0;
	}

	public boolean containsKey(K key) {
		try{
			V value = get(key);
			return true;
		}catch(KeyNotFoundException e){
			//throw new KeyNotFoundException();
			return false;
		}
		
		
		
	}

	public V get(K key) throws KeyNotFoundException {
		try{
			return get(root, key);
		}catch(KeyNotFoundException e){
			throw new KeyNotFoundException();
		}
		
	}

	public V get (BSTNode n, K key) throws KeyNotFoundException {
		if(key == null){
			throw new KeyNotFoundException();
		}

		if(n == null){
			throw new KeyNotFoundException();
		}


		int c = n.key.compareTo(key);

		if(c > 0){
			return get(n.left, key);
		}else if(c < 0){
			return get(n.right, key);
		}else{
			return (V)n.value;
		}



		//return null;
	}

	public List<Entry<K,V> >	entryList() {
		

		return null;
	}

	
	 public void put(K key, V value){
       	insert(root, key, value);
    }

    private void insert(BSTNode traverse, K key, V value){
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
				insert(traverse.left, key, value);
				
			}
			 
			
		}else if(comp < 0){

			if(traverse.right == null){
				traverse.right = new BSTNode(key,value);
				count += 1;
			}else{
				 insert(traverse.right, key ,value);
				
			}
		
		}else{
			if(comp == 0){
				traverse.value = value;
			}
		}

		}



	public int size() {
		return count;
	}

	public void clear() {
		root = null;
		count = 0;
	}

}

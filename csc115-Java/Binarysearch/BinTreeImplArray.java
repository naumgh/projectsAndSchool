public class BinTreeImplArray<ItemType> implements BinTree<ItemType> {
	
	private static int free = 0;	
	private static Object[] data = new Object[1000];
	
	private static void initialize(int size) {
		free = 0;
		data = new Object[size];
	}
	
	private ItemType root;
	private int index;
	private int left;
	private int right;
	
	public BinTreeImplArray() {
		root = null;
		index = free;
		data[free++]=this;
		// should check for max size to prevent overflow
	}

	// setting the root of the tree
	// item is the input for the root

	public BinTree<ItemType> setRoot(ItemType item) {
		if (isEmpty()) {
			left = free;
			new BinTreeImplArray();
			free++;	
			right = free;
			new BinTreeImplArray();	
			free++;
		}
		root = item;
		return this;
	};
	
	// setting the left and right subtrees

	public BinTree<ItemType> setLeft(BinTree<ItemType> l) {
		left = ((BinTreeImplArray<ItemType>)l).getIndex();
		return this;
	}

	public BinTree<ItemType> setRight(BinTree<ItemType> r) {
		right = ((BinTreeImplArray<ItemType>)r).getIndex();
		return this;
	}

	// getting the root

	public ItemType getRoot() {
		return root;
	}
	
	// get the left and right subtrees

	public BinTree<ItemType> getLeft() {
		return (BinTree<ItemType>) data[left];
	};

	public BinTree<ItemType> getRight() {
		return (BinTree<ItemType>) data[right];
	}

	// tests if tree is empty

	public boolean isEmpty() {
		return root == null; 
	}
	
	public int getIndex() {
		return index;
	}
}
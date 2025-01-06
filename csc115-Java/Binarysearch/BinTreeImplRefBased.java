public class BinTreeImplRefBased<ItemType> implements BinTree<ItemType>{
	
private ItemType root;

private BinTree<ItemType> left, right;
	
BinTreeImplRefBased() {
	root = null;
	left = null;
	right = null;
}

public Boolean isEmpty() {
	return root == null;
}


public BinTree<ItemType> setRoot(ItemType item) {
	if (isEmpty()) {
		left = new BinTreeImplRefBased<ItemType>();
		right = new BinTreeImplRefBased<ItemType>();
	}
	root = item;
	return this;
}


// getting the root (of type ItemType)

public ItemType getRoot() {
	return root;
}
	
// setting the subtrees

public BinTree<ItemType> setLeft(BinTree<ItemType> left) {
	this.left = left;
	return this;
}

public BinTree<ItemType> setRight(BinTree<ItemType> right) {
	this.right = right;
	return this;
}

// retrieving the subtrees

public BinTree<ItemType> getLeft() {
	return left;
}

public BinTree<ItemType> getRight() {
	return right;
}

}
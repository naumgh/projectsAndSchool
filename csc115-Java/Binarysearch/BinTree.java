public interface BinTree<ItemType> {
	
//  creation

// done using the constructor of the implementation
// cannot be defined in interface in Java


//	test if tree is empty

Boolean isEmpty();


//	setting the root (item of type ItemType)

BinTree<ItemType> setRoot(ItemType item);


// getting the root (of type ItemType)

ItemType getRoot();
	
// setting the subtrees

BinTree<ItemType> setLeft(BinTree<ItemType> left);

BinTree<ItemType> setRight(BinTree<ItemType> right);

// retrieving the subtrees

BinTree<ItemType> getLeft();

BinTree<ItemType> getRight();
}
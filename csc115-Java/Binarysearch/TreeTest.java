public class TreeTest {
	public static void main(String[] args) {
		BinTree<Integer> t;
		
		t= create(5)
			.setLeft(create(1)
				      .setRight(create(4)
						         .setLeft(create(8))))
			.setRight(create(2)
					   .setLeft(create(3)
								  .setLeft(create(7)))
					   .setRight(create(6)));						 
		
		System.out.println(traverse(t));
		
		
	}
	
	public static BinTree<Integer> create() {
		BinTree<Integer> newTree = null;
		
		newTree = new BinTreeImplRefBased<Integer>();
		
		return newTree;
	}
	
	public static BinTree<Integer> create(int i) {
		return create().setRoot(i);
	}
	
	public static String traverse(BinTree<Integer> t) {
		if (t.isEmpty())
			return "";
		else return t.getRoot() + " " + traverse(t.getLeft()) + " " + traverse(t.getRight()); 
	}
		
}
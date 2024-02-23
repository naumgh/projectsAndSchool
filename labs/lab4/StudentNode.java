public class StudentNode {
	public StudentNode next;
	private Student data;

	public StudentNode(Student data){
		//this.next = next;
		this.data = data;

	}

	public StudentNode(Student data, StudentNode next){
		this.next = next;
		this.data = data;


	}


	public StudentNode getNext(){
		return this.next;
	}

	public void setNext(StudentNode next){
		this.next = next;
	}

	public Student getData(){
		return this.data;
	}

	public void setData(Student data){
		 this.data = data;


	}





}
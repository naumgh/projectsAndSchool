

public class C {

int x;

public C() {

System.out.println("C constructor 1");
this.x = 0;

}

public C(int x) {

this.x = x;
System.out.println("C constructor 2");}

public void foo() {
System.out.println("C foo:"  + x);
}
}



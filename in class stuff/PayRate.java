public class PayRate {
private int hrsPerWeek;
private double wagePerHour;

public PayRate() {
hrsPerWeek = 0;
wagePerHour = 0.0;
System.out.println("A");

}


//(int, double) -> void
public PayRate(int hrsPerWeek, double wagePerHour) {

this.hrsPerWeek = hrsPerWeek;
this.wagePerHour = wagePerHour;
System.out.println("B");

}

public void setHours(int hrsPerWeek) {

this.hrsPerWeek = hrsPerWeek;

}

public int getHours() {

return this.hrsPerWeek;

}

public void setWage(double wagePerHour) {
this.wagePerHour = wagePerHour;

}

public double getWage() {
return this.wagePerHour;
}

public int getSalary() {

return (hrsPerWeek * (int) wagePerHour * 52);

}
public boolean equals(PayRate pr) {

return this.getSalary() == pr.getSalary();

}

public String toString() {
return hrsPerWeek + "*" + wagePerHour + " per week";

}

public void giveRaise(int percent) {

// you will implement this in Question 4
}



public static void main(String[] args) {
PayRate prate1;
PayRate prate2;
System.out.println("C:");

PayRate prate3 = new PayRate();
System.out.println("D:" + prate3.getWage());

PayRate prate4 = prate3;
prate1 = new PayRate(20, 40.97);
prate2 = new PayRate(40, 15.90);
System.out.println("E:" + prate2);
prate3 = prate2;prate3.setWage(20.27);
System.out.println("F:" + prate1.getWage());
System.out.println("G:" + prate2.getWage());
System.out.println("H:" + prate3.getWage());
System.out.println("I:" + prate4.getWage());
System.out.println("J:" + prate1.equals(prate4));
System.out.println("K:" + prate1.equals(prate3));

}

}



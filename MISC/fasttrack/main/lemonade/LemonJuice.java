package lemonade;

public class LemonJuice {
    private int amount;
    private String unit;

    // defining constructor (all classes have a default cconstructor)
    public LemonJuice(int amount, String unit) {
        this.amount = amount;
        this.unit = unit;
    }

    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }

}

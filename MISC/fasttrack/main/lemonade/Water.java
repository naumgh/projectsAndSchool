package lemonade;

public class Water {
    private int amount;
    private String unit;

    public Water(int amount, String unit) {
        super();
        this.amount = amount;
        this.unit = unit;
    }

    public void drink(int amount) {
        if (this.amount < amount) {
            throw new IllegalArgumentException("Not enough water to drink. amount of water avaliable: " + this.amount);
        } else {
            this.amount -= amount;
        }

    }
}

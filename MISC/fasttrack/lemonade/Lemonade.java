package lemonade;

public class Lemonade {
    LemonJuice lemonJuice;
    Sugar sugar;
    Water water;

    // default constructor (all classes have a default constructor)
    public Lemonade(LemonJuice lemonJuice, Sugar sugar, Water water) {
        this.lemonJuice = new LemonJuice(0, "ml");
        this.sugar = new Sugar(0, "tst");
        this.water = water;
    }

    // overloading
    public Lemonade(LemonJuice lemonJuice, Water water) {
        this.lemonJuice = lemonJuice;
        this.water = water;
    }

}

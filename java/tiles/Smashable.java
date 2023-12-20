package tiles;

import ingredients.Burger;

public class Smashable extends Tile {
    private int hardness;
    private boolean broken = false;

    public void init(int h) {
        hardness = h;
    }

    public boolean onEnter(Burger b) {
        return broken;
    }

    public void interact(Burger b) {
        if (b.getStrength() >= hardness) broken = true;
    }
}

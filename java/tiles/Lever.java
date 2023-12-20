package tiles;

import ingredients.Burger;

public class Lever extends Tile {
    private int height;
    private Tile device;

    public void init(int h, Tile d) {
        height = h;
        device = d;
    }

    public boolean onEnter(Burger b) {
        return false;
    }

    public void interact(Burger b) {
        if (b.getHeight() >= height) device.toggle();
    }
}

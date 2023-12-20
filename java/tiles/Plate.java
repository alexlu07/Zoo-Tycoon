package tiles;

import ingredients.Burger;

public class Plate extends Tile {
    private int weight = 0;
    private Tile device;

    public void init(int w, Tile d) {
        weight = w;
        device = d;
    }

    public boolean onEnter(Burger b) {
        if (b.getWeight() >= weight) device.activate();
        return true;
    }

    public boolean onLeave(Burger b) {
        device.deactivate();
        return true;
    }
}

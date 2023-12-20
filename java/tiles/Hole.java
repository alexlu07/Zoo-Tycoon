package tiles;

import ingredients.Burger;

public class Hole extends Tile {
    private int height;

    public void init(int h) {
        height = h;
    }

    public boolean onEnter(Burger b) {
        return b.getHeight() <= height;
    }
}

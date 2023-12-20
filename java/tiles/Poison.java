package tiles;

import ingredients.Burger;

public class Poison extends Tile {
    public boolean onEnter(Burger b) {
        b.kill();
        return true;
    }
}

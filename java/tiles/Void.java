package tiles;

import ingredients.Burger;

public class Void extends Tile {
    public boolean onEnter(Burger b) {
        return b.topAbility() == "fly";
    }
}

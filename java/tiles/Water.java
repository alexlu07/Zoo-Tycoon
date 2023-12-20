package tiles;

import ingredients.Burger;

public class Water extends Tile{
    public boolean onEnter(Burger b) {
        return b.botAbility() == "swim" || b.topAbility() == "fly";
    }
}

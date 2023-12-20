package tiles;

import ingredients.Burger;

public class Tile {

    public boolean onEnter(Burger b) {return true;}
    public boolean onLeave(Burger b) {return true;}

    public void interact(Burger b) {}
    public void activate() {};
    public void deactivate() {};
    public void toggle() {};
}

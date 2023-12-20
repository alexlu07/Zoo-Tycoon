package tiles;

import ingredients.Burger;

public class Gate extends Tile {
    private boolean original;
    private boolean state = false;

    public void init(boolean o) {
        original = o;
    }

    public boolean onEnter(Burger b) {
        return original ^ state;
    }

    public void activate() {
        state = true;
    }

    public void deactivate() {
        state = false;
    }

    public void toggle() {
        state = !state;
    }
}

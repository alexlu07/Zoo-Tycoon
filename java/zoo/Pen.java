package zoo;

import ingredients.BaseAnimal;

public class Pen {

    /*
     * 0: Bird
     * 1: Fish
     * 2: Giraffe
     * 3: Rat
     * 4: Elephant
     * 5: Kangaroo
     */

    private static int[][] cost = {
        { 1, 2, 3, 4, 1000000 },
        { 1, 2, 3, 4, 1000000 },
        { 1, 2, 3, 4, 1000000 },
        { 1, 2, 3, 4, 1000000 },
        { 1, 2, 3, 4, 1000000 },
        { 1, 2, 3, 4, 1000000 },
    };

    public static int getLevel(int a) {
        if (a == -1) return BurgerPen.getLevel();
        return BaseAnimal.getLevel(a);
    }

    public int getCost(int a) {
        if (a == -1) return BurgerPen.getCost();
        return cost[a][getLevel(a)];
    }
    
    public void upgrade(int a) {
        if (a == -1) {BurgerPen.upgrade(); return;}
        BaseAnimal.upgrade(a);
    }
    
}

class BurgerPen {

    private static int level = 0;
    private static int[] cost = {1, 2, 3, 1000000};

    public static int getLevel() {return level;}
    public static int getCost() {return cost[level];}
    public static void upgrade() {level++;}
}

package ingredients;

public class BaseAnimal {

    /*
     * 0: Bird
     * 1: Fish
     * 2: Giraffe
     * 3: Rat
     * 4: Elephant
     * 5: Kangaroo
     */

    private static int[] level = {0, 0, 0, 0, 0, 0};

    private static int[][] strength = {
        { 1, 2, 3, 4, 5 },
        { 1, 2, 3, 4, 5 },
        { 1, 2, 3, 4, 5 },
        { 1, 2, 3, 4, 5 },
        { 1, 2, 3, 4, 5 },
        { 1, 2, 3, 4, 5 },
    };

    private static int[][] height = {
        { 1, 2, 3, 4, 5 },
        { 1, 2, 3, 4, 5 },
        { 1, 2, 3, 4, 5 },
        { 1, 2, 3, 4, 5 },
        { 1, 2, 3, 4, 5 },
        { 1, 2, 3, 4, 5 },
    };

    private static int[][] weight = {
        { 1, 2, 3, 4, 5 },
        { 1, 2, 3, 4, 5 },
        { 1, 2, 3, 4, 5 },
        { 1, 2, 3, 4, 5 },
        { 1, 2, 3, 4, 5 },
        { 1, 2, 3, 4, 5 },
    };

    private static String[] topAbility = {"fly", "none", "none", "none", "none", "pocket"};
    private static String[] botAbility = {"none", "swim", "none", "none", "none", "none"};

    public static void upgrade(int a) {level[a]++;}
    public static int getLevel(int a) {return level[a];}
    public static int getStrength(int a) {return strength[a][level[a]];}
    public static int getWeight(int a) {return weight[a][level[a]];}
    public static int getHeight(int a) {return height[a][level[a]];}
    public static String topAbility(int a) {return topAbility[a];} 
    public static String botAbility(int a) {return botAbility[a];}

}

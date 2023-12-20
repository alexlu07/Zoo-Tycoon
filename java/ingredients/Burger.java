package ingredients;

import java.util.ArrayList;

public class Burger {
    private ArrayList<Integer> stack;
    private Burger passenger;

    public boolean addIngredient(int ingredient) {
        if (stack.isEmpty() || getWeight() <= getStrength()) {
            stack.add(ingredient);
            return true;
        }

        return false;
    }

    public int getStrength() {
        return BaseAnimal.getStrength(stack.get(0));
    }

    public int getWeight() {
        return stack.stream().mapToInt(a -> BaseAnimal.getWeight(a)).sum();
    }

    public int getHeight() {
        // int h = stack.stream().mapToInt(a -> BaseAnimal.getHeight(a)).sum();
        // if (passenger != null) h += passenger.stack.stream().mapToInt(a -> BaseAnimal.getHeight(a)).sum();

        // return h;

        // ^deleted because ima make so kangaroo doesn't add to height
        return stack.stream().mapToInt(a -> BaseAnimal.getHeight(a)).sum();
    }

    public String topAbility() {
        return BaseAnimal.topAbility(stack.get(stack.size()-1));
    }

    public String botAbility() {
        return BaseAnimal.botAbility(stack.get(0));
    }

    public void kill() {
        stack.remove(0);
    }

    public boolean dead() {
        return stack.isEmpty();
    }

}
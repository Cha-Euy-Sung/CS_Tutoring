package forestfires;

/**
 *
 * @author mmonsalv
 */
public class FFTree {

    private int x, y;
    private int burnday = 0;

    // constructor--it receives a location (x,y)
    public FFTree(int x, int y) {
        this.x = x;
        this.y = y;
    }

    // days while burning == 1
    public void setFire() {
        if (burnday == 0) {
            burnday = 1;
        }
        // short version:
        // burnday += (burnday==0)?1:0;
    }

    // true iff the tree is burning
    public boolean isBurning() {
        return (burnday > 0 && burnday < 4);
    }

    // true iff the true has completed burning
    public boolean isBurnt() {
        return (burnday > 3);
    }

    // advances a day--has an effect only if the tree is burning
    public void newDay() {
        if (burnday > 0) {
            burnday++;
        }
    }

    // returns the original x-part of the location
    public int getX() {
        return x;
    }

    // returns the original y-part of the location
    public int getY() {
        return y;
    }

    // computes the Euclidean distance to another tree
    public double distanceTo(FFTree other) {
        int dx = this.x - other.x, dy = this.y - other.y;
        return Math.sqrt(dx * dx + dy * dy);
    }

}

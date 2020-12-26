package forestfires;

/**
 *
 * @author mmonsalv
 */
public class FFCustomSimulator extends FFSimulator{

    // constructor with two parameters--just as the one in FFSimulator
    public FFCustomSimulator(int forest_size, int fire_size) {
        super(forest_size, fire_size);
    }
    
    // empty constructor--works as FFSimulator(500,2)
    public FFCustomSimulator() {
        super(500, 2);
    }
    
    // constructor with FFTree array--it copies the array to
    // the myforest field
    public FFCustomSimulator(FFTree[] aforest) {
        super(1, 1);
        super.myforest = aforest;
    }
    
    // Sets the animation speed. The parameter states how many
    // seconds uses a day in the simulation. The original speed
    // is 0.1 seconds per day.
    public void setFrameSpeed(double delay) {
        wait_time = delay;
    }
    
    // Sets the distance for the spread of fire. Initially, the
    // distance is set to 20 pixels (method spreadFire).
    public void setSpreadDistance(int dist) {
        this.dist = dist;
    }
    // field for the current reach of the fire
    private int dist = 20;

    // I need to override (overwrite?) this method to make the
    // simulation sensitive to the value of field 'dist'
    @Override
    public void spreadFire(FFTree[] burningTrees) {
        for (FFTree t : myforest) {
            for (FFTree b : burningTrees) {
                if (t.distanceTo(b) < dist) {
                    t.setFire();
                }
            }
        }
    }

    
}

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package demo;

/**
 *
 * @author mmonsalv
 */
public class Demo {

    // this method prints the contents of an integer array into the
    // standard output (text console)
    public static void printAr(int[] x) {
        for (int c : x) {
            System.out.print(c + " ");
        }
        System.out.println();
    }

    // the main--this method is called when we run Demo
    public static void main(String[] args) {
        int[] p = {1, 2, 3, 4, 5};
        int[] q = {-1, -2, -3, -4};
        printAr(p);
        printAr(q);
        
        // let us c
        int[] c = acClass(p, q);
        printAr(c);
    }

    /**
     * Method acDirect takes two integer arrays and returns
     * a new array containing the elements of a and then b
     * in their original order. It performs a concatenation.
     */
    public static int[] acDirect(int[] a, int[] b) {
        int[] result = new int[a.length + b.length];
        // copy elements a
        for (int i = 0; i < a.length; i = i + 1) {
            result[i] = a[i];
        }
        // copy the elements of b
        for (int i = 0; i < b.length; i = i + 1) {
            result[a.length + i] = b[i];
        }
        return result;
    }

    /**
     * Method acShort takes two integer arrays and returns
     * a new array containing the elements of a and then b
     * in their original order. It performs a concatenation.
     * This method's behavior is identical to acDirect's.
     */
    public static int[] acShort(int[] a, int[] b) {
	int[] result = new int[a.length + b.length];
	int i = 0;

	for (int x : a) {
	    result[i++] = x;
	}
	for (int x : b) {
	    result[i++] = x;
	}
	return result;
    }
    
    /**
     * Method acClass takes two integer arrays and returns
     * a new array containing the elements of a and then b
     * in their original order. It performs a concatenation.
     * This method's behavior is as acDirect's and acShort's.
     */
    public static int[] acClass(int[] a,int[] b) {
        ArrayClassContainer acc = new ArrayClassContainer( a.length+b.length);
        acc.putArray(a);
        acc.putArray(b);
        return acc.getArray();
    }

}


/**
 * The ArrayClassContainer class is an object that contains an integer
 * array into which it copies information from other arrays.
 */
class ArrayClassContainer{
    
    // fields: the result and the current index
    int[] result;
    int i = 0;
    
    // constructor
    public ArrayClassContainer(int size) {
        result = new int[size];
        // i = 0; this is an alternative
    }
    
    // this method copies the content of anArray into result, sequentially
    // after the last elements copies
    public void putArray(int[] anArray) {
        for(int x: anArray) {
            result[ i++ ] = x;
            //i = i % result.length;
            if (i >= result.length) i = 0;
        }
    }
    
    // it is in the culture of Java that, if you want to see the contents
    // of a field, you “need” to create a method that does so
    public int[] getArray() {
        return result;
    }
    
}













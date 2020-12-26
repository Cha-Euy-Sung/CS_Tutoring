package edutypes;


// DO NOT MODIFY THIS CLASS
public abstract class Person {}

// Define the following classes without using methods or fields;
// you can make them abstract, interfaces, or concrete classes,
// and you can subtype through extends, implements, or both.
interface Instructor {} 

class Professor extends Person implements Instructor { }

class Student extends Person{ }

class TeachingAssistant extends Student implements Instructor { }
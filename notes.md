# this is for testing phase
## this is smaller 
# Java OOPs Concepts


Java OOPs (Object Oriented Programming) is a programming concept in which 
everything is an object. In Java, everything is an object, and we can create 
objects by defining a class. A class is like a blueprint of an object. It 
defines the properties (data) and the methods (functions) of an object.

When we create an object, we are essentially creating an instance of a 
class. We can create as many objects as we want from the same class. Objects 
can have their own unique properties and behaviors.

Java OOPs also has concepts like inheritance, polymorphism, and encapsulation.
Inheritance is where one class can inherit the properties and methods of 
another class. Polymorphism is where we can have multiple functions with the 
same name but different parameters. Encapsulation is where we can hide the 
implementation details of an object by making the variables and methods private.

```java

public class Student {
    private String name;
    private int age;
    private double cgpa;

    public Student(String name, int age, double cgpa) {
        this.name = name;
        this.age = age;
        this.cgpa = cgpa;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public double getCgpa() {
        return cgpa;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public void setCgpa(double cgpa) {
        this.cgpa = cgpa;
    }
}

```
css 
js
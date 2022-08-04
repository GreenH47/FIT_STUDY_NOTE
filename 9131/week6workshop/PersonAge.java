public class PersonAge
{
    private String name;
    private int age;

    public PersonAge()
    {
        this.name = "";
        this.age = -1;
    }

    public PersonAge(String name, int age)
    {
        this.name = name;
        this.age = age;
    }

    public void display()
    {   
        System.out.println("Name: " + this.name + ", Age: " + this.age);
    }

    public void setAge(int a)
    {
        this.age = a;
    }
    
    public int getAge()
    {
        return this.age;
    }

    public String getName()
    {
        return this.name;
    }

}

public class Content
{
    private String name;
    private double dosage;

    public Content()
    {
        name = "Unknown";
        dosage = -1;
    }

    public Content(String name, double dosage)
    {
        this.name = name;
        this.dosage = dosage;
    }

    public double getDosage()
    {
        return dosage;
    }

    public String getName()
    {
        return name;
    }

    public void setDosage(double dosage)
    {
        this.dosage = dosage;
    }

    public void setName(String name)
    {
        this.name = name;
    }

    public String display()
    {
        return this.name + "," + this.dosage;
    }
}//Content.java


public class Tour
{
    private String  origin, destination;
    private int days, cost;

    public Tour(String origin, String destination,int days, int cost)
    {
        this.origin = origin;
        this.destination = destination;
        this.days = days;
        this.cost= cost;
    }

    public void setOrigin(String origin)
    {
        this.origin = origin;
    }

    public void setDestination(String destination)
    {
        this.destination = destination;
    }

    public void setDays(int days)
    {
        this.days = days;
    }

    public void setCost(int cost)
    {
        this.cost = cost;
    }

    public String display()
    {
        String text = "origin= " + this.origin + " destination= " + this.destination 
            + " days= " + this.days + " cost= " + this.cost;
        return text;
    }
}//Tour.java

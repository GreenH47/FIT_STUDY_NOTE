public class BoxArea
{
    private double length;
    private double width;
    private double height;

    public BoxArea()
    {
        length = -1.1;
        width = -2.2;
        height = -3.3;
    }

    public BoxArea(double length, double width, double height)
    {
        length = length;
        width = width;
        height = height;
    }

    public int calcArea()
    {
        return (int)(0.5 * length * width * height);
    }

    public double getHeight()
    {
        return height;
    }

    public double getLength()
    {
        return length;
    }

    public double getWidth()
    {
        return width;
    }

    public static void main(String[] args)
    {
        BoxArea objArea = new BoxArea(3, 5, 7);
        System.out.println("Area = " + objArea.calcArea());
    }

    public void setHeight(double height)
    {
        this.height = height;
    }

    public void setLength(double length)
    {
        this.length = length;
    }

    public void setWidth(double width)
    {
        this.width = width;
    }
}

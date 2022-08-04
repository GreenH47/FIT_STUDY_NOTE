import java.util.ArrayList;

public class Medicine
{
    private String name;
    private ArrayList<Content> contents;

    public Medicine()
    {
        name = "Unknown";
        contents = new ArrayList<>();
    }

    public Medicine(String name, ArrayList<Content> contents)
    {
        this.name = name;
        this.contents = contents;
    }

    public void addContent(String name, double dosage)
    {
        contents.add(new Content(name, dosage));
    }

    public ArrayList<Content> getContents()
    {
        return contents;
    }

    public String getName()
    {
        return name;
    }

    public Content getSpecificContent(int index)
    {
        return contents.get(index);
    }

    public void setContents(ArrayList<Content> contents)
    {
        this.contents = contents;
    }

    public void setName(String name)
    {
        this.name = name;
    }

    public void setSpecificContent(int index, Content content)
    {
        contents.set(index, content);
    }

    public String display()
    {
        String text = this.name;
        for(Content c:contents)
        {
            text += "," + c.display();
        }
        return text + "\n";
    }
}//Medicine.java

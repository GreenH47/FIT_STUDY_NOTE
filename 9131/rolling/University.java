import java.util.ArrayList

public class University
{
    private ArrayList<Enrolment> enrolments;

    public University()
    {
        this.enrolments = new ArrayList<Enrolment>();
    }

    public University(ArrayList<Enrolment> enrolments)
    {
        this.enrolments = enrolments;
    }

    public void addEnrolment(Enrolment enrolment)
    {
        enrolments.add(enrolment);
    }

    public String display()
    {
        //
    }

    public ArrayList<Enrolment> getEnrolment()
    {
        //
    }

    public int getEnrolmentSize()
    {
        return enrolments.size();
    }

    public Enrolment getSpecificEnrolment(int index)
    {
        if(index >= 0 && index < enrolments.size())
        {
           if(enrolments.get(index) != null)
           {
               enrolments.set(index,enrolment);
           }
            
        }
        else
        {
            //print not exist
        }
    }

    public void removeEnrolment(int index)
    {
        //
    }

    public void setEnrolments(ArrayList<Enrolment> enrolments)
    {
        //
    }

    public void setSpecificEnrolment(int index,Enrolment,enrolment)
    {
        //
    }


}

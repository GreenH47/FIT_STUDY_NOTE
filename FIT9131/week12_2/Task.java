public class Task
{
    private String priority;
    private String taskName;
    private String taskDescription;
    private String taskOwner;

    public Task()
    {
        this.priority = "";
        this.taskName = "";
        this.taskDescription = "";
        this.taskOwner = "";
    }

    public Task(String priority,String taskName,String taskDescription,String taskOwner)
    {
        this.priority = priority;
        this.taskName = taskName;
        this.taskDescription = taskDescription;
        this.taskOwner = taskOwner;
    }

    public String display()
    {
        return "Task priority= " + priority
                + "; TaskName = " + taskName
                + "; Task Description = " + taskDescription
                +";Task Owner = "+taskOwner;
    }
}//Task.java

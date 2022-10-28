import java.util.ArrayList;
import java.io.FileWriter;

public class Medication
{
    private ArrayList<Medicine> medicines;

    public Medication()
    {
        medicines = new ArrayList<Medicine>();
    }

    public Medication(ArrayList<Medicine> medicines)
    {
        this.medicines = medicines;
    }

    public ArrayList<Medicine> getMedicines()
    {
        return medicines;
    }

    public Medicine getSpecificMedicine(int index)
    {
        return medicines.get(index);
    }

    public static void main(String[] args)
    {
        Medication medication = new Medication();
        medication.storeMedicines();
        medication.writeToFile();
    }
    
    public void storeMedicines()
    {
        Medicine medicine = new Medicine();
        medicine.setName("Lomotil");
        medicine.addContent("Diphenoxylate Hydrochloride", 20);
        medicine.addContent("Atropine Suphate", 10);
        medicines.add(medicine);

        medicine = new Medicine();
        medicine.setName("Cenovis Multi Vitamins");
        medicine.addContent("Calcium", 80);
        medicine.addContent("Zinc", 15);
        medicine.addContent("Folic Acid", 0.3);
        medicine.addContent("Boron", 1);
        medicines.add(medicine);

        medicine = new Medicine();
        medicine.setName("Mega Zinc 40mg");
        medicine.addContent("Zinc Amino Acid Chelate", 200);
        medicine.addContent("Pyridoxine Hydrochloride", 20);
        medicine.addContent("Betacarotene", 3);
        medicines.add(medicine);
    }

    public void setMedicines(ArrayList<Medicine> medicines)
    {
        this.medicines = medicines;
    }

    public void setSpecificMedicine(int index, Medicine medicine)
    {
        medicines.set(index, medicine);
    }

    public void writeToFile()
    {
        try(FileWriter writer = new FileWriter("medication.txt",true))
        {
            for(Medicine medicine: medicines)
            {
                writer.append(medicine.display());
            }
        }
        catch(Exception e)
        {
            System.out.println("file can not write");
        }
    }
}//Medication.java

## Assignment No. 3

### Creating an Application in Salesforce.com Using Apex Programming Language

---

## Step 1 - Open Salesforce Login Page

Open the Salesforce Developer Edition login page:

[Salesforce Login](https://login.salesforce.com?utm_source=chatgpt.com)

Login using your Salesforce Developer Edition account.

---

## Step 2 - Open Developer Console

After logging in:

1. Click the Gear icon at the top-right corner.
2. Click **Developer Console**.

The Salesforce Developer Console window will open.

---

## Step 3 - Create New Apex Class

Inside Developer Console:

1. Click **File -> New -> Apex Class**.
2. Enter class name: `StudentManager`.
3. Click **OK**.

---

## Step 4 - Write Apex Code

Delete all default code and paste the following Apex program:

```java
public class StudentManager {

   // Method to create student record and assign grade
   public static void createStudent(String name, Integer marks) {

      String grade;

      // Grade calculation logic
      if (marks >= 75) {
         grade = 'Distinction';
      } else if (marks >= 60) {
         grade = 'First Class';
      } else if (marks >= 40) {
         grade = 'Pass';
      } else {
         grade = 'Fail';
      }

      // Display output in debug log
      System.debug('Student Name : ' + name);
      System.debug('Marks        : ' + marks);
      System.debug('Grade        : ' + grade);
   }

   // Main method
   public static void showAll() {

      System.debug('--- Student Records ---');

      createStudent('Gargi', 85);
      createStudent('Soham', 62);
      createStudent('Vedika', 45);
      createStudent('Raj', 30);
   }
}
```

---

## Step 5 - Save the Program

Press **Ctrl + S**. The dot/star near `StudentManager.apxc` should disappear after a successful save.

---

## Step 6 - Execute the Program

1. Click **Debug -> Open Execute Anonymous Window**.
2. Paste the following code:

```java
StudentManager.showAll();
```

3. Tick **Open Log**.
4. Click **Execute**.

---

## Step 7 - View Output

After execution, the Execution Log window will open. At the bottom, tick **Debug Only**.

Output will appear like:

```text
--- Student Records ---

Student Name : Gargi
Marks        : 85
Grade        : Distinction

Student Name : Soham
Marks        : 62
Grade        : First Class

Student Name : Vedika
Marks        : 45
Grade        : Pass

Student Name : Raj
Marks        : 30
Grade        : Fail
```

---

## Step 8 - View Apex Class in Salesforce Setup

To view the Apex class from the Salesforce dashboard:

1. Go back to the Salesforce main page.
2. Click **Gear icon -> Setup**.
3. In **Quick Find**, type **Apex Classes**.
4. Click **Apex Classes**.
5. Click **StudentManager**.

The class details page will show:

- Apex Class Name
- Class Body
- Code
- Created By
- Status
- Metadata Information

---

## Output

The Apex program successfully:

- Created student records.
- Calculated grades.
- Displayed output using `System.debug()`.
- Executed on Salesforce cloud platform.

---

## Conclusion

We successfully created and executed an application in Salesforce.com using Apex programming language. The application was executed on the Salesforce cloud platform using the Developer Console and generated student grade records successfully.

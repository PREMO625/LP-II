## What You Are Making

Mini Project: **Student Record Management System**

Using:

- Salesforce Lightning Experience
- Custom Object
- Fields
- Records
- Lightning App

No heavy coding required.

---

## What You Will Show the Examiner

You will show:

- ✅ Custom object
- ✅ Fields
- ✅ Records
- ✅ App/tab
- ✅ Cloud dashboard

This fully satisfies Assignment 4.

---

## Full Practical Flow (Exact)

### Step 1 - Login to Salesforce

Go to **Salesforce Login** and log in using your Developer account.

### Step 2 - Open Setup

Top-right: ⚙️ Gear icon -> **Setup**. Wait for the Setup page to open.

### Step 3 - Create Custom Object

In the left **Quick Find** search box, type **Object Manager**, then click **Object Manager**.

Top-right: **Create -> Custom Object**.

### Step 4 - Fill Object Details

Fill exactly this:

| Field | Value |
| --- | --- |
| Label | Student Record |
| Plural Label | Student Records |
| Object Name | Student_Record |
| Record Name | Student Name |

Leave most settings default, then click **Save**.

### Step 5 - Create Fields

Inside **Student Record** object:

- Click **Fields & Relationships**.
- Click **New**.

#### Field 1 - Marks

Select **Number**, click **Next**.

Fill:

| Field | Value |
| --- | --- |
| Field Label | Marks |
| Length | 3 |
| Decimal Places | 0 |

Click **Next -> Next -> Save**.

#### Field 2 - Grade

Click **New**, select **Text**.

Fill:

| Field | Value |
| --- | --- |
| Field Label | Grade |
| Length | 50 |

Click **Next -> Next -> Save**.

You now have:

- Student Name
- Marks
- Grade

### Step 6 - Create Tab

In **Quick Find**, type **Tabs**, then click **Tabs**.

Scroll to **Custom Object Tabs**, click **New**.

### Step 7 - Select Object

Object: **Student Record**. Choose any icon/color.

Click **Next -> Next -> Save**.

### Step 8 - Open Sales App

Top-left: Waffle icon (9 dots) -> **View All** -> **Sales**.

### Step 9 - Add Student Records Tab

At the top navigation bar, click **More**.

- If **Student Records** is visible, click it.
- If not, click **Edit Navigation** (pencil icon), search **Student Records**, add it, and save.

### Step 10 - Add Records

Open **Student Records** -> **New**.

Add the following records:

**Record 1**

| Field | Value |
| --- | --- |
| Student Name | Gargi |
| Marks | 85 |
| Grade | Distinction |

**Record 2**

| Field | Value |
| --- | --- |
| Student Name | Soham |
| Marks | 62 |
| Grade | First Class |

**Record 3**

| Field | Value |
| --- | --- |
| Student Name | Vedika |
| Marks | 45 |
| Grade | Pass |

Save each record.

### Step 11 - Show Output

You will see the records list. This screen is your output, screenshot, and final result.

Practical complete.
### **What is Normalization?**
* Normalization is the process of **organizing the data** in the database.
* The Normalization form is used to reduce redundancy from the database table, and improve data integrity.
* Normalization divides the larger table into smaller and links them using relationships using foreign keys.
* It is also used to eliminate undesirable characteristics like Insertion, Update, and Deletion Anomalies.
* HINDI:- 
  * Normalization database ko organize karne ki process hai jisse:
    * Data redundancy (duplicate data) kam ho
    * Data consistency bani rahe
    * Insert, Update aur Delete anomalies na aaye
    * Tables ko relationships (Primary Key aur Foreign Key) ke through connect kiya ja sake

#### Why do we need Normalization?
* Normalization is used to **organize data in a database**, reduce data redundancy (duplicate data), improve data integrity, and eliminate insertion, update, and deletion anomalies.

#### Benefits of Normalization
1. Reduces Data Redundancy:- Same data baar-baar store nahi karna padta.
2. Improves Data Integrity:- Data consistent aur accurate rehta hai.
3. Avoids Update Anomalies:- Ek value change karne par multiple rows update nahi karni padti.
4. Avoids Insert Anomalies:- Naya data insert karna aasaan hota hai.
5. Avoids Delete Anomalies:- Ek record delete karne se important information lose nahi hoti.
6. Better Database Design:- Tables logically organized rehti hain.

#### **Types of Normalization**
1. **First Normal Form (1NF)**
* Each column can have only **one type of data/value**, i.e, there cannot be more than one value in the same cell.
* All values in a column **must be of the same data type**, such as all names or all numbers
* Each record (row) must be unique identifier (primary key).

```sql
-- Unnormalized Table (UNF)
| OrderID | CustomerName | ProductName   |
| ------- | ------------ | ------------- |
| 1       | Alice        | Apple, Banana |
| 2       | Bob          | Banana        |

-- Normalized to 1NF
| OrderID | CustomerName | ProductName |
| ------- | ------------ | ----------- |
| 1       | Alice        | Apple       |
| 1       | Alice        | Banana      |
| 2       | Bob          | Banana      |
```

2. **Second Normal Form (2NF)**
* The table **should already be in 1NF**.
* Every non-prime attribute (which is not part of the primary key) in the table must depend on the entire primary key,
* suppose hame kisi data ka name change karna pada to sabhi column mai karna padega isliye id use karte hai
```sql
-- Unnormalized Table (UNF)
| std_id | course_id | std_name | course_name |
| ------ | --------- | -------- |-------------|
| 1      | 101       | Ram      | Math        |
| 2      | 101       | Sita     | Math        |
| 1      | 102       | Ram      | Hindi       |

-- Normalized to 2NF
| std_id | std_name |
| ------ | -------- |
| 1      | Ram      |
| 2      | Sita     |

| course_id | course_name |
| --------- |-------------|
| 101       | Math        |
| 102       | Hindi       |
```

3. तीसरा सामान्य रूप (3NF)
* Third Normal Form means the **table should be in 2NF**, and there should be **no transitive dependency**. Non-key attributes should depend only on the primary key, not on another non-key attribute.
- Remove the Transitive Dependency
- 3NF में हम यह सुनिश्चित करते हैं कि कोई ट्रांजिटिव डिपेंडेंसी (Transitive Dependency) न हो। इसका मतलब है कि अगर कॉलम A → B और कॉलम B → C है, तो हमें कॉलम C को टेबल से अलग करना होगा और उसे स्वतंत्र टेबल में रखना होगा।




#### Data modification anomalies can be categorized into three types:
* **Insertion Anomaly:** Insertion Anomaly refers to when one cannot insert a new tuple into a relationship due to lack of data.
* **Deletion Anomaly:** The delete anomaly refers to the situation where the deletion of data results in the unintended loss of some other important data.
* **Updatation Anomaly:** The update anomaly is when an update of a single data value requires multiple rows of data to be updated.

Notes:- Anomaly means 



### **Ques. What is Denormalization?**
DeNormalization is a technique used to access the data from higher to lower normal
forms of database. It is also process of introducing redundancy into a table by
incorporating data from the related tables.

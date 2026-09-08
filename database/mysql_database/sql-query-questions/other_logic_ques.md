|  No.  | Other Logical Questions                                                                                     |
| :---: | ----------------------------------------------------------------------------------------------------------- |
|       | [Replace a column value:- M to F & F to M](#replace-a-column-values-from-male-to-female-and-female-to-male) |


<div style="page-break-before: always;"></div>


### 🎯**Replace a Column Values from 'male' to 'female' and 'female' to 'male'**
```sql
UPDATE empdata
SET GENDER = CASE
    WHEN GENDER='male' THEN 'female'
    WHEN GENDER='female' THEN 'male'
    END;
(OR)
UPDATE EMPDATA 
SET gender = CASE 
    gender WHEN 'male' THEN 'female' 
            WHEN 'female' THEN 'male'
    ELSE gender
END;
```
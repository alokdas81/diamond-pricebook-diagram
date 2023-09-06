# A. Proposed DB Structure

Proposed Structure for storing the pricebook information.
[Click here](./data/pricelistDBStructure.json)

The above structure has been generated depending on the following files.
###### **Allegion**:
`GJ_Price_Book_12_Feb2023_CAN010061.pdf`,
`CAN110065_FAL_Price_Book_13_Feb2023_RevJun2023_07-05-23.pdf`,
`SCH_Residential_Price_Book_13_MRCAN1000.pdf`,
`CAN110962_Zero_Price_Book_10_Feb2023_RevJun2023_07-05-23.pdf`,
###### **KNC**:
`KNC - Price Book - Feb 26, 2023 18% Surcharge.pdf`
###### **NGP**:
`NGP - Price Book 2023.pdf`


###### **Some Constraints to keep in mind:**
1. Series will be active only when all base price adding will be completed.
2. fetures/options will be active as soon as they inserted into the DB.
3. To minimize the complexity, We will features treat as a new entry into the DB. i.e if one feature `model` will be associated with two siries `100 series` and `70 series` then their code will be different.
4. In backend we will use the `code` for referance and in UI user can see the `desc` as label.

# **B. Different paramiter list:**
Manufaturer wise PDF and their corresponding paramiter list.

- **B.1 - Allegion:**
  - [B.1.a - Glynn Jhonson](./data/Pricebook/Allegion/glynn_jhonson/README.md)
  - [B.1.b - Falcon](./data/Pricebook/Allegion/falcon/README.md)
  - [B.1.c - LCN](./data/Pricebook/Allegion/LCN/README.md)
  - [B.1.d - Zero](./data/Pricebook/Allegion/zero/README.md)
- **B.2 - Standard Metal Hardware:**
  - [B.2.a - Standard Metal Hardware-2021](./data/Pricebook/SMH/README.md)